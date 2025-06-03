<template>
  <div class="page-content">
    <div
      class="min-h-screen w-full p-6 bg-[url('/images/search_bg.avif')] bg-cover bg-center bg-no-repeat bg-fixed"
    >
      <!-- saerch content-->
      <div class="bg-center bg-no-repeat  bg-cover">
        <div class="mx-auto max-w-7xl sm:px-6 lg:px-8">
          <div
            class="relative isolate overflow-hidden px-6 py-20 text-center bg-transparent sm:px-16 sm:shadow-sm"
          >
            <p class="title text-white">
              Fetch X (Twitter) real-time data of any hashtag, keywords, or
              @mentions
            </p>

            <form @submit.prevent="handleSearch">
              <label
                class="mx-auto mt-8 relative bg-white min-w-sm max-w-2xl flex flex-col md:flex-row items-center justify-center border py-2 px-2 rounded-2xl gap-2 shadow-2xl focus-within:border-gray-300"
                for="search-bar"
              >
                <input
                  id="search-bar"
                  v-model="searchQuery"
                  placeholder="Search your keyword here"
                  name="q"
                  class="px-6 py-2 w-full rounded-md flex-1 outline-none bg-white"
                  required
                />

                <button
                  type="submit"
                  class="w-full md:w-auto px-6 py-3 bg-black border-black text-white fill-white active:scale-95 duration-100 border will-change-transform overflow-hidden relative rounded-xl transition-all duration-300 hover:scale-110"
                >
                  <div class="flex items-center transition-all opacity-1">
                    <span
                      class="text-sm font-semibold whitespace-nowrap truncate mx-auto"
                    >
                      Search
                    </span>
                  </div>
                </button>
              </label>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const searchQuery = ref("");
const router = useRouter();

const handleSearch = () => {
  if (!searchQuery.value.trim()) return;
  router.push({ path: "/LiveFeed", query: { q: searchQuery.value.trim() } });
};
</script>

<style>
/* Add these styles */

@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap");
.title {
  font-family: "Inter", sans-serif;
  font-optical-sizing: auto;
  font-size: 3rem;
  font-weight: 600;
  font-style: normal;
}

/* .page-content {
  margin-top: 64px;
  min-height: calc(100vh - 64px);
} */
</style>
