<template>
  <div class="relative mt-[40px] p-6 bg-gradient-to-br from-gray-900 to-[#1a1c1f] border border-gray-800 rounded-2xl shadow-2xl transition-all duration-500 hover:shadow-2xl hover:-translate-y-1 group overflow-hidden">
    <!-- Glow effect -->
    <div class="absolute inset-0 bg-gradient-to-br from-blue-900/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
    <!-- Header with icon -->
    <div class="flex items-center mb-6">
      <div class="p-2 mr-3 rounded-lg bg-blue-900/30 backdrop-blur-sm border border-blue-800/50 shadow-lg">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 20l4-16m2 16l4-16M6 9h14M4 15h14" />
        </svg>
      </div>
      <h2 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 transition-all duration-500 group-hover:bg-gradient-to-r group-hover:from-blue-300 group-hover:to-cyan-200">
        Trending Hashtags
      </h2>
    </div>
    
    <!-- Chart container with shimmer loading effect -->
    <div class="relative h-64">
      <canvas ref="hashtagChart" class="opacity-0 animate-fade-in-delayed z-10 relative"></canvas>
      <div v-if="loading" class="absolute inset-0 flex items-center justify-center">
        <div class="animate-pulse flex space-x-4 w-full h-full">
          <div class="flex-1 space-y-4">
            <div v-for="i in 5" :key="i" class="h-8 bg-gray-800 rounded" :style="`width: ${Math.random() * 80 + 20}%`"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Footer with refresh button -->
    <!-- <div class="mt-6 flex justify-end">
      <button @click="refreshData" class="px-4 py-2 text-sm font-medium rounded-lg bg-blue-900/40 hover:bg-blue-800/60 border border-blue-800/50 text-blue-300 hover:text-white transition-all duration-300 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Refresh Data
      </button>
    </div> -->
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

const hashtagChart = ref(null);
const loading = ref(true);

const processData = (tweets) => {
  const hashtags = [];
  tweets.forEach(tweet => {
    const tags = tweet.text.match(/#\w+/g);
    if (tags) {
      hashtags.push(...tags.map(tag => tag.toLowerCase()));
    }
  });

  const freq = {};
  hashtags.forEach(tag => {
    freq[tag] = (freq[tag] || 0) + 1;
  });

  return Object.entries(freq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10);
};

const createChart = (sortedHashtags) => {
  const labels = sortedHashtags.map(item => item[0]);
  const data = sortedHashtags.map(item => item[1]);
  
  // Gradient for bars
  const ctx = hashtagChart.value.getContext('2d');
  const gradient = ctx.createLinearGradient(0, 0, 0, hashtagChart.value.height);
  gradient.addColorStop(0, 'rgba(59, 130, 246, 0.8)');
  gradient.addColorStop(1, 'rgba(34, 211, 238, 0.8)');

  return new Chart(hashtagChart.value, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'Mentions',
        data,
        backgroundColor: gradient,
        borderColor: 'rgba(96, 165, 250, 0.5)',
        borderWidth: 1,
        borderRadius: 6,
        hoverBackgroundColor: 'rgba(34, 211, 238, 0.8)',
      }],
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1200,
        easing: 'easeOutQuart'
      },
      scales: {
        x: {
          beginAtZero: true,
          title: { 
            display: true, 
            text: 'Mention Count', 
            color: '#9CA3AF',
            font: {
              weight: 'bold'
            }
          },
          grid: { 
            color: 'rgba(255, 255, 255, 0.05)',
            drawBorder: false
          },
          ticks: {
            color: '#6B7280'
          }
        },
        y: {
          grid: { 
            color: 'rgba(255, 255, 255, 0.05)',
            drawBorder: false
          },
          ticks: {
            color: '#D1D5DB',
            font: {
              weight: '500'
            }
          }
        }
      },
      plugins: {
        legend: { 
          display: false
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
              return `${context.raw} mentions`;
            }
          }
        }
      }
    },
  });
};

const fetchData = async () => {
  try {
    loading.value = true;
    const res = await fetch('http://127.0.0.1:8000/api/tweets/');
    const tweets = await res.json();
    const sortedHashtags = processData(tweets);
    
    if (hashtagChart.value) {
      // Destroy previous chart if exists
      Chart.getChart(hashtagChart.value)?.destroy();
      createChart(sortedHashtags);
      hashtagChart.value.style.opacity = '1';
    }
  } catch (error) {
    console.error('Error loading hashtags:', error);
  } finally {
    loading.value = false;
  }
};

const refreshData = () => {
  fetchData();
};

onMounted(() => {
  fetchData();
});
</script>

<style scoped>
@keyframes fade-in {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in-delayed {
  animation: fade-in 0.8s cubic-bezier(0.22, 1, 0.36, 1) forwards;
  animation-delay: 0.4s;
}

/* Custom scrollbar for chart (if needed) */
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