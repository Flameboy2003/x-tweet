<template>
  <div class="p-6 bg-gray-50 min-h-screen">
    <div class="p-4">
      <h1 class="text-2xl font-bold mb-4">🔥 Trending Topics</h1>

      <div class="flex items-center gap-2 mb-4">
        <input v-model="searchQuery" @input="fetchTweets" type="text" placeholder="Search keyword..."
          class="p-2 border rounded w-full" />
        <button @click="fetchTweets" class="bg-blue-500 text-white px-4 py-2 rounded">
          Search
        </button>
      </div>

      <ul>
        <div v-if="loading" class="text-center text-gray-500 my-4">Loading tweets...</div>

        <li v-for="tweet in tweets" :key="tweet.id"
          class="mb-4 border border-gray-200 p-4 rounded-xl shadow-sm hover:shadow-md transition-all">
          <div class="flex justify-between items-center mb-2">
            <div class="font-semibold text-blue-600">@{{ tweet.username }}</div>
            <div class="text-xs text-gray-500">{{ new Date(tweet.created_at).toLocaleString() }}</div>
          </div>
          <p class="text-gray-800 mb-3">{{ tweet.text }}</p>

          <div class="flex gap-6 text-sm text-gray-600">
            <span>❤️ {{ tweet.like_count }}</span>
            <span>🔁 {{ tweet.retweet_count }}</span>
            <span>💬 {{ tweet.reply_count }}</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

const searchQuery = ref('')
const tweets = ref([])
const loading = ref(false) // 🔧 define loading

let intervalId = null

const fetchTweets = async () => {
  try {
    loading.value = true
    const response = await axios.get(`http://127.0.0.1:8000/api/tweets/?q=${searchQuery.value}`)
    tweets.value = response.data
  } catch (error) {
    console.error('Error fetching tweets:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchTweets()
  intervalId = setInterval(fetchTweets, 10000000) // fetch every 10 seconds
})

onUnmounted(() => {
  clearInterval(intervalId)
})
</script>