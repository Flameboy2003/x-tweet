<template>
  <div class="main-container bg-black">
    <div class="page-content bg-black overflow-visible">
      <!-- Hero Section -->
      <div>
        <div
          class="min-h-screen p-6 bg-[url('/images/bg-img2.avif')] bg-cover bg-center bg-no-repeat bg-fixed"
        >
          <div class="min-h-[80vh] flex items-center justify-start">
            <div
              class="title text-[75px] font-bold text-white ml-8 max-w-4xl leading-tight"
              data-aos="fade-right"
              data-aos-delay="300"
            >
              Real-time Twitter Trend Analysis <br />
              Stay ahead with instant sentiment, anomaly, and influencer
              insights<br />
              from live tweets.
              <div>
                <button
                  @click="navigateTo('/Search')"
                  class="bg-blue-500 text-white px-4 py-2 text-xl rounded hover:bg-blue-600"
                  data-aos="zoom-in"
                  data-aos-delay="600"
                >
                  Get Started
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div
      class="grid grid-cols-1 md:grid-cols-2 bg-[#0a0a0a] p-11 justify-center relative w-full h-[700px] mx-auto"
      data-aos="fade-up"
      data-aos-duration="1000"
    >
      <div
        class="right-container p-10 border border-white/20 bg-[url('/images/cont-bg.avif')] bg-auto flex flex-col items-center justify-center text-center"
      >
        <h2 class="text-xl md:text-4xl font-bold text-white mb-12">
          Let Twitter Trends Guide Smarter Decisions
        </h2>
        <p class="text-gray-400 text-xl max-w-2xl">
          Stay in the loop with what people are really talking about on
          Twitter.<br />
          X-Tweet lets you follow real-time conversations, spot changes in
          sentiment, and find patterns you might otherwise miss. Whether you're
          tracking trends, identifying unusual spikes, or discovering facts,<br />
          it's all right here simplified and in one place.
        </p>
      </div>

      <div
        class="left-container max-w-7xl w-full grid md:grid-cols-2 lg:grid-cols-3 gap-8 border border-white/20 relative z-0"
      >
        <!-- Card 1 -->
        <div
          class="absolute top-[-100px] left-[170px] h-[300px] w-[200px] bg-[#1b1c1e] p-6 rounded-2xl shadow-lg hover:shadow-xl transition"
        >
          <div
            class="w-12 h-12 bg-blue-500/20 rounded-full flex items-center justify-center mr-4"
          >
            <svg
              class="w-6 h-6 text-blue-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"
              ></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-blue-400 mb-2">
            Real-Time Tweet Monitoring
          </h3>
          <p class="text-sm text-gray-400">
            Stay updated with live tweets on any topic or hashtag. See what’s
            trending as it happens.
          </p>
        </div>

        <!-- Card 2 -->
        <div
          class="absolute top-[-50px] right-[140px] h-[300px] w-[200px] bg-[#1b1c1e] p-6 rounded-2xl shadow-lg hover:shadow-xl transition"
        >
          <div
            class="w-12 h-12 bg-purple-500/20 rounded-full flex items-center justify-center mr-4"
          >
            <svg
              class="w-6 h-6 text-purple-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              ></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-blue-400 mb-2">
            Advanced Sentiment Analysis
          </h3>
          <p class="text-sm text-gray-400">
            Understand how people feel about a topic using accurate, AI-powered
            sentiment detection.
          </p>
        </div>

        <!-- Card 3 -->
        <div
          class="absolute bottom-[50px] right-[150px] h-[300px] w-[200px] bg-[#1b1c1e] p-6 rounded-2xl shadow-lg hover:shadow-xl transition"
        >
          <div
            class="w-12 h-12 bg-blue-500/20 rounded-full flex items-center justify-center mr-4"
          >
            <svg
              class="w-6 h-6 text-blue-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
              ></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-blue-400 mb-2">
            Anomaly & Trend Detection
          </h3>
          <p class="text-sm text-gray-400">
            Identify sudden spikes or unusual behavior in tweet volume and
            sentiment spot virality early.
          </p>
        </div>

        <!-- Card 4 -->
        <div
          class="absolute bottom-[100px] left-[160px] h-[300px] w-[200px] bg-[#1b1c1e] p-6 rounded-2xl shadow-lg hover:shadow-xl transition"
        >
          <div
            class="w-12 h-12 bg-purple-500/20 rounded-full flex items-center justify-center mr-4"
          >
            <svg
              class="w-6 h-6 text-purple-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
              ></path>
            </svg>
          </div>
          <h3 class="text-xl font-semibold text-blue-400 mb-2">
            Influencer & Bot Insights
          </h3>
          <p class="text-sm text-gray-400">
            Know who's shaping conversations. Track influencer impact and detect
            automated bot activity.
          </p>
        </div>
      </div>
    </div>

    <div
      class="grid grid-cols-1 md:grid-cols-2 bg-[#0a0a0a] p-11 justify-center relative w-full h-[700px] mx-auto"
      data-aos="fade-up"
      data-aos-duration="1000"
    >
      <div
        class="right-container p-10 border bg-[length:760px_760px] bg-no-repeat border-white/20 justify-center bg-[url('/images/cont-bg3.avif')]"
      ></div>
      <div
        class="left-container p-[100px] border border-white/20 justify-center"
      >
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-12 text-center">
          X-Tweet
        </h2>
        <p class="text-gray-400 text-center text-xl mb-8">
          X-Tweet is a full-stack web application designed to analyze real-time
          Twitter trends and sentiments. It leverages Twitter API v2 to fetch
          tweets based on user queries, processes them with natural language
          tools, and visualizes insights to help users understand public opinion
          and emerging trends
        </p>
      </div>
    </div>

    <!-- banner line-->
    <div
      class="relative text-white text-center py-14 p-10 overflow-hidden bg-[url(/images/cont-bg1.avif)] bg-center bg-no-repeat bg-cover"
    >
      <!-- Main content -->
      <div class="relative z-10 max-w-4xl mx-auto">
        <h2 class="text-4xl md:text-5xl font-light"></h2>
      </div>
    </div>

    <div
      class="bg-[#0a0a0a] py-20 px-4 sm:px-6 lg:px-8 relative overflow-hidden"
    >
      <!-- Animated background elements -->
      <div
        class="absolute -top-20 -right-20 w-64 h-64 bg-blue-500 rounded-full filter blur-[100px] opacity-10"
      ></div>
      <div
        class="absolute -bottom-20 -left-20 w-64 h-64 bg-cyan-500 rounded-full filter blur-[100px] opacity-10"
      ></div>

      <div class="max-w-7xl mx-auto relative z-10">
        <div class="text-center mb-16" data-aos="fade-up">
          <h2
            class="text-3xl md:text-4xl lg:text-5xl font-bold text-white mb-4"
          >
            Key
            <span
              class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300"
              >Metrics</span
            >
          </h2>
          <p class="text-lg text-gray-400 max-w-3xl mx-auto">
            Essential Twitter analytics to power your social media strategy
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
          <!-- Metric 1 -->
          <div
            class="metric-card bg-[#1b1c1e] p-6 rounded-xl border border-white/10 hover:border-blue-500/30 transition-all duration-300 hover:-translate-y-2"
            data-aos="fade-up"
            data-aos-delay="100"
          >
            <div
              class="w-12 h-12 rounded-full bg-blue-500/10 flex items-center justify-center mb-4"
            >
              <svg
                class="w-6 h-6 text-blue-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Trend Volume</h3>
            <p class="text-gray-400 text-sm mb-4">
              Track mentions over time to identify growing conversations
            </p>
            <!-- <div class="text-2xl font-bold text-blue-400">12.8K</div> -->
            <!-- <div class="text-xs text-green-400 mt-1 flex items-center">
              <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M12 7a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V8.414l-4.293 4.293a1 1 0 01-1.414 0L8 10.414l-4.293 4.293a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0L11 10.586 14.586 7H12z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              +24% this week
            </div> -->
          </div>

          <!-- Metric 2 -->
          <div
            class="metric-card bg-[#1b1c1e] p-6 rounded-xl border border-white/10 hover:border-cyan-500/30 transition-all duration-300 hover:-translate-y-2"
            data-aos="fade-up"
            data-aos-delay="200"
          >
            <div
              class="w-12 h-12 rounded-full bg-cyan-500/10 flex items-center justify-center mb-4"
            >
              <svg
                class="w-6 h-6 text-cyan-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Sentiment</h3>
            <p class="text-gray-400 text-sm mb-4">
              Overall positivity/negativity of conversations
            </p>
            <!-- <div class="text-2xl font-bold text-cyan-400">78%</div>
            <div class="text-xs text-green-400 mt-1 flex items-center">
              <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M12 7a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V8.414l-4.293 4.293a1 1 0 01-1.414 0L8 10.414l-4.293 4.293a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0L11 10.586 14.586 7H12z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              +12% change
            </div> -->
          </div>

          <!-- Metric 3 -->
          <div
            class="metric-card bg-[#1b1c1e] p-6 rounded-xl border border-white/10 hover:border-purple-500/30 transition-all duration-300 hover:-translate-y-2"
            data-aos="fade-up"
            data-aos-delay="300"
          >
            <div
              class="w-12 h-12 rounded-full bg-purple-500/10 flex items-center justify-center mb-4"
            >
              <svg
                class="w-6 h-6 text-purple-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">
              Filtered Top Influencers
            </h3>
            <p class="text-gray-400 text-sm mb-4">
              Accounts driving the most engagement
            </p>
            <!-- <div class="text-2xl font-bold text-purple-400">428</div>
            <div class="text-xs text-gray-400 mt-1">Identified this week</div> -->
          </div>

          <!-- Metric 4 -->
          <div
            class="metric-card bg-[#1b1c1e] p-6 rounded-xl border border-white/10 hover:border-pink-500/30 transition-all duration-300 hover:-translate-y-2"
            data-aos="fade-up"
            data-aos-delay="400"
          >
            <div
              class="w-12 h-12 rounded-full bg-pink-500/10 flex items-center justify-center mb-4"
            >
              <svg
                class="w-6 h-6 text-blue-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">CSV Download</h3>
            <p class="text-gray-400 text-sm mb-4">
              Users should download their research data
            </p>
            <!-- <div class="text-2xl font-bold text-pink-400">5.2M</div>
            <div class="text-xs text-green-400 mt-1 flex items-center">
              <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M12 7a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V8.414l-4.293 4.293a1 1 0 01-1.414 0L8 10.414l-4.293 4.293a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0L11 10.586 14.586 7H12z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              +1.1M from yesterday
            </div> -->
          </div>

          <!-- Metric 5 -->
          <div
            class="metric-card bg-[#1b1c1e] p-6 rounded-xl border border-white/10 hover:border-yellow-500/30 transition-all duration-300 hover:-translate-y-2"
            data-aos="fade-up"
            data-aos-delay="500"
          >
            <div
              class="w-12 h-12 rounded-full bg-yellow-500/10 flex items-center justify-center mb-4"
            >
              <svg
                class="w-6 h-6 text-yellow-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                ></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold text-white mb-2">Response Time</h3>
            <p class="text-gray-400 text-sm mb-4">
              Average time to detect new trends
            </p>
            <!-- <div class="text-2xl font-bold text-yellow-400">47s</div>
            <div class="text-xs text-green-400 mt-1 flex items-center">
              <svg class="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fill-rule="evenodd"
                  d="M12 7a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0V8.414l-4.293 4.293a1 1 0 01-1.414 0L8 10.414l-4.293 4.293a1 1 0 01-1.414-1.414l5-5a1 1 0 011.414 0L11 10.586 14.586 7H12z"
                  clip-rule="evenodd"
                ></path>
              </svg>
              Faster than 92% of competitors
            </div> -->
          </div>
        </div>
      </div>
    </div>

    <div
      class="grid grid-cols-1 md:grid-cols-2 bg-[#0a0a0a] justify-center relative w-full h-[500px] mx-auto"
    >
      <div
        class="left-container p-[100px] border border-white/20 justify-center"
      >
        <h2 class="text-3xl md:text-4xl font-bold text-white mb-12 text-center">
          Our Services
        </h2>
        <p class="text-gray-400 text-center text-xl mb-8">
          At X-Tweet, we offer real-time tweet tracking, sentiment analysis,
          anomaly detection, and influencer insights—all in one place. Our
          platform helps you monitor conversations as they happen, understand
          public sentiment, detect unusual trends, and analyze key voices and
          bot activity, empowering smarter social media decisions.
        </p>
      </div>
      <div
        class="right-container p-10 border border-white/20 bg-[length:760px_760px] justify-center bg-[url('/images/cont-bg2.avif')]"
      ></div>
    </div>
  </div>
  <!-- footer -->
  <footer>
    <div
      class="relative text-white text-center py-8 px-6 overflow-hidden bg-black"
    >
      <ul>
        © 2025 X-Tweet. All rights reserved.
      </ul>
    </div>
  </footer>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { navigateTo } from "#app";
import { useRouter } from "#app"; // Use Nuxt's built-in composable
import AOS from "aos";
import "aos/dist/aos.css";

const message = ref("Hello, X-Tweet!");
const router = useRouter(); // Use Nuxt's router

onMounted(() => {
  AOS.init({
    offset: 120,
    delay: 0,
    duration: 400,
    easing: "ease",
    once: false,
    mirror: false,
    anchorPlacement: "top-bottom",
  });
});
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap");
.title {
  font-family: "Inter", sans-serif;
  font-optical-sizing: auto;
  font-size: 3rem;
  font-weight: 600;
  font-style: normal;
}


/* Hide scrollbar for Chrome, Safari and Opera */
::-webkit-scrollbar {
  display: none;
}

/* Optional: Add smooth scrolling to anchor links */
html {
  scroll-behavior: smooth;
}

/* Custom animation delays if needed */
[data-aos-delay="100"] {
  transition-delay: 100ms;
}

[data-aos-delay="200"] {
  transition-delay: 200ms;
}

[data-aos-delay="300"] {
  transition-delay: 300ms;
}
</style>
