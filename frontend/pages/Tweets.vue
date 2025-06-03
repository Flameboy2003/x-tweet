<template>
  <div class="min-h-screen flex">
    <div
      class="min-h-screen w-full p-6 bg-gray-100 bg-[url('/images/cont-bg2.avif')] bg-cover bg-center bg-no-repeat bg-fixed"
    >
      <h1
        class="title header font-bold text-transparent bg-clip-text p-3 text-white mb-2 text-center"
      >
        Stored Tweets
      </h1>

      <!-- Statistics Grid -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
        <div class="bg-white p-4 rounded-xl shadow-sm text-center">
          <div class="text-2xl font-bold text-gray-800">{{ formatCount(tweetsCount) }}</div>
          <div class="text-sm text-gray-500 mt-1">TWEETS</div>
        </div>

        <div class="bg-white p-4 rounded-xl shadow-sm text-center">
          <div class="text-2xl font-bold text-gray-800">{{ formatCount(impressionsCount) }}</div>
          <div class="text-sm text-gray-500 mt-1">IMPRESSIONS</div>
        </div>

        <div class="bg-white p-4 rounded-xl shadow-sm text-center">
          <div class="text-2xl font-bold text-gray-800">{{ formatCount(reachCount) }}</div>
          <div class="text-sm text-gray-500 mt-1">REACH</div>
        </div>

        <div class="bg-white p-4 rounded-xl shadow-sm text-center">
          <div class="text-2xl font-bold text-gray-800">{{ formatCount(contributorsCount) }}</div>
          <div class="text-sm text-gray-500 mt-1">CONTRIBUTORS</div>
        </div>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div class="loading-spinner inline-block w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full mb-4"></div>
        <p class="text-white">Loading tweets...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="error-message max-w-md mx-auto text-center">
        {{ error }}
      </div>

      <!-- Content -->
      <div v-else>
        <!-- Empty State -->
        <div v-if="paginatedTweets.length === 0" class="text-center py-12">
          <div class="text-gray-400 text-6xl mb-4">-!-</div>
          <p class="text-gray-500 text-lg">No tweets found in the nest!</p>
        </div>

        <!-- Tweet Grid -->
        <div v-else>
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 items-stretch ">
            <div
              v-for="tweet in paginatedTweets"
              :key="tweet.tweet_id"
              class="tweet-card relative p-4 h-full hover:scale-105 transition-transform duration-300"
            >
              <div class="card bg-[#1b1c1e] border rounded-2xl border-white p-4 h-full flex flex-col justify-between">
                <div class="relative z-10 space-y-2 text-white">
                  <div class="username flex items-center gap-2 text-lg font-semibold mb-1">
                    <img :src="userIcon" alt="User Icon" class="h-5 w-5 text-blue-400" />
                    {{ tweet.username }}
                  </div>
                  <div class="flex gap-2 text-gray-200">
                    <img :src="commentIcon" alt="Comment Icon" class="h-5 w-5 text-blue-400" />
                    <p>{{ tweet.text }}</p>
                  </div>
                  <div class="flex gap-2 text-gray-200">
                    <img :src="clockIcon" alt="Clock Icon" class="h-5 w-5 text-blue-400" />
                    <p>{{ tweet.created_at }}</p>
                  </div>
                  <div class="flex items-center gap-1">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v16l4-4h12V4H4z" />
                    </svg>
                    <span>{{ tweet.retweet_count }}</span>
                  </div>
                  <div class="flex gap-2 text-gray-200">
                    <img :src="hashIcon" alt="Hashtag Icon" class="h-5 w-5 text-blue-400" />
                    {{ tweet.hashtags.join(', ') || 'None' }}
                  </div>
                  <div class="flex gap-2 text-gray-200">
                    <img :src="usersIcon" alt="Mentions Icon" class="h-5 w-5 text-blue-400" />
                    {{ tweet.mentions.join(', ') || 'None' }}
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Pagination -->
          <div class="mt-6 flex items-center justify-between flex-wrap gap-2">
            <div class="text-sm text-white">Showing {{ startItem }} to {{ endItem }} of {{ totalItems }} tweets</div>
            <div class="flex items-center space-x-2">
              <button @click="prevPage" :disabled="currentPage === 1" class="px-4 py-2 border rounded-lg flex items-center transition"
                :class="{
                  'border-gray-300 text-gray-400 cursor-not-allowed': currentPage === 1,
                  'border-indigo-300 text-indigo-600 hover:text-white hover:bg-white/20': currentPage > 1
                }">
                <svg class="w-5 h-5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
                </svg>
                Previous
              </button>

              <div class="flex space-x-1">
                <template v-for="page in visiblePages" :key="page">
                  <span v-if="page === '...'" class="w-10 h-10 flex items-center justify-center">...</span>
                  <button v-else @click="currentPage = page" class="w-10 h-10 flex items-center justify-center rounded-lg transition"
                    :class="{
                      'bg-indigo-600 text-white': page === currentPage,
                      'text-white hover:bg-white/20': page !== currentPage
                    }">
                    {{ page }}
                  </button>
                </template>
              </div>

              <button @click="nextPage" :disabled="currentPage === totalPages" class="px-4 py-2 border rounded-lg flex items-center transition"
                :class="{
                  'border-gray-300 text-gray-400 cursor-not-allowed': currentPage === totalPages,
                  'border-indigo-300 text-indigo-600 hover:text-white hover:bg-white/20': currentPage < totalPages
                }">
                Next
                <svg class="w-5 h-5 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      </div>

      <footer class="mt-12 py-6 text-center bg-[#1b1c1e] text-gray-500 text-sm border-t">
        © 2025 X-Tweet. All rights reserved.
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from "axios";

import userIcon from "@/assets/user.svg";
import usersIcon from "@/assets/users.svg";
import commentIcon from "@/assets/comment.svg";
import clockIcon from "@/assets/clock.svg";
import hashIcon from "@/assets/hash.svg";




const allTweets = ref([]);
const loading = ref(true);
const error = ref(null);
const itemsPerPage = 6;
const tweetsPerPage = ref(itemsPerPage);
const currentPage = ref(1);

// Statistics
const tweetsCount = computed(() => allTweets.value.length);
const impressionsCount = computed(() =>
  allTweets.value.reduce((acc, tweet) => acc + tweet.hashtags.length, 0)
);
const reachCount = computed(() =>
  allTweets.value.reduce((acc, tweet) => acc + tweet.mentions.length, 0)
);
const contributorsCount = computed(() =>
  new Set(allTweets.value.map(tweet => tweet.username)).size
);

// Formatter
const formatCount = num => {
  if (num >= 1e6) return `${(num / 1e6).toFixed(1)}M`;
  if (num >= 1e3) return `${(num / 1e3).toFixed(1)}K`;
  return num.toLocaleString();
};

// Pagination logic
const tweets = allTweets;
const totalItems = computed(() => tweets.value.length);
const totalPages = computed(() => Math.ceil(totalItems.value / tweetsPerPage.value));

const paginatedTweets = computed(() => {
  const start = (currentPage.value - 1) * tweetsPerPage.value;
  return [...tweets.value].reverse().slice(start, start + tweetsPerPage.value);
});

const visiblePages = computed(() => {
  const pages = [];
  const maxVisible = 5;
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2));
  let end = Math.min(totalPages.value, start + maxVisible - 1);

  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1);
  }

  for (let i = start; i <= end; i++) {
    pages.push(i);
  }

  return pages;
});

const startItem = computed(() => (currentPage.value - 1) * tweetsPerPage.value + 1);
const endItem = computed(() => Math.min(currentPage.value * tweetsPerPage.value, totalItems.value));

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};
const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};

// Fetch Data
const fetchTweets = async () => {
  try {
    loading.value = true;
    error.value = null;
    const response = await axios.get("http://localhost:8000/api/tweets/");
    allTweets.value = response.data;
  } catch (err) {
    error.value = `Failed to load tweets: ${err.message}`;
    console.error("Error fetching tweets:", err);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchTweets);



</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap");
.title {
  font-family: "Inter", sans-serif;
  font-optical-sizing: auto;
  font-size: 3rem;
  font-weight: 600;
  font-style: normal;
}
</style>