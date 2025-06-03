<template>
  <div class="relative p-6 bg-gradient-to-br from-gray-900 to-[#1a1c1f] border border-gray-800 rounded-2xl shadow-2xl transition-all duration-500 hover:shadow-2xl hover:-translate-y-1 group overflow-hidden">
    <!-- Glow effect -->
    <div class="absolute inset-0 bg-gradient-to-br from-blue-900/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
    
    <!-- Header with icon -->
    <div class="flex items-center mb-6">
      <div class="p-2 mr-3 rounded-lg bg-blue-900/30 backdrop-blur-sm border border-blue-800/50 shadow-lg">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-blue-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
      </div>
      <h2 class="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-cyan-300 transition-all duration-500 group-hover:bg-gradient-to-r group-hover:from-blue-300 group-hover:to-cyan-200">
        Sentiment Comparison
      </h2>
    </div>
    
    <!-- Chart container with shimmer loading effect -->
    <div class="relative h-64">
      <canvas ref="comparativeChart" class="opacity-0 animate-fade-in-delayed z-10 relative"></canvas>
      <div v-if="loading" class="absolute inset-0 flex items-center justify-center">
        <div class="animate-pulse flex space-x-4 w-full h-full">
          <div class="flex-1 space-y-4">
            <div v-for="i in 3" :key="i" class="h-8 bg-gray-800 rounded" :style="`width: ${Math.random() * 80 + 20}%`"></div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Footer with topic selector -->
    <div class="mt-6 flex justify-between items-center">
      <div class="flex space-x-2">
        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-900/50 text-green-200">
          <span class="w-2 h-2 mr-1 rounded-full bg-green-400"></span>
          Topic 1
        </span>
        <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-red-900/50 text-red-200">
          <span class="w-2 h-2 mr-1 rounded-full bg-red-400"></span>
          Topic 2
        </span>
      </div>
      <button @click="refreshData" class="px-4 py-2 text-sm font-medium rounded-lg bg-blue-900/40 hover:bg-blue-800/60 border border-blue-800/50 text-blue-300 hover:text-white transition-all duration-300 flex items-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
        Refresh Data
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

const comparativeChart = ref(null);
const loading = ref(true);

const processData = (dataSets) => {
  const getSentimentCounts = (tweets) => {
    return tweets.reduce(
      (counts, tweet) => {
        if (tweet.sentiment === 'positive') counts.positive++;
        else if (tweet.sentiment === 'negative') counts.negative++;
        else counts.neutral++;
        return counts;
      },
      { positive: 0, negative: 0, neutral: 0 }
    );
  };

  return {
    topic1: getSentimentCounts(dataSets[0]),
    topic2: getSentimentCounts(dataSets[1])
  };
};

const createChart = (counts) => {
  return new Chart(comparativeChart.value, {
    type: 'bar',
    data: {
      labels: ['Positive', 'Neutral', 'Negative'],
      datasets: [
        {
          label: 'Topic 1',
          data: [counts.topic1.positive, counts.topic1.neutral, counts.topic1.negative],
          backgroundColor: 'rgba(34, 197, 94, 0.8)',
          hoverBackgroundColor: 'rgba(22, 163, 74, 0.9)',
          borderColor: 'rgba(34, 197, 94, 0.2)',
          borderWidth: 1,
          borderRadius: 6,
          barPercentage: 0.8,
          categoryPercentage: 0.7
        },
        {
          label: 'Topic 2',
          data: [counts.topic2.positive, counts.topic2.neutral, counts.topic2.negative],
          backgroundColor: 'rgba(248, 113, 113, 0.8)',
          hoverBackgroundColor: 'rgba(239, 68, 68, 0.9)',
          borderColor: 'rgba(248, 113, 113, 0.2)',
          borderWidth: 1,
          borderRadius: 6,
          barPercentage: 0.8,
          categoryPercentage: 0.7
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        duration: 1200,
        easing: 'easeOutQuart'
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { 
            display: true, 
            text: 'Tweet Count',
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
            color: '#6B7280',
            stepSize: 1
          }
        },
        x: {
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
              return `${context.dataset.label}: ${context.raw} tweets`;
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
    const responses = await Promise.all([
      fetch('http://127.0.0.1:8000/api/tweets/?topic=topic1'),
      fetch('http://127.0.0.1:8000/api/tweets/?topic=topic2'),
    ]);
    const dataSets = await Promise.all(responses.map(res => res.json()));
    const counts = processData(dataSets);
    
    if (comparativeChart.value) {
      Chart.getChart(comparativeChart.value)?.destroy();
      createChart(counts);
      comparativeChart.value.style.opacity = '1';
    }
  } catch (error) {
    console.error('Error loading comparative sentiment data:', error);
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
</style>