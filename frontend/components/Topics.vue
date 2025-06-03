<template>
  <div class="premium-container mt-[40px]">
    <div class="premium-card">
      <div class="card-header">
        <h2 class="card-title">
          <span class="text-gradient">Tweet Word Cloud</span>
        </h2>
  
      </div>
      
      <!-- Filters -->
      <div class="filters-container">
        <div class="filter-group">
          <label class="filter-label">Search Query</label>
          <input
            v-model="query"
            placeholder="e.g. 'climate change'"
            class="filter-input"
          />
        </div>
        
        <div class="filter-group">
          <label class="filter-label">Username</label>
          <input
            v-model="user"
            placeholder="@username"
            class="filter-input"
          />
        </div>
        
        <!-- <div class="filter-group">
          <label class="filter-label">Date Range</label>
          <div class="date-range">
            <input type="date" v-model="startDate" class="date-input" />
            <span class="date-separator">to</span>
            <input type="date" v-model="endDate" class="date-input" />
          </div>
        </div> -->
        
        <button
          @click="fetchTopics"
          class="analyze-button"
        >
          <span>Analyze Topics</span>
          <svg xmlns="http://www.w3.org/2000/svg" class="button-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
          </svg>
        </button>
      </div>

      <!-- Loading/Error -->
      <div v-if="loading" class="loading-state">
        <div class="spinner"></div>
        <p>Analyzing tweet data...</p>
      </div>
      <div v-else-if="error" class="error-state">
        <svg xmlns="http://www.w3.org/2000/svg" class="error-icon" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
        <p>{{ error }}</p>
      </div>

      <!-- Topic Results -->
      <div v-else class="topics-container">
        <div v-for="topic in topics" :key="topic.topic_id" class="topic-card">
          <div class="topic-header">
            <h3 class="topic-title">
              <span class="topic-id">Topic {{ topic.topic_id }}</span>
              <span class="topic-name">{{ topic.name }}</span>
            </h3>
            <div class="topic-meta">
              <span class="mentions-count">
                <svg xmlns="http://www.w3.org/2000/svg" class="meta-icon" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z" clip-rule="evenodd" />
                </svg>
                {{ topic.count }} mentions
              </span>
            </div>
          </div>
          <TopicChart :keywords="topic.keywords" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import TopicChart from "./TopicChart.vue";

const topics = ref([]);
const loading = ref(false);
const error = ref("");
const query = ref("");
const user = ref("");
const startDate = ref("");
const endDate = ref("");

const fetchTopics = async () => {
  loading.value = true;
  error.value = "";
  topics.value = [];

  const params = new URLSearchParams();
  if (query.value) params.append("query", query.value);
  if (user.value) params.append("user", user.value);
  if (startDate.value) params.append("start_date", startDate.value);
  if (endDate.value) params.append("end_date", endDate.value);

  try {
    const res = await fetch(
      `http://127.0.0.1:8000/api/topics/?${params.toString()}`
    );
    const data = await res.json();
    if (data.topics) topics.value = data.topics;
    else error.value = "No topics found with these filters.";
  } catch (err) {
    error.value = "Failed to fetch topics. Please try again later.";
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
/* Base Styles */
.premium-container {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --primary: #4361ee;
  --primary-light: #3f37c9;
  --secondary: #3a0ca3;
  --accent: #f72585;
  --dark: #1a1a2e;
  --darker: #16213e;
  --light: #f8f9fa;
  --gray: #6c757d;
  --success: #4cc9f0;
  --border-radius: 12px;
  --shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.2);
  --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.premium-card {
  background: linear-gradient(145deg, #1a1a2e, #16213e);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  border: 1px solid rgba(255, 255, 255, 0.08);
  overflow: hidden;
  padding: 2rem;
  color: white;
  position: relative;
}

.premium-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--accent), var(--primary));
}

/* Header Styles */
.card-header {
  margin-bottom: 2rem;
}

.card-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.75rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
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

.card-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
}

/* Filter Styles */
.filters-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.filter-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-label {
  font-size: 0.8rem;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.7);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.filter-input, .date-input {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 0.75rem 1rem;
  color: white;
  font-family: inherit;
  transition: var(--transition);
}

.filter-input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.filter-input:focus, .date-input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 2px rgba(67, 97, 238, 0.2);
}

.date-range {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.date-separator {
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.8rem;
}

/* Button Styles */
.analyze-button {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, var(--primary), var(--primary-light));
  color: white;
  border: none;
  border-radius: 8px;
  padding: 0.75rem 1.5rem;
  font-weight: 600;
  cursor: pointer;
  transition: var(--transition);
  align-self: flex-end;
  margin-top: auto;
}

.analyze-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px -5px var(--primary);
}

.analyze-button:active {
  transform: translateY(0);
}

.button-icon {
  width: 1rem;
  height: 1rem;
}

/* State Styles */
.loading-state, .error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 1rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
}

.spinner {
  width: 3rem;
  height: 3rem;
  border: 3px solid rgba(255, 255, 255, 0.1);
  border-radius: 50%;
  border-top-color: var(--primary);
  animation: spin 1s ease-in-out infinite;
  margin-bottom: 1rem;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-state {
  color: #ff6b6b;
}

.error-icon {
  width: 2rem;
  height: 2rem;
  margin-bottom: 1rem;
}

/* Topic Styles */
.topics-container {
  display: grid;
  gap: 1.5rem;
}

.topic-card {
  background: rgba(255, 255, 255, 0.03);
  border-radius: var(--border-radius);
  padding: 1.5rem;
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: var(--transition);
}

.topic-card:hover {
  border-color: rgba(67, 97, 238, 0.3);
  transform: translateY(-3px);
}

.topic-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.topic-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.1rem;
}

.topic-id {
  color: var(--primary);
  font-weight: 700;
}

.topic-name {
  font-weight: 600;
}

.topic-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.mentions-count {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.6);
}

.meta-icon {
  width: 0.9rem;
  height: 0.9rem;
  color: var(--success);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .filters-container {
    grid-template-columns: 1fr;
  }
  
  .card-title {
    font-size: 1.5rem;
  }
}
</style>