<template>
  <div class="rounded-xl shadow-2xl mt-[60px] border border-gray-800 transition-all duration-500 hover:shadow-3xl hover:-translate-y-1 bg-gradient-to-br from-gray-900 to-[#1b1c1e]">
    <div class="p-8">
      <div class="flex justify-between items-center mb-8">
        <div>
          <h1 class="text-4xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-400 mb-2 transition-all duration-500 hover:from-blue-300 hover:to-cyan-300">
            Top Influencers
          </h1>
          <p class="text-gray-400">Discover the most impactful social media voices</p>
        </div>
        <div class="flex items-center space-x-2">
          <span class="h-3 w-3 rounded-full bg-cyan-400 animate-pulse"></span>
          <span class="text-sm text-cyan-400">Live Data</span>
        </div>
      </div>

      <!-- Filter Form -->
      <div class="mb-8 p-6 bg-gray-800/50 backdrop-blur-sm rounded-xl border border-gray-700 shadow-inner">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 items-end">
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-1">Sentiment</label>
            <select
              v-model="sentiment"
              class="w-full border border-gray-700 bg-gray-900/70 text-white p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-200 hover:border-gray-600"
            >
              <option value="">All Sentiments</option>
              <option value="positive" class="bg-green-900/30">Positive</option>
              <option value="neutral" class="bg-yellow-900/30">Neutral</option>
              <option value="negative" class="bg-red-900/30">Negative</option>
            </select>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-1">Min Followers</label>
            <input
              type="number"
              v-model="minFollowers"
              placeholder="e.g. 10000"
              class="w-full border border-gray-700 bg-gray-900/70 text-white p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-200 hover:border-gray-600"
            />
          </div>
          
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-1">Hashtag</label>
            <input
              type="text"
              v-model="hashtag"
              placeholder="#trending"
              class="w-full border border-gray-700 bg-gray-900/70 text-white p-3 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500/50 transition-all duration-200 hover:border-gray-600"
            />
          </div>
          
          <button
            @click="fetchInfluencers"
            class="h-[50px] bg-gradient-to-r from-cyan-600 to-blue-600 text-white font-medium px-6 rounded-lg hover:from-cyan-500 hover:to-blue-500 transition-all duration-300 transform hover:scale-[1.02] active:scale-95 flex items-center justify-center space-x-2 shadow-lg shadow-cyan-500/20"
          >
            <span>Apply Filters</span>
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M3 3a1 1 0 011-1h12a1 1 0 011 1v3a1 1 0 01-.293.707L12 11.414V15a1 1 0 01-.293.707l-2 2A1 1 0 018 17v-5.586L3.293 6.707A1 1 0 013 6V3z" clip-rule="evenodd" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Table -->
      <div class="border border-gray-800 rounded-xl overflow-hidden shadow-2xl">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-800">
            <thead class="bg-gray-800/80 backdrop-blur-sm">
              <tr>
                <th scope="col" class="px-14 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">
                  <!-- <div class="flex items-center">
                    <span>Username</span>
                    <svg xmlns="http://www.w3.org/2000/svg" class="ml-1 h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                  </div> -->
                  USER NAME
                </th>
                <th scope="col" class="px-8 py-4 text-center text-xs font-semibold text-gray-300 uppercase tracking-wider">
                  Followers
                </th>
                <!-- <th scope="col" class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">
                  Likes
                </th> -->
                <th scope="col" class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">
                  Retweets
                </th>
                <th scope="col" class="px-6 py-4 text-left text-xs font-semibold text-gray-300 uppercase tracking-wider">
                  Influence Score
                </th>
              </tr>
            </thead>
            <tbody class="bg-gray-900/50 divide-y divide-gray-800">
              <tr
                v-for="(influencer, index) in influencers"
                :key="influencer.username"
                class="hover:bg-gray-800/60 transition-all duration-150"
                :class="{'bg-gray-900/30': index % 2 === 0}"
              >
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-8 w-8 rounded-full bg-gradient-to-br from-blue-500 to-cyan-400 flex items-center justify-center text-white font-bold">
                      {{ influencer.username.charAt(0).toUpperCase() }}
                    </div>
                    <div class="ml-4">
                      <div class="text-sm font-medium text-white group">
                        <span class="group-hover:text-cyan-400 transition-colors duration-200">@{{ influencer.username }}</span>
                      </div>
                      <div class="text-xs text-gray-400">{{ influencer.name || 'Social influencer' }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-white">{{ influencer.followers_count.toLocaleString() }}</div>
                  <div class="text-xs text-gray-400">{{ calculatePercentage(influencer.followers_count) }}% of top</div>
                </td>
                <!-- <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-white">{{ influencer.total_likes.toLocaleString() }}</div>
                  <div class="text-xs text-gray-400">{{ (influencer.total_likes / influencer.followers_count * 100).toFixed(2) }}% rate</div>
                </td> -->
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-white">{{ influencer.total_retweets.toLocaleString() }}</div>
                  <div class="text-xs text-gray-400">{{ (influencer.total_retweets / influencer.followers_count * 100).toFixed(2) }}% rate</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="w-24 bg-gray-700 rounded-full h-2.5 mr-3">
                      <div 
                        class="h-2.5 rounded-full" 
                        :class="getScoreColor(influencer.influence_score)" 
                        :style="{'width': `${Math.min(100, influencer.influence_score)}%`}"
                      ></div>
                    </div>
                    <span class="text-sm font-bold" :class="getScoreTextColor(influencer.influence_score)">
                      {{ influencer.influence_score.toFixed(1) }}
                    </span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Loading state -->
      <div v-if="loading" class="mt-8 text-center py-12">
        <div class="inline-flex items-center space-x-2 text-cyan-400">
          <svg class="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>Loading influencer data...</span>
        </div>
      </div>

      <!-- Empty state -->
      <div v-if="!loading && influencers.length === 0" class="mt-8 text-center py-12 border-2 border-dashed border-gray-800 rounded-xl">
        <svg xmlns="http://www.w3.org/2000/svg" class="mx-auto h-12 w-12 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="mt-2 text-lg font-medium text-gray-300">No influencers found</h3>
        <p class="mt-1 text-sm text-gray-500">Try adjusting your filters to see results</p>
        <button
          @click="resetFilters"
          class="mt-4 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-cyan-600 hover:bg-cyan-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-cyan-500"
        >
          Reset Filters
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const influencers = ref([]);
const sentiment = ref("");
const minFollowers = ref("");
const hashtag = ref("");
const loading = ref(false);
const maxFollowers = ref(0);

onMounted(() => {
  fetchInfluencers();
});

function calculatePercentage(value) {
  if (maxFollowers.value === 0) return 0;
  return ((value / maxFollowers.value) * 100).toFixed(1);
}

function getScoreColor(score) {
  if (score >= 80) return 'bg-green-500';
  if (score >= 60) return 'bg-cyan-400';
  if (score >= 40) return 'bg-yellow-500';
  return 'bg-red-500';
}

function getScoreTextColor(score) {
  if (score >= 80) return 'text-green-400';
  if (score >= 60) return 'text-cyan-400';
  if (score >= 40) return 'text-yellow-400';
  return 'text-red-400';
}

function resetFilters() {
  sentiment.value = "";
  minFollowers.value = "";
  hashtag.value = "";
  fetchInfluencers();
}

async function fetchInfluencers() {
  loading.value = true;
  const params = new URLSearchParams();
  if (sentiment.value) params.append("sentiment", sentiment.value);
  if (minFollowers.value) params.append("min_followers", minFollowers.value);
  if (hashtag.value) params.append("hashtag", hashtag.value);

  try {
    const response = await axios.get(
      `http://localhost:8000/api/influencer-impact/?${params.toString()}`
    );
    influencers.value = response.data;
    
    // Calculate max followers for percentage calculation
    if (influencers.value.length > 0) {
      maxFollowers.value = Math.max(...influencers.value.map(i => i.followers_count));
    }
  } catch (error) {
    console.error("Error fetching influencers:", error);
    influencers.value = [];
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
/* Custom scrollbar for the table */
::-webkit-scrollbar {
  height: 8px;
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #1a1a1a;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  background: #3b82f6;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
  background: #2563eb;
}

/* Glow effect on hover for table rows */
tr {
  position: relative;
}

/* tr:hover::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
} */

/* Animated gradient border for the main container */
.border-gradient {
  position: relative;
  border: 1px solid transparent;
  background-clip: padding-box;
}

.border-gradient::after {
  content: '';
  position: absolute;
  top: -1px;
  left: -1px;
  right: -1px;
  bottom: -1px;
  background: linear-gradient(135deg, #3b82f6, #10b981, #3b82f6);
  background-size: 200% 200%;
  z-index: -1;
  border-radius: inherit;
  opacity: 0.7;
  animation: gradientBorder 3s ease infinite;
}

@keyframes gradientBorder {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

/* Pulse animation for the live data indicator */
@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}

.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Spin animation for loading spinner */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>