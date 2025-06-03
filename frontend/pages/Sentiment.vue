<template>
  <div class="min-h-screen p-6 bg-black bg-cover bg-center bg-no-repeat bg-fixed">
    <div class="max-w-6xl mx-auto">
      <!-- Header -->
      <div class="mb-8 text-center">
        <h1 class="text-4xl font-bold text-transparent bg-clip-text p-3 bg-gradient-to-r from-blue-400 to-purple-600 mb-2">Sentiment Analysis Dashboard</h1>
        <p class="text-lg text-white">Understanding public opinion through tweet analysis</p>
      </div>

      <!-- Summary Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="bg-gray-300 p-6 rounded-2xl shadow-lg transform transition-all hover:scale-105 hover:shadow-xl border-t-4 border-green-500">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-green-500">Positive</p>
              <p class="text-3xl font-bold text-green-600">{{ sentimentCounts.positive }}</p>
            </div>
            <div class="p-3 rounded-full bg-green-100 text-green-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
              </svg>
            </div>
          </div>
          <p class="mt-2 text-sm text-green-600" v-if="sentimentCounts.positive > 0">
            +{{ Math.round((sentimentCounts.positive / tweets.length) * 100) }}% of total
          </p>
        </div>

        <div class="bg-gray-300 p-6 rounded-2xl shadow-lg transform transition-all hover:scale-105 hover:shadow-xl border-t-4 border-gray-400">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Neutral</p>
              <p class="text-3xl font-bold text-gray-700">{{ sentimentCounts.neutral }}</p>
            </div>
            <div class="p-3 rounded-full bg-gray-100 text-gray-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
              </svg>
            </div>
          </div>
          <p class="mt-2 text-sm text-gray-600" v-if="sentimentCounts.neutral > 0">
            {{ Math.round((sentimentCounts.neutral / tweets.length) * 100) }}% of total
          </p>
        </div>

        <div class="bg-gray-300 p-6 rounded-2xl shadow-lg transform transition-all hover:scale-105 hover:shadow-xl border-t-4 border-red-500">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-red-500">Negative</p>
              <p class="text-3xl font-bold text-red-600">{{ sentimentCounts.negative }}</p>
            </div>
            <div class="p-3 rounded-full bg-red-100 text-red-600">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14H5.236a2 2 0 01-1.789-2.894l3.5-7A2 2 0 018.736 3h4.018a2 2 0 01.485.06l3.76.94m-7 10v5a2 2 0 002 2h.096c.5 0 .905-.405.905-.904 0-.715.211-1.413.608-2.008L17 13V4m-7 10h2m5-10h2a2 2 0 012 2v6a2 2 0 01-2 2h-2.5" />
              </svg>
            </div>
          </div>
          <p class="mt-2 text-sm text-red-600" v-if="sentimentCounts.negative > 0">
            {{ Math.round((sentimentCounts.negative / tweets.length) * 100) }}% of total
          </p>
        </div>
      </div>

      <!-- Charts Section -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <!-- Pie Chart -->
        <div class="bg-[#1b1c1e] p-6 rounded-2xl shadow-lg">
          <h2 class="text-xl font-semibold text-blue-600 mb-4">Sentiment Distribution (Pie Chart)</h2>
          <Pie :data="pieChartData" :options="pieChartOptions" class="max-h-80" />
        </div>

        <!-- Histogram Chart -->
        <div class="bg-[#1b1c1e] p-6 rounded-2xl shadow-lg">
          <h2 class="text-xl font-semibold text-blue-600 mb-4">Sentiment Distribution (Histogram)</h2>
          <Bar :data="barChartData" :options="barChartOptions" class="max-h-80" />
        </div>
      </div>

      <!-- Tweets List -->
      <div class="bg-[#1b1c1e] p-6 rounded-2xl shadow-lg mb-8">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-xl font-semibold text-blue-600">Recent Tweets Analysis</h2>
          <div class="relative w-32">
            <select v-model="tweetsPerPage" class="appearance-none w-full bg-white/20 border border-gray-300 text-white py-2 px-4 pr-8 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
              <option value="5">5 per page</option>
              <option value="10">10 per page</option>
              <option value="20">20 per page</option>
            </select>
            <div class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700">
              <svg class="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
                <path d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"/>
              </svg>
            </div>
          </div>
        </div>

        <ul class="space-y-4">
          <li v-for="(tweet, index) in paginatedTweets" :key="index"
              class="p-5 rounded-xl transition-all duration-300 hover:shadow-md border"
              >
            <div class="flex justify-between items-start">
              <p class="text-white flex-1 pr-4">{{ tweet.text }}</p>
              <span class="px-4 py-1 rounded-full text-sm font-semibold shadow-sm whitespace-nowrap"
                    :class="getSentimentClass(tweet.sentiment)">
                {{ tweet.sentiment.charAt(0).toUpperCase() + tweet.sentiment.slice(1) }}
              </span>
            </div>
            <div class="mt-3 flex items-center text-sm text-gray-500">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {{ formatDate(new Date()) }}
            </div>
          </li>
        </ul>

        <!-- Pagination -->
        <div class="mt-6 flex items-center justify-between">
          <div class="text-sm text-white">
            Showing {{ (currentPage - 1) * tweetsPerPage + 1 }} to {{ Math.min(currentPage * tweetsPerPage, tweets.length) }} of {{ tweets.length }} tweets
          </div>
          <div class="flex space-x-2">
            <button @click="prevPage" :disabled="currentPage === 1"
                    class="px-4 py-2 border rounded-lg flex items-center transition"
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
              <button v-for="page in visiblePages" :key="page"
                      @click="currentPage = page"
                      class="w-10 h-10 flex items-center justify-center rounded-lg transition"
                      :class="{
                        'bg-indigo-600 text-white': page === currentPage,
                        'text-white hover:bg-white/20': page !== currentPage
                      }">
                {{ page }}
              </button>
              <span v-if="showEllipsis" class="flex items-end px-1">...</span>
            </div>
            <button @click="nextPage" :disabled="currentPage === totalPages"
                    class="px-4 py-2 border rounded-lg flex items-center transition"
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
  </div>
  
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { Pie, Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, BarElement, CategoryScale, LinearScale)

const tweets = ref([])
const currentPage = ref(1)
const tweetsPerPage = ref(10)

// Get sentiment counts (positive, neutral, negative)
const sentimentCounts = computed(() => {
  const counts = { positive: 0, neutral: 0, negative: 0 }
  tweets.value.forEach(tweet => {
    counts[tweet.sentiment]++
  })
  return counts
})

// Pagination Computations
const totalPages = computed(() => Math.ceil(tweets.value.length / tweetsPerPage.value))
const paginatedTweets = computed(() => {
  const start = (currentPage.value - 1) * tweetsPerPage.value
  return tweets.value.slice(start, start + tweetsPerPage.value)
})

// Improved pagination with visible pages
const visiblePages = computed(() => {
  const pages = []
  const maxVisible = 5
  let start = Math.max(1, currentPage.value - Math.floor(maxVisible / 2))
  let end = Math.min(totalPages.value, start + maxVisible - 1)
  
  if (end - start + 1 < maxVisible) {
    start = Math.max(1, end - maxVisible + 1)
  }
  
  for (let i = start; i <= end; i++) {
    pages.push(i)
  }
  
  return pages
})

const showEllipsis = computed(() => {
  return visiblePages.value[visiblePages.value.length - 1] < totalPages.value
})

// Pie Chart data
const pieChartData = computed(() => {
  const counts = sentimentCounts.value
  const total = counts.positive + counts.neutral + counts.negative || 1

  return {
    labels: [
      `Positive ${(counts.positive / total * 100).toFixed(1)}%`,
      `Neutral ${(counts.neutral / total * 100).toFixed(1)}%`,
      `Negative ${(counts.negative / total * 100).toFixed(1)}%`
    ],
    datasets: [{
      data: [counts.positive, counts.neutral, counts.negative],
      backgroundColor: ['#86efac', '#d4d4d8', '#fca5a5'],
      borderColor: ['#22c55e', '#a1a1aa', '#ef4444'],
      borderWidth: 1
    }]
  }
})

// Pie Chart options
const pieChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { 
      position: 'bottom',
      labels: {
        padding: 20,
        font: {
          size: 14
        }
      }
    },
    tooltip: {
      callbacks: {
        label: function (context) {
          const dataset = context.dataset
          const value = dataset.data[context.dataIndex]
          const total = dataset.data.reduce((a, b) => a + b, 0)
          const percentage = ((value / total) * 100).toFixed(1)
          return `${context.label}: ${value} (${percentage}%)`
        }
      }
    }
  }
}

// Bar Chart (Histogram) data
const barChartData = computed(() => {
  const counts = sentimentCounts.value
  return {
    labels: ['Positive', 'Neutral', 'Negative'],
    datasets: [{
      label: 'Number of Tweets',
      data: [counts.positive, counts.neutral, counts.negative],
      backgroundColor: [
        'rgba(34, 197, 94, 0.7)',
        'rgba(161, 161, 170, 0.7)',
        'rgba(239, 68, 68, 0.7)'
      ],
      borderColor: [
        'rgba(34, 197, 94, 1)',
        'rgba(161, 161, 170, 1)',
        'rgba(239, 68, 68, 1)'
      ],
      borderWidth: 1
    }]
  }
})

// Bar Chart options
const barChartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      ticks: {
        precision: 0
      }
    }
  },
  plugins: {
    legend: {
      display: false
    },
    tooltip: {
      callbacks: {
        label: function(context) {
          const value = context.raw
          const total = context.dataset.data.reduce((a, b) => a + b, 0)
          const percentage = ((value / total) * 100).toFixed(1)
          return `${context.dataset.label}: ${value} (${percentage}%)`
        }
      }
    }
  }
}

// Fetch tweets with sentiment from the backend
onMounted(async () => {
  try {
    const res = await fetch('http://localhost:8000/api/get-tweets-with-sentiment/') 
    const data = await res.json()
    tweets.value = data.map(item => ({
      text: item.text,
      sentiment: item.sentiment || 'neutral',
    }))
  } catch (error) {
    console.error('Error fetching tweets:', error)
  }
})

// Pagination Methods
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

// Helper Method for sentiment badge classes
const getSentimentClass = (sentiment) => {
  return {
    'bg-green-100 text-green-800 border border-green-200': sentiment === 'positive',
    'bg-gray-100 text-gray-800 border border-gray-200': sentiment === 'neutral',
    'bg-red-100 text-red-800 border border-red-200': sentiment === 'negative',
  }
}

// Format date
const formatDate = (date) => {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}
</script>

<style scoped>
/* Smooth transitions */
.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}

/* Custom scrollbar for dropdown */
select::-webkit-scrollbar {
  width: 6px;
}

select::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

select::-webkit-scrollbar-thumb {
  background: #c7d2fe;
  border-radius: 4px;
}

select::-webkit-scrollbar-thumb:hover {
  background: #1b1c1e;
}
</style>