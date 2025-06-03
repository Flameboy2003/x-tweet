<template>
  <div class="min-h-screen bg-[#1b1c1e] py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md mx-auto">
      <!-- Header -->
      <div class="text-center mb-10">
        <h1
          class="text-4xl font-bold text-transparent bg-clip-text p-3 bg-gradient-to-r from-blue-400 to-purple-600 mb-2"
        >
          Trending Tweets
        </h1>
        <p class="text-gray-400 " >Real-time trending topics across the web</p>
      </div>

      <!-- Loading Spinner -->
      <div
        v-if="loading"
        class="flex flex-col items-center justify-center py-12"
      >
        <div class="relative">
          <div
            class="w-16 h-16 border-4 border-purple-500 border-t-transparent rounded-full animate-spin"
          ></div>
          <div class="absolute inset-0 flex items-center justify-center">
            <div
              class="w-8 h-8 bg-gradient-to-r from-purple-500 to-blue-600 rounded-full animate-pulse"
            ></div>
          </div>
        </div>
        <p class="mt-4 text-gray-400">Loading cosmic trends...</p>
      </div>

      <!-- Main Content -->
      <div v-else class="space-y-8">
        <!-- Timestamp Dropdown -->
        <div class="relative ">
          <label class="block text-sm font-medium text-gray-400 mb-2"
            >Select Moment in Time</label
          >
          <div class="relative">
            <select
              v-model="selectedTimestamp"
              @change="fetchTrends"
              class="appearance-none w-full py-3 px-4 pr-10 bg-gray-800 border border-gray-700 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent text-white transition-all duration-300"
            >
              <option disabled value="">Select a timestamp</option>
              <option
                v-for="(ts, idx) in timestamps"
                :key="idx"
                :value="ts"
                class="bg-gray-800 text-white hover:bg-purple-600"
              >
                {{ ts }}
              </option>
            </select>
            <div
              class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-gray-400"
            >
              <svg
                class="h-5 w-5"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 9l-7 7-7-7"
                />
              </svg>
            </div>
          </div>
        </div>

        <!-- No timestamps message -->
        <div v-if="timestamps.length === 0" class="text-center py-12">
          <div class="text-gray-500 mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-12 w-12 mx-auto"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <h3 class="text-lg font-medium text-gray-300">
            No moments captured yet
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            Check back later for trending topics
          </p>
        </div>

        <!-- Trends list -->
        <div v-if="latestBatch" class="space-y-6">
          <div class="flex items-center justify-between text-sm text-gray-400">
            <span>Captured at</span>
            <span class="font-medium text-purple-400">{{
              latestBatch.timestamp
            }}</span>
          </div>

          <div class="space-y-3">
            <div
              v-for="(topic, idx) in paginatedTrends"
              :key="idx"
              class="group relative overflow-hidden bg-gray-800 rounded-xl p-5 shadow-lg hover:shadow-xl transition-all duration-300 hover:bg-gray-750 border-l-4"
              :class="{
                'border-purple-500': idxOnPage(idx) === 0,
                'border-pink-500': idxOnPage(idx) === 1,
                'border-blue-500': idxOnPage(idx) === 2,
                'border-gray-700': idxOnPage(idx) > 2,
              }"
            >
              <div class="flex items-start">
                <div class="flex-shrink-0 pt-0.5">
                  <div
                    class="flex items-center justify-center w-8 h-8 rounded-full text-white font-bold"
                    :class="{
                      'bg-purple-500': idxOnPage(idx) === 0,
                      'bg-pink-500': idxOnPage(idx) === 1,
                      'bg-blue-500': idxOnPage(idx) === 2,
                      'bg-gray-700': idxOnPage(idx) > 2,
                    }"
                  >
                    {{ currentPage * trendsPerPage + idxOnPage(idx) + 1 }}
                  </div>
                </div>
                <div class="ml-4 flex-1">
                  <h3
                    class="text-lg font-medium text-white group-hover:text-purple-300 transition-colors duration-300"
                  >
                    {{ topic }}
                  </h3>
                  <div class="mt-1 flex items-center text-xs text-gray-400">
                    <svg
                      class="mr-1 h-4 w-4"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                      />
                    </svg>
                    <span>Trending now</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Pagination Controls -->
          <div class="flex justify-between items-center mt-4">
            <button
              @click="prevPage"
              :disabled="currentPage === 0"
              class="px-4 py-2 bg-gray-700 text-white rounded disabled:opacity-30 hover:bg-gray-600"
            >
              Previous
            </button>
            <span class="text-gray-400"
              >Page {{ currentPage + 1 }} of {{ totalPages }}</span
            >
            <button
              @click="nextPage"
              :disabled="currentPage >= totalPages - 1"
              class="px-4 py-2 bg-gray-700 text-white rounded disabled:opacity-30 hover:bg-gray-600"
            >
              Next
            </button>
          </div>
        </div>

        <!-- No trends for timestamp -->
        <div v-else-if="timestamps.length > 0" class="text-center py-12">
          <div class="text-gray-500 mb-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-12 w-12 mx-auto"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="1.5"
                d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
          </div>
          <h3 class="text-lg font-medium text-gray-300">
            Select a moment to view trends
          </h3>
          <p class="mt-1 text-sm text-gray-500">
            Choose from the dropdown above
          </p>
        </div>
      </div>
    </div>
  </div>
  
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      timestamps: [],
      selectedTimestamp: null,
      latestBatch: null,
      loading: true,
      currentPage: 0,
      trendsPerPage: 5,
    };
  },
  computed: {
    totalPages() {
      return this.latestBatch
        ? Math.ceil(this.latestBatch.trends.length / this.trendsPerPage)
        : 0;
    },
    paginatedTrends() {
      if (!this.latestBatch) return [];
      const start = this.currentPage * this.trendsPerPage;
      return this.latestBatch.trends.slice(start, start + this.trendsPerPage);
    },
  },
  methods: {
    idxOnPage(idx) {
      return idx;
    },
    async fetchTimestamps() {
      try {
        const res = await axios.get(
          "http://localhost:5000/api/trends_by_hour/timestamps"
        );
        this.timestamps = res.data;
      } catch (err) {
        console.error("Error fetching timestamps:", err);
      } finally {
        this.loading = false;
      }
    },
    async fetchTrends() {
      if (!this.selectedTimestamp) return;
      this.loading = true;
      try {
        const res = await axios.get(
          `http://localhost:5000/api/trends_by_hour/${this.selectedTimestamp}`
        );
        this.latestBatch = res.data;
        this.currentPage = 0;
      } catch (err) {
        console.error("Error fetching trends:", err);
        this.latestBatch = null;
      } finally {
        this.loading = false;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages - 1) {
        this.currentPage++;
      }
    },
    prevPage() {
      if (this.currentPage > 0) {
        this.currentPage--;
      }
    },
  },
  async mounted() {
    await this.fetchTimestamps();
  },
};
</script>

<style scoped>
select::-webkit-scrollbar {
  width: 8px;
}
select::-webkit-scrollbar-track {
  background: #1f2937;
}
select::-webkit-scrollbar-thumb {
  background-color: #6b7280;
  border-radius: 4px;
}
</style>
