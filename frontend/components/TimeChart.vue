<template>
  <div class="premium-chart-container">
    <div class="premium-chart-card">
      <div class="chart-header">
        <div class="header-content">
          <h2 class="chart-title">
            <span class="text-gradient">Tweet Volume Analytics</span>
            
          </h2>
          <p class="chart-subtitle">Daily tweet activity visualization</p>
        </div>
        <!-- <div class="chart-actions">
          <button class="action-button">
            <svg xmlns="http://www.w3.org/2000/svg" class="action-icon" viewBox="0 0 20 20" fill="currentColor">
              <path d="M6 10a2 2 0 11-4 0 2 2 0 014 0zM12 10a2 2 0 11-4 0 2 2 0 014 0zM16 12a2 2 0 100-4 2 2 0 000 4z" />
            </svg>
          </button>
        </div> -->
      </div>

      <div v-if="error" class="error-state">
        <svg xmlns="http://www.w3.org/2000/svg" class="error-icon" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        <p>{{ error }}</p>
      </div>

      <div class="chart-wrapper">
        <div class="relative">
          <canvas ref="timeChart" class="premium-chart"></canvas>
        </div>
      </div>

      <!-- <div v-if="debugInfo" class="debug-info">
        <div class="debug-item">
          <span class="debug-label">Data Points:</span>
          <span class="debug-value">{{ debugInfo.datesCount }}</span>
        </div>
        <div class="debug-item">
          <span class="debug-label">Sample Dates:</span>
          <span class="debug-value">{{ debugInfo.sampleDates.join(', ') }}</span>
        </div>
        <div class="debug-item">
          <span class="debug-label">Sample Counts:</span>
          <span class="debug-value">{{ debugInfo.sampleCounts.join(', ') }}</span>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

const timeChart = ref(null);
const error = ref(null);
const debugInfo = ref(null);

onMounted(async () => {
  try {
    // 1. Verify API response
    const response = await fetch('http://127.0.0.1:8000/api/tweets/');
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
    
    const data = await response.json();
    if (!data.length) throw new Error('Empty response from API');

    // 2. Verify data processing
    const dateCounts = {};
    data.forEach(tweet => {
      if (!tweet.created_at) throw new Error('Missing created_at field in tweet');
      const date = tweet.created_at.split('T')[0];
      dateCounts[date] = (dateCounts[date] || 0) + 1;
    });

    const sortedDates = Object.keys(dateCounts).sort();
    const counts = sortedDates.map(date => dateCounts[date]);

    debugInfo.value = {
      datesCount: sortedDates.length,
      sampleDates: sortedDates.slice(0, 3),
      sampleCounts: counts.slice(0, 3)
    };

    // 3. Verify canvas element
    if (!timeChart.value) throw new Error('Canvas element not found');
    
    // 4. Create chart with premium styling
    const ctx = timeChart.value.getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: sortedDates,
        datasets: [{
          label: 'Tweets per Day',
          data: counts,
          borderColor: '#4f46e5',
          backgroundColor: 'rgba(79, 70, 229, 0.1)',
          borderWidth: 2,
          pointBackgroundColor: '#4f46e5',
          pointBorderColor: '#fff',
          pointRadius: 4,
          pointHoverRadius: 6,
          fill: true,
          tension: 0.3,
        }],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
            labels: {
              color: '#e2e8f0',
              font: {
                family: 'Inter',
                size: 12
              },
              padding: 20,
              usePointStyle: true,
              pointStyle: 'circle'
            }
          },
          tooltip: {
            backgroundColor: '#1e293b',
            titleColor: '#f8fafc',
            bodyColor: '#e2e8f0',
            borderColor: '#334155',
            borderWidth: 1,
            padding: 12,
            usePointStyle: true,
            callbacks: {
              label: function(context) {
                return `${context.dataset.label}: ${context.parsed.y}`;
              }
            }
          }
        },
        scales: {
          x: {
            grid: {
              color: 'rgba(255, 255, 255, 0.05)',
              drawBorder: false
            },
            ticks: {
              color: '#94a3b8',
              font: {
                family: 'Inter'
              }
            },
            title: {
              display: true,
              text: 'Date',
              color: '#94a3b8',
              font: {
                family: 'Inter',
                weight: '500',
                size: 12
              }
            }
          },
          y: {
            grid: {
              color: 'rgba(255, 255, 255, 0.05)',
              drawBorder: false
            },
            ticks: {
              color: '#94a3b8',
              font: {
                family: 'Inter'
              },
              padding: 10
            },
            title: {
              display: true,
              text: 'Tweet Count',
              color: '#94a3b8',
              font: {
                family: 'Inter',
                weight: '500',
                size: 12
              }
            },
            beginAtZero: true
          }
        },
        interaction: {
          intersect: false,
          mode: 'index'
        }
      }
    });

  } catch (err) {
    error.value = `Error loading chart data: ${err.message}`;
    console.error('Error:', err);
  }
});
</script>

<style scoped>
.premium-chart-container {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --primary: #4f46e5;
  --primary-light: #6366f1;
  --accent: #ec4899;
  --dark: #1e293b;
  --darker: #0f172a;
  --light: #f8fafc;
  --border-radius: 12px;
  --shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.3);
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.premium-chart-card {
  background: linear-gradient(145deg, var(--darker), var(--dark));
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  border: 1px solid rgba(255, 255, 255, 0.08);
  overflow: hidden;
  padding: 1.5rem;
  color: white;
  position: relative;
}

.premium-chart-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--primary));
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.header-content {
  flex: 1;
}

.chart-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 0.25rem;
}

.text-gradient {
  background: linear-gradient(90deg, var(--primary), var(--accent));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.badge {
  background: var(--accent);
  color: white;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.25rem 0.5rem;
  border-radius: 100px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.chart-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.85rem;
}

.chart-actions {
  display: flex;
  gap: 0.5rem;
}

.action-button {
  background: rgba(255, 255, 255, 0.05);
  border: none;
  border-radius: 6px;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
}

.action-button:hover {
  background: rgba(255, 255, 255, 0.1);
}

.action-icon {
  width: 1rem;
  height: 1rem;
  color: rgba(255, 255, 255, 0.7);
}

.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem 1rem;
  text-align: center;
  color: #f87171;
  background: rgba(239, 68, 68, 0.1);
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.error-icon {
  width: 2rem;
  height: 2rem;
  margin-bottom: 1rem;
}

.chart-wrapper {
  position: relative;
  height: 350px;
  margin-bottom: 1.5rem;
}

.premium-chart {
  width: 100%;
  height: 100%;
}

.debug-info {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  padding: 1rem;
  border: 1px solid rgba(255, 255, 255, 0.05);
  font-size: 0.8rem;
}

.debug-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.debug-item:last-child {
  margin-bottom: 0;
}

.debug-label {
  color: rgba(255, 255, 255, 0.6);
  font-weight: 500;
}

.debug-value {
  color: white;
  font-family: 'Menlo', 'Monaco', monospace;
}

@media (max-width: 768px) {
  .chart-header {
    flex-direction: column;
    gap: 1rem;
  }
  
  .chart-title {
    font-size: 1.25rem;
  }
  
  .chart-wrapper {
    height: 300px;
  }
}
</style>