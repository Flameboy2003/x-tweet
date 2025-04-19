<template>





  <div class="bg-[url(/images/search_bg.jpg)] bg-center bg-no-repeat bg-cover  ">
    <div class="mx-auto max-w-7xl sm:px-6 lg:px-8 ">
      <div class="relative isolate overflow-hidden  px-6 py-20 text-center bg-transparent  sm:px-16 sm:shadow-sm ">
        <p class="mx-auto max-w-2xl text-3xl font-bold  tracking-tight text-white sm:text-4xl">
          Fetch X (Twitter) historical data of any hashtag, keywords, or @mentions
        </p>

        <form @submit.prevent="handleSearch">
          <label
            class="mx-auto mt-8 relative bg-white min-w-sm max-w-2xl flex flex-col md:flex-row items-center justify-center border py-2 px-2 rounded-2xl gap-2 shadow-2xl focus-within:border-gray-300"
            for="search-bar">

            <input id="search-bar" v-model="searchQuery" placeholder="Search your keyword here" name="q"
              class="px-6 py-2 w-full rounded-md flex-1 outline-none bg-white" required />

            <button type="submit"
              class="w-full md:w-auto px-6 py-3 bg-black border-black text-white fill-white active:scale-95 duration-100 border will-change-transform overflow-hidden relative rounded-xl transition-all duration-300 hover:scale-110">
              <div class="flex items-center transition-all opacity-1">
                <span class="text-sm font-semibold whitespace-nowrap truncate mx-auto">
                  Search
                </span>
              </div>
            </button>
          </label>
        </form>

        <svg viewBox="0 0 1024 1024"
          class="absolute left-1/2 top-1/2 -z-10 h-[64rem] w-[64rem] -translate-x-1/2 [mask-image:radial-gradient(closest-side,white,transparent)]"
          aria-hidden="true">
          <circle cx="512" cy="512" r="512" fill="url(#827591b1-ce8c-4110-b064-7cb85a0b1217)" fill-opacity="0.7" />
          <defs>
            <radialGradient id="827591b1-ce8c-4110-b064-7cb85a0b1217">
              <stop stop-color="#3b82f6" />
              <stop offset="1" stop-color="#1d4ed8" />
            </radialGradient>
          </defs>
        </svg>
      </div>
    </div>
  </div>





  <div class="mx-auto max-w-7xl sm:px-6 lg:px-8  ">
    <section class="py-16 px-4 bg-white text-center">
      <h2 class="text-3xl md:text-4xl font-bold mb-12">
        Intelligent AI-powered X (Twitter) Hashtag Analytics Tool </h2>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-10 max-w-6xl mx-auto">
        <!-- Analyze Hashtags -->
        <div>
          <h3 class="text-xl font-semibold mb-2">Explore X (Twitter) Hashtags</h3>
          <p class="text-gray-600">
            Access historical data for any hashtag, keyword, or @mention on X (Twitter) and view insightful results
            through our interactive dashboard.
          </p>
        </div>

        <!-- Center Icon -->
        <div class="flex items-center justify-center">

        </div>

        <!-- Find Key Influencers -->
        <div>
          <h3 class="text-xl font-semibold mb-2">Influencer Impact Analyzer</h3>
          <p class="text-gray-600">
            Detect and rank the most influential accounts driving hashtag momentum using AI-based scoring algorithms.
          </p>
        </div>

        <!-- Measure and Analyse -->
        <div>
          <h3 class="text-xl font-semibold mb-2">Historical Tweet Data Tracker</h3>
          <p class="text-gray-600">
            Access and visualize tweet history from 2006 onward for any keyword or hashtag. Great for long-term trend
            analysis. </p>
        </div>

        <!-- Center Icon -->
        <div class="flex items-center justify-center">

        </div>

        <!-- Historical Hashtag Data -->
        <div>
          <h3 class="text-xl font-semibold mb-2">Competitor Hashtag Intelligence</h3>
          <p class="text-gray-600">
            Monitor and compare your competitors’ social media campaigns by tracking their most used and effective
            hashtags. </p>
        </div>

        <!-- Center Icon -->
        <div class="flex items-center justify-center">

        </div>

        <!-- Competition Hashtag Analytics -->
        <div>
          <h3 class="text-xl font-semibold mb-2">Campaign Reach & Sentiment Metrics</h3>
          <p class="text-gray-600">
            Measure the total reach, impressions, and sentiment (positive/negative/neutral) of your hashtag campaigns
            using AI-powered sentiment analysis and graph tools. </p>
        </div>
      </div>
    </section>


  </div>





  <div class="relative text-white text-center py-14 px-6 overflow-hidden bg-[url(/images/anime_bg.jpg)]  bg-center bg-no-repeat bg-cover  ">

    <!-- Main content -->
    <div class="relative z-10 max-w-4xl mx-auto">
      <h2 class="text-4xl md:text-5xl font-light">
        On average, around <span class="font-medium text-white">6000+Tweets</span> are sent per second on Twitter (X). 
      </h2>
    </div>
  </div>




  <div class="mx-auto max-w-7xl sm:px-6 lg:px-8  ">
    <div class="bg-white py-16 px-4 sm:px-6 lg:px-30">


      <!-- Main heading -->
      <div class="text-center mb-12">
        <h2 class="text-3xl md:text-5xl font-light text-gray-900">
          TrackMyHashtag Features To Automate And Declutter Your Timeline
        </h2>
      </div>

      <!-- 1st one content section -->
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 items-center  mb-20">

        <!-- Left: Image -->
        <div class="flex justify-center">
          <img src="/images/social.png" alt="Analytics Features Preview"
            class="rounded-lg shadow-md max-w-full h-auto" />
        </div>

        <!-- Right: Text content -->
        <div>
          <h3 class="text-2xl font-semibold text-gray-900 mb-4">
            Smarter Hashtag Analytics to Streamline Your Social Media Strategy </h3>
          <p class="text-gray-700 mb-4">
            Our advanced hashtag analytics tool helps you track key metrics like reach, impressions, and engagement
            across your X (Twitter) campaigns.
            <a href="#" class="text-blue-600 underline">X (Twitter) analytics</a>.
          </p>
          <p class="text-gray-700 mb-4">
            The platform delivers detailed, easy-to-digest analytics designed to cut through the clutter. </p>
          <ul class="list-disc pl-5 text-gray-700 space-y-2">
            <li>Monitor reach, engagement, and impressions for any hashtag, keyword, or @mention</li>
            <li>Identify top-performing content: most retweeted, most liked, top URLs, media-rich posts, and trending
              related hashtags</li>
          </ul>
        </div>
      </div>

      <!-- 2nd one content section -->
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 items-center  mb-20">

        <!-- left Text content -->
        <div>
          <h3 class="text-2xl font-semibold text-gray-900 mb-4">
            Identify and Rank Key Influencers in Any X (Twitter) Campaign</h3>
          <p class="text-gray-700 mb-4">
            Influencers on X (Twitter) are users who, due to their authority, large following, expertise, or social position, significantly boost the visibility and reach of a marketing campaign.
          </p>
          <p class="text-gray-700 mb-4">
            Our hashtag analysis tool helps you discover the most influential users participating in any X (Twitter) campaign. It allows you to analyze their impact, measure their contributions, and optimize your future marketing strategies accordingly. </p>
            <p class="text-gray-700 mb-4">
              Easily find and rank top influencers, users, and contributors from raw Twitter data. Access detailed reports on their impressions, reach, and tweets, and sort them by engagement, impact, follower count, and other valuable metrics.

</p>
          
        </div>
        <!-- Left: Image -->
        <div class="flex justify-center">
          <img src="/images/influencer.png" alt="Analytics Features Preview"
            class="rounded-lg shadow-md max-w-full h-auto" />
        </div>
      </div>

      <!-- 3rd one one content section -->
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 items-center  mb-20">

        <!-- Left: Image -->
        <div class="flex justify-center">
          <img src="/images/history.png" alt="Analytics Features Preview"
            class="rounded-lg shadow-md max-w-full h-auto" />
        </div>

        <!-- Right: Text content -->
        <div>
          <h3 class="text-2xl font-semibold text-gray-900 mb-4">
            Access Historical Hashtag Data from X (Twitter)
          </h3>
          <p class="text-gray-700 mb-4">
            Retrieve tweet IDs from any time period based on hashtags, keywords, or @mentions with our Historical Data Tool.
          </p>
          <p class="text-gray-700 mb-4">
            This tool enables you to analyze the full history of any X (Twitter) topic, giving you a comprehensive view of a campaign’s past performance. </p>
          <ul class="list-disc pl-5 text-gray-700 space-y-2">
            <li>Easily export historical X (Twitter) datasets from previous years related to specific hashtags, keywords, or user mentions.</li>
            <li>Data is available for download in both CSV and JSON formats</li>
          </ul>
        </div>
      </div>

      <!-- 4th one content section -->
      <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-10 items-center  mb-20">

        <!-- left Text content -->
        <div>
          <h3 class="text-2xl font-semibold text-gray-900 mb-4">
            Analyze Competitor Hashtags with Our Tracking Tool</h3>
          <p class="text-gray-700 mb-4">
            Monitor your competitors' social media presence by tracking their hashtags, keywords, and @mentions using our hashtag analytics tool. This helps you refine your own strategy based on real insights.
          </p>
          <p class="text-gray-700 mb-4">
            Gain visibility into your competitors’ activities, including their tweets, top influencers, contributors, and related hashtags. </p>
          <ul class="list-disc pl-5 text-gray-700 space-y-2">
            <li>Use this data to shape and strengthen your own marketing campaigns.</li>
            <li>Check out the sample report for more insights.</li>
          </ul>
        </div>
        <!-- Left: Image -->
        <div class="flex justify-center">
          <img src="/images/metrics.png" alt="Analytics Features Preview"
            class="rounded-lg shadow-md max-w-full h-auto" />
        </div>
      </div>


    </div>
  </div>





  <footer>
    <div class="relative text-white text-center py-8 px-6 overflow-hidden bg-gray-600 ">
      <div class="relative z-10 max-w-4xl mx-auto text-left">
        <p class="font-semibold">About us</p>
        <ul>Hashtag Analytics offers smart, data-driven solutions to help marketers, brands, and analysts track, monitor, and optimize their social media campaigns using real-time and historical hashtag insights.</ul>
        <p class="font-semibold">Copyrights</p>
        <ul>© 2025 Hashtag Analytics. All rights reserved.</ul>
      </div>
    </div>
  </footer>




</template>



<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const searchQuery = ref('')
const router = useRouter()


const handleSearch = () => {
  if (!searchQuery.value.trim()) return
  router.push({ path: '/LiveFeed', query: { q: searchQuery.value.trim() } })
}

</script>


