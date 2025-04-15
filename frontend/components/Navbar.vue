<template>
  <nav class="bg-white border-gray-200 dark:bg-gray-900">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <NuxtLink to="/" class="flex items-center space-x-3 rtl:space-x-reverse">
        <img width="48" height="48" src="https://img.icons8.com/pulsar-color/48/twitterx.png" alt="x-tweet logo" />
        <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white ">Tweet</span>
      </NuxtLink>

      <!-- Mobile menu toggle button -->
      <button @click="isMenuOpen = !isMenuOpen" type="button"
        class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
        aria-controls="navbar-default" :aria-expanded="isMenuOpen">
        <span class="sr-only">Open main menu</span>
        <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 17 14">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
            d="M1 1h15M1 7h15M1 13h15" />
        </svg>
      </button>

      <!-- Menu items -->
      <div :class="['w-full md:block md:w-auto', isMenuOpen ? 'block' : 'hidden']" id="navbar-default">
        <ul
          class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">

          <li>
            <NuxtLink to="/"
              class="block py-2 px-3 text-gray-900 hover:bg-gray-100  hover:underline  md:hover:bg-transparent md:p-0 dark:text-white duration-300 hover:scale-110">
              Home
            </NuxtLink>
          </li>
          <li>
            <NuxtLink to="/TrendingTopics"
              class="block py-2 px-3 text-gray-900 hover:bg-gray-100 hover:underline md:hover:bg-transparent md:p-0 dark:text-white duration-300 hover:scale-110">
              Trends
            </NuxtLink>
          </li>
          <li>
            <NuxtLink to="/Sentiment"
              class="block py-2 px-3 text-gray-900 hover:bg-gray-100 hover:underline md:hover:bg-transparent md:p-0 dark:text-white duration-300 hover:scale-110">
              Sentiment
            </NuxtLink>
          </li>
          <li>
            <NuxtLink to="/Compare"
              class="block py-2 px-3 text-gray-900 hover:bg-gray-100 hover:underline md:hover:bg-transparent md:p-0 dark:text-white duration-300 hover:scale-110">
              Compare
            </NuxtLink>
          </li>
          <li>
            <NuxtLink to="/LiveFeed"
              class="block py-2 px-3 text-gray-900 hover:bg-gray-100 hover:underline md:hover:bg-transparent md:p-0 dark:text-white duration-300 hover:scale-110">
              Live Feed
            </NuxtLink>
          </li>

        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
const isMenuOpen = ref(false)
</script>
