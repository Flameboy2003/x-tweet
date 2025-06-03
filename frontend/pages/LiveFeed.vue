<template>
  <div class="p-6 bg-gray-50 min-h-screen bg-[url('/images/cont-bg2.avif')]">
    <h1 class="text-2xl text-white font-bold mb-6">Live Feed for "{{ query }}"</h1>

    <div v-if="tweets.length === 0" class="text-white text-lg">
      No tweets found
    </div>
    <div v-else>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-white">
        <div
          v-for="tweet in paginatedTweets"
          :key="tweet.tweet_id"
          class=" shadow-md border border-white bg-[#1b1c1e]  p-4 hover:shadow-lg transition"
        >
          <div
            class="flex items-center gap-2 text-lg font-semibold  mb-1"
          >
            <img
              :src="userIcon"
              alt="User Icon"
              class="h-5 w-5 text-blue-400"
            />
            {{ tweet.username }}
          </div>

          <div class="text-gray-700 mb-2 flex text-white gap-2">
            <img
              :src="commentIcon"
              alt="User Icon"
              class="h-5 w-5 text-blue-400"
            />
            <p>{{ tweet.text }}</p>
          </div>

          <div class="text-sm text-white flex gap-2">
            <img
              :src="clockIcon"
              alt="User Icon"
              class="h-5 w-5 text-blue-400"
            />
            <p>{{ tweet.created_at }}</p>
          </div>

          <div class="flex justify-between text-sm text-white mt-2">
            <div class="flex items-center gap-1">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-4 w-4 text-yellow-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 4v16l4-4h12V4H4z"
                />
              </svg>
              <span>{{ tweet.retweet_count }}</span>
            </div>
          </div>

          <p class="mt-2 text-sm text-white">
            <img
              :src="hashIcon"
              alt="User Icon"
              class="h-5 w-5 text-blue-400"
            />
            {{ tweet.hashtags.join(", ") || "None" }}
          </p>
          <p class="text-sm text-white">
            <img
              :src="usersIcon"
              alt="User Icon"
              class="h-5 w-5 text-blue-400"
            />
            <strong>Mentions:</strong> {{ tweet.mentions.join(", ") || "None" }}
          </p>
        </div>
      </div>
    </div>

    <!-- Pagination -->
    <div
      class="mt-6 flex justify-center items-center gap-4 text-gray-700 text-sm"
    >
      <button
        @click="prevPage"
        :disabled="currentPage === 1"
        class="bg-transparent text-gray-700 font-semibold border border-gray-300 rounded-md px-2 py-1"
      >
        <svg class="h-6 w-6 fill-current" viewBox="0 0 20 20">
          <path d="M10 18l-8-8 8-8 1.414 1.414L4.828 10l6.586 6.586L10 18z" />
        </svg>
      </button>

      <span class="font-medium text-base text-gray-800">
        {{ currentPage }} <span class="text-gray-500">/ {{ totalPages }}</span>
      </span>

      <button
        @click="nextPage"
        :disabled="currentPage === totalPages"
        class="bg-transparent text-gray-700 font-semibold border border-gray-300 rounded-md px-2 py-1"
      >
        <svg class="h-6 w-6 fill-current" viewBox="0 0 20 20">
          <path d="M10 2l8 8-8 8-1.414-1.414L15.172 10l-6.586-6.586L10 2z" />
        </svg>
      </button>
    </div>

    <footer class="mt-12 py-6 text-center text-gray-500 text-sm border-t">
      © 2025 X-Tweet. All rights reserved.
    </footer>
  </div>
</template>

<script setup>

import userIcon from "@/assets/user.svg";
import usersIcon from "@/assets/users.svg";
import commentIcon from "@/assets/comment.svg";
import clockIcon from "@/assets/clock.svg";
import hashIcon from "@/assets/hash.svg";

import { ref, computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";

const route = useRoute();
const query = route.query.q || "";
const tweets = ref([]);
const currentPage = ref(1);
const tweetsPerPage = 9;

const paginatedTweets = computed(() => {
  const start = (currentPage.value - 1) * tweetsPerPage;
  return [...tweets.value].reverse().slice(start, start + tweetsPerPage);
});

const totalPages = computed(() =>
  Math.ceil(tweets.value.length / tweetsPerPage)
);

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++;
};

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--;
};



onMounted(async () => {
  if (query) {
    try {
      const response = await axios.get(
        `http://127.0.0.1:8000/api/search_tweets/?q=${encodeURIComponent(
          query
        )}`
      );
      tweets.value = response.data;
    } catch (error) {
      console.error("Error fetching tweets:", error);
    }
  }
});
</script>
