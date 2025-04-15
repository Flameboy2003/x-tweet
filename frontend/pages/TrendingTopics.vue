<template>
<<<<<<< HEAD
  <div class="twitter-trends-viewer">
    <h1>📈 Twitter Trending Topics <span class="country">🇮🇳 India</span></h1>

    <!-- Loading State -->
    <div v-if="loading" class="loading-indicator">
      <div class="spinner"></div>
      <p>Loading trends...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-message">
      <p>⚠️ Failed to load trends. Please try again later.</p>
    </div>

    <!-- Main Content -->
    <template v-else>
      <!-- Icon-based Time Navigation -->
      <div class="menu-bar">
        <button
          v-for="(entry, index) in trendData"
          :key="entry._id"
          :class="{ active: activeTab === index }"
          @click="showTrend(index)"
        >
          🕒 {{ formatTime(entry.timestamp) }}
        </button>
      </div>

      <!-- Trend Data -->
      <div class="trend-columns">
        <transition-group name="fade">
          <div
            v-for="(entry, index) in trendData"
            v-show="activeTab === index"
            :key="entry._id"
            class="trend-column"
          >
            <div class="timestamp">📅 {{ formatTime(entry.timestamp) }} UTC</div>
            <ul class="trend-list">
              <li
                v-for="(trend, trendIndex) in entry.trends"
                :key="trendIndex"
                :style="{ 'animation-delay': `${trendIndex * 0.05}s` }"
                @click="openTwitterSearch(trend)"
              >
                <span class="rank">⭐ {{ trendIndex + 1 }}.</span>
                <span class="trend-text">{{ trend }}</span>
                <span class="trend-action">🔍</span>
              </li>
            </ul>
          </div>
        </transition-group>
      </div>
    </template>
  </div>
</template>

<script>
export default {
  name: 'TrendingTopics',
  data() {
    return {
      trendData: [],
      activeTab: 0,
      loading: true,
      error: null,
      apiBaseUrl: 'http://localhost:5001/api/trends'
    }
  },
  async created() {
    await this.fetchTrendData();
  },
  methods: {
    async fetchTrendData() {
      this.loading = true;
      this.error = null;
      
      try {
        const response = await fetch(this.apiBaseUrl);
        
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (!Array.isArray(data)) {
          throw new Error('Invalid data format received');
        }
        
        this.trendData = data.sort((a, b) => 
          new Date(b.timestamp) - new Date(a.timestamp)
        );
        
        // Auto-refresh every 5 minutes
        setTimeout(this.fetchTrendData, 300000);
        
      } catch (err) {
        console.error('Error fetching trends:', err);
        this.error = err.message;
        
        // Retry after 30 seconds if failed
        setTimeout(this.fetchTrendData, 30000);
      } finally {
        this.loading = false;
      }
    },
    showTrend(index) {
      this.activeTab = index;
    },
    formatTime(timestamp) {
      const date = new Date(timestamp);
      return date.toLocaleTimeString([], { 
        hour: '2-digit', 
        minute: '2-digit',
        hour12: false 
      });
    },
    openTwitterSearch(trend) {
      const query = trend.startsWith('#') ? trend : `%23${trend.substring(1)}`;
      window.open(`https://twitter.com/search?q=${encodeURIComponent(query)}`, '_blank');
    }
  }
}
</script>

<style scoped>
.twitter-trends-viewer {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  padding: 20px;
  background: linear-gradient(to right, #f5f7fa, #dce4f3);
  color: #333;
  min-height: 100vh;
}

h1 {
  font-size: 2.4rem;
  font-weight: 800;
  text-align: center;
  margin-bottom: 30px;
  color: #1a1a1a;
}

.country {
  font-size: 1.5rem;
}

/* Menu Bar */
.menu-bar {
  display: flex;
  overflow-x: auto;
  gap: 12px;
  justify-content: center;
  padding-bottom: 20px;
  margin-bottom: 20px;
}

.menu-bar button {
  padding: 10px 18px;
  background: white;
  border: 2px solid #007bff;
  border-radius: 30px;
  font-weight: bold;
  color: #007bff;
  transition: all 0.3s ease;
  cursor: pointer;
  min-width: 150px;
  white-space: nowrap;
}

.menu-bar button.active,
.menu-bar button:hover {
  background: #007bff;
  color: white;
  box-shadow: 0 4px 10px rgba(0, 123, 255, 0.3);
  transform: translateY(-2px);
}

/* Trend Column */
.trend-columns {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.trend-column {
  background: #ffffff;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
  padding: 24px;
  width: 100%;
  max-width: 600px;
  animation: fadeIn 0.6s ease forwards;
  margin-bottom: 30px;
}

.timestamp {
  text-align: center;
  font-size: 1.1rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #444;
  letter-spacing: 0.5px;
}

.trend-list {
  list-style: none;
  padding: 0;
  counter-reset: rank;
}

.trend-list li {
  background: #f1f6ff;
  padding: 14px 18px;
  margin-bottom: 10px;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
  align-items: center;
  animation: slideIn 0.4s ease both;
  cursor: pointer;
  transition: all 0.2s ease-in-out;
}

.trend-list li:hover {
  background: #e0efff;
  transform: scale(1.015);
}

.rank {
  font-weight: bold;
  color: #007bff;
}

.trend-action {
  font-size: 1.2rem;
  color: #007bff;
}

/* Animation */
.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-top: 4px solid #007bff;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

.loading-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
}

.error-message {
  color: #dc3545;
  font-weight: bold;
  text-align: center;
  padding: 20px;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(15px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-10px); }
  to   { opacity: 1; transform: translateX(0); }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* Responsive */
@media (max-width: 600px) {
  .menu-bar {
    flex-direction: column;
    align-items: center;
  }

  .menu-bar button {
    width: 100%;
  }
}
</style>
=======
  
</template>
>>>>>>> 82aebb4da2869ae9b2e14e7a014d53ea59630b75
