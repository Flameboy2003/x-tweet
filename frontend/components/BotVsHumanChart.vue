<template>
  <div class="relative mt-[40px] p-6 bg-gradient-to-br from-gray-900 to-[#1a1c1f] border border-gray-800 rounded-2xl shadow-2xl transition-all duration-500 hover:shadow-2xl hover:-translate-y-1 group overflow-hidden">
    <!-- Glow effect -->
    <div class="absolute inset-0 bg-gradient-to-br from-blue-900/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
    <!-- Header with icon -->
    <div class="flex items-center mb-6">
      <div class="p-2 mr-3 rounded-lg bg-blue-900/30 backdrop-blur-sm border border-blue-800/50 shadow-lg">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zM4 19.235v-.11a6.375 6.375 0 0112.75 0v.109A12.318 12.318 0 0110.374 21c-2.331 0-4.512-.645-6.374-1.766z" />
        </svg>
      </div>
      <h2 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 transition-all duration-500 group-hover:bg-gradient-to-r group-hover:from-blue-300 group-hover:to-cyan-200">
        Bot vs Human Ratio
      </h2>
    </div>
    
    <!-- Chart container -->
    <div class="relative h-64">
      <transition name="fade" mode="out-in">
        <Doughnut 
          v-if="chartData" 
          :data="chartData" 
          :options="chartOptions" 
          class="transition-opacity duration-500 ease-in-out"
        />
        <div v-else class="absolute inset-0 flex items-center justify-center">
          <div class="animate-pulse flex flex-col items-center w-full">
            <div class="h-40 w-40 rounded-full bg-gray-800 mb-4"></div>
            <div class="h-4 bg-gray-800 rounded w-3/4"></div>
            <div class="h-4 bg-gray-800 rounded w-1/2 mt-2"></div>
          </div>
        </div>
      </transition>
    </div>
    
    <!-- Footer with stats -->
    <div class="mt-6 flex justify-between items-center">
      <div class="flex space-x-4">
        <div class="flex items-center">
          <span class="w-3 h-3 mr-2 rounded-full bg-green-400"></span>
          <span class="text-sm text-gray-300">Human: {{ humanPercentage }}%</span>
        </div>
        <div class="flex items-center">
          <span class="w-3 h-3 mr-2 rounded-full bg-red-400"></span>
          <span class="text-sm text-gray-300">Bot: {{ botPercentage }}%</span>
        </div>
      </div>
      <!-- <button @click="refreshData" class="px-4 py-2 text-sm font-medium rounded-lg bg-blue-900/40 hover:bg-blue-800/60 border border-blue-800/50 text-blue-300 hover:text-white transition-all duration-300 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Refresh
      </button> -->
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Doughnut } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js'
import axios from 'axios'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

const chartData = ref(null)
const botCount = ref(0)
const humanCount = ref(0)
const loading = ref(true)

const humanPercentage = computed(() => {
  const total = botCount.value + humanCount.value
  return total > 0 ? Math.round((humanCount.value / total) * 100) : 0
})

const botPercentage = computed(() => {
  const total = botCount.value + humanCount.value
  return total > 0 ? Math.round((botCount.value / total) * 100) : 0
})

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  cutout: '70%',
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      backgroundColor: 'rgba(17, 24, 39, 0.9)',
      titleColor: '#E5E7EB',
      bodyColor: '#D1D5DB',
      borderColor: 'rgba(55, 65, 81, 0.5)',
      borderWidth: 1,
      padding: 12,
      usePointStyle: true,
      callbacks: {
        label: function(context) {
          const label = context.label || ''
          const value = context.raw || 0
          const total = context.dataset.data.reduce((a, b) => a + b, 0)
          const percentage = Math.round((value / total) * 100)
          return `${label}: ${value} (${percentage}%)`
        }
      }
    }
  },
  animation: {
    duration: 1500,
    easing: 'easeInOutQuart',
    animateScale: true,
    animateRotate: true
  },
  hover: {
    mode: 'nearest',
    intersect: true
  }
}

const fetchData = async () => {
  try {
    loading.value = true
    const res = await axios.get('http://127.0.0.1:8000/api/tweets/')
    const tweets = res.data

    let bot = 0
    let human = 0

    tweets.forEach(tweet => {
      tweet.is_bot ? bot++ : human++
    })

    botCount.value = bot
    humanCount.value = human

    chartData.value = {
      labels: ['Human', 'Bot'],
      datasets: [
        {
          data: [human, bot],
          backgroundColor: [
            'rgba(74, 222, 128, 0.8)',
            'rgba(248, 113, 113, 0.8)'
          ],
          hoverBackgroundColor: [
            'rgba(74, 222, 128, 1)',
            'rgba(248, 113, 113, 1)'
          ],
          borderColor: [
            'rgba(74, 222, 128, 0.2)',
            'rgba(248, 113, 113, 0.2)'
          ],
          hoverOffset: 20,
          borderWidth: 1,
          borderRadius: 10,
          spacing: 4
        },
      ],
    }
  } catch (error) {
    console.error('Error loading tweets:', error)
  } finally {
    loading.value = false
  }
}

const refreshData = () => {
  fetchData()
}

onMounted(() => {
  fetchData()
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Custom chart hover effect */
.doughnut-chart:hover {
  transform: scale(1.02);
  transition: transform 0.3s ease-in-out;
}

/* Custom scrollbar (if needed) */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}

::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
}

::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.2);
}
</style>