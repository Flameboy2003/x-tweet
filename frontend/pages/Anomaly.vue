<template>
  <div
    class="min-h-screen w-full p-6 bg-[#1b1c1e] bg-cover bg-center bg-no-repeat bg-fixed"
  >
    <h1
      class="text-4xl  py-8 font-extrabold mb-8 text-center text-white drop-shadow-lg"
    >
      Anomaly Detection
    </h1>

    <div>
      <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
        <div
          class="relative isolate px-6 text-center rounded-3xl sm:px-12"
        >
          <form @submit.prevent="fetchAnomalies" class="max-w-xl mx-auto">
            <label
              class="mx-auto mt-8 relative bg-white min-w-sm max-w-2xl flex flex-col md:flex-row items-center justify-center border py-2 px-2 rounded-2xl gap-2 shadow-2xl focus-within:border-gray-300"
              for="search-bar"
            >
              <input
                id="search-bar"
                v-model="query"
                placeholder="Search your keyword here"
                name="q"
                class="px-6 py-2 w-full rounded-md flex-1 outline-none bg-white"
                required
              />

              <button
                type="submit"
                class="w-full md:w-auto px-6 py-3 bg-black border-black text-white fill-white active:scale-95 duration-100 border will-change-transform overflow-hidden relative rounded-xl transition-all duration-300 hover:scale-110"
              >
                <div class="flex items-center transition-all opacity-1">
                  <span
                    class="text-sm font-semibold whitespace-nowrap truncate mx-auto"
                  >
                    Search
                  </span>
                </div>
              </button>
            </label>
          </form>
        </div>
      </div>
    </div>

    <div v-if="error" class="mt-6 text-center text-red-600 font-semibold">
      {{ error }}
    </div>

    <div
      v-if="anomalyData"
      class="mt-8 max-w-4xl mx-auto bg-white rounded-2xl shadow-lg p-6"
    >
      <p class="mb-6 text-gray-800 font-medium leading-relaxed">
        Query: <span class="font-semibold">{{ anomalyData.query }}</span
        ><br />
        Anomalies detected:
        <span class="font-semibold">{{ anomalyData.anomaly_count }}</span
        ><br />
        Mean Sentiment Score:
        <span class="font-semibold">{{
          anomalyData.mean_sentiment.toFixed(3)
        }}</span
        ><br />
        Std Dev:
        <span class="font-semibold">{{
          anomalyData.std_sentiment.toFixed(3)
        }}</span
        ><br />
        Thresholds:
        <span class="font-semibold">
          Lower &ge; {{ anomalyData.thresholds.lower.toFixed(3) }} </span
        >,
        <span class="font-semibold">
          Upper &le; {{ anomalyData.thresholds.upper.toFixed(3) }}
        </span>
      </p>

      <ul
        v-if="anomalyData.anomalies.length"
        class="space-y-5 max-h-96 overflow-y-auto scrollbar-thin scrollbar-thumb-gray-300 scrollbar-track-gray-100"
      >
        <li
          v-for="tweet in anomalyData.anomalies"
          :key="tweet.id"
          class="rounded-lg border border-red-400 bg-red-50 p-5 shadow-sm"
        >
          <p class="mb-2 text-gray-900 text-lg font-medium">{{ tweet.text }}</p>
          <p class="text-sm text-gray-700">
            Sentiment Score:
            <span
              :class="{
                'text-green-700':
                  tweet.sentiment_score > anomalyData.mean_sentiment,
                'text-red-700':
                  tweet.sentiment_score < anomalyData.mean_sentiment,
              }"
              class="font-semibold"
            >
              {{ tweet.sentiment_score.toFixed(3) }}
            </span>
            &nbsp;|&nbsp; Created at: {{ formatDate(tweet.created_at) }}
          </p>
        </li>
      </ul>

      <p v-else class="mt-6 text-center italic text-gray-500 select-none">
        No anomalies found for this query.
      </p>

      <div class="my-8 h-96">
        <canvas ref="chartRef"></canvas>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, nextTick } from "vue";
import { Chart, registerables } from "chart.js";

Chart.register(...registerables);

const query = ref("");
const anomalyData = ref(null);
const loading = ref(false);
const error = ref(null);
const chartRef = ref(null);
let chartInstance = null;

function formatDate(isoString) {
  const dt = new Date(isoString);
  return dt.toLocaleString();
}

async function fetchAnomalies() {
  if (!query.value.trim()) {
    error.value = "Please enter a query.";
    return;
  }
  error.value = null;
  anomalyData.value = null;
  loading.value = true;

  try {
    const response = await fetch(
      `http://localhost:8000/api/anomalies/?query=${encodeURIComponent(
        query.value.trim()
      )}`
    );
    if (!response.ok) {
      const errData = await response.json();
      throw new Error(
        errData.error || errData.message || "Failed to fetch anomalies"
      );
    }
    const data = await response.json();
    anomalyData.value = data;
  } catch (err) {
    error.value = err.message;
  } finally {
    loading.value = false;
  }
}

// Watch for anomaly data changes to render chart
watch(anomalyData, async (newVal) => {
  if (newVal && newVal.anomalies.length) {
    await nextTick();
    renderChart(newVal.anomalies);
  } else {
    if (chartInstance) {
      chartInstance.destroy();
      chartInstance = null;
    }
  }
});

function renderChart(anomalies) {
  const ctx = chartRef.value.getContext("2d");
  if (chartInstance) {
    chartInstance.destroy();
  }

  chartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: anomalies.map((a) => formatDate(a.created_at)),
      datasets: [
        {
          label: "Anomaly Sentiment Scores",
          data: anomalies.map((a) => a.sentiment_score),
          backgroundColor: "rgba(239, 68, 68, 0.6)",
          borderColor: "rgba(220, 38, 38, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: false,
        },
      },
      responsive: true,
      maintainAspectRatio: false,
    },
  });
}
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap");
.title {
  font-family: "Inter", sans-serif;
  font-optical-sizing: auto;
  font-size: 3rem;
  font-weight: 600;
  font-style: normal;
}
/* Custom scrollbar for anomaly list */
ul {
  scrollbar-width: thin;
  scrollbar-color: rgb(191 219 254) rgb(255 255 255);
}

ul::-webkit-scrollbar {
  width: 8px;
}

ul::-webkit-scrollbar-track {
  background: #fff;
}

ul::-webkit-scrollbar-thumb {
  background-color: #bfdbfe;
  border-radius: 10px;
  border: 2px solid #fff;
}
</style>
