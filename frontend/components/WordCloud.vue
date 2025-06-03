<template>
  <div class="premium-wordcloud-container">
    <div class="premium-wordcloud-card">
      <div class="card-header">
        <h2 class="card-title">
          <span class="text-gradient">Tweet Word Cloud</span>
          
        </h2>
        <p class="card-subtitle">Visualization of trending keywords</p>
      </div>

      <div class="wordcloud-wrapper">
       
    <canvas ref="wordCloudCanvas" style="width: 100%; height: 100%;"></canvas>
      </div>

      <!-- <div class="wordcloud-footer">
        <div class="footer-item">
          <svg xmlns="http://www.w3.org/2000/svg" class="footer-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M12.586 4.586a2 2 0 112.828 2.828l-3 3a2 2 0 01-2.828 0 1 1 0 00-1.414 1.414 4 4 0 005.656 0l3-3a4 4 0 00-5.656-5.656l-1.5 1.5a1 1 0 101.414 1.414l1.5-1.5zm-5 5a2 2 0 012.828 0 1 1 0 101.414-1.414 4 4 0 00-5.656 0l-3 3a4 4 0 105.656 5.656l1.5-1.5a1 1 0 10-1.414-1.414l-1.5 1.5a2 2 0 11-2.828-2.828l3-3z" clip-rule="evenodd" />
          </svg>
          <span>Words are sized by frequency</span>
        </div>
        <div class="footer-item">
          <svg xmlns="http://www.w3.org/2000/svg" class="footer-icon" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clip-rule="evenodd" />
          </svg>
          <span>Updated in real-time</span>
        </div>
      </div> -->
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const wordCloudCanvas = ref(null);

onMounted(async () => {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/tweets/');
    const tweets = await res.json();

    // Combine all tweet texts into one string
    const allText = tweets.map(t => t.text).join(' ').toLowerCase();

    // Simple preprocessing: remove punctuation & split words
    const words = allText
      .replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, '')
      .split(/\s+/)
      .filter(w => w.length > 3); // Filter out short words

    // Count word frequencies
    const frequency = {};
    words.forEach(word => {
      frequency[word] = (frequency[word] || 0) + 1;
    });

    // Convert to array for wordcloud2.js format: [word, weight]
    const wordFreqArray = Object.entries(frequency);

    // Draw word cloud on canvas
    import('wordcloud').then(WordCloud => {
      WordCloud.default(wordCloudCanvas.value, {
        list: wordFreqArray,
        gridSize: 8,
        weightFactor: 10,
        fontFamily: 'Segoe UI, sans-serif',
        color: 'random-dark',
        rotateRatio: 0.3,
        backgroundColor: '#fff',
      });
    });
  } catch (error) {
    console.error('Error loading or processing tweets for word cloud:', error);
  }
});
</script>

<style scoped>
.premium-wordcloud-container {
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

.premium-wordcloud-card {
  background: linear-gradient(145deg, var(--darker), var(--dark));
  border-radius: var(--border-radius);
  box-shadow: var(--shadow);
  border: 1px solid rgba(255, 255, 255, 0.08);
  overflow: hidden;
  padding: 1.5rem;
  color: white;
  position: relative;
}

.premium-wordcloud-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--accent), var(--primary));
}

.card-header {
  margin-bottom: 1.5rem;
}

.card-title {
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

.card-subtitle {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.85rem;
}

.wordcloud-wrapper {
  position: relative;
  height: 359px;
  margin: 1rem 0;
  background-color: rgba(255, 255, 255, 0.03);
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  overflow: hidden;
}

.wordcloud-canvas {
  width: 100%;
  height: 100%;
  transition: var(--transition);
}

.wordcloud-footer {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}

.footer-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8rem;
  color: rgba(255, 255, 255, 0.7);
}

.footer-icon {
  width: 1rem;
  height: 1rem;
  color: var(--primary-light);
}

@media (max-width: 768px) {
  .wordcloud-wrapper {
    height: 300px;
  }
  
  .card-title {
    font-size: 1.25rem;
  }
  
  .wordcloud-footer {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>