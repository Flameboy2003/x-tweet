<template>
    <div class="max-w-4xl mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold mb-6 text-center">Live Tweets for "{{ route.query.q }}"</h1>
  
      <div v-if="loading" class="flex justify-center items-center h-40">
        <svg class="animate-spin h-8 w-8 text-blue-600" xmlns="http://www.w3.org/2000/svg" fill="none"
             viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10"
                  stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor"
                d="M4 12a8 8 0 018-8v8H4z"></path>
        </svg>
      </div>
  
      <div v-else>
        <div v-if="tweets.length === 0" class="text-center text-gray-500">No tweets found.</div>
        <ul class="space-y-4">
          <li v-for="tweet in tweets" :key="tweet.id" class="border p-4 rounded-lg shadow-sm bg-white">
            <p class="text-gray-800">{{ tweet.text }}</p>
            <p class="text-sm text-gray-500 mt-2">— {{ tweet.username }} | {{ tweet.created_at }}</p>
          </li>
        </ul>
      </div>
    </div>
  </template>
  

<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const tweets = ref([])
const loading = ref(true)

const fetchTweets = async () => {
  try {
    const query = route.query.q
    if (!query) return
    const response = await axios.get(`http://127.0.0.1:8000/api/tweets/?q=${query}`)
    tweets.value = response.data
  } catch (error) {
    console.error(error)
  } finally {
    loading.value = false
  }
}

onMounted(fetchTweets)
</script>
