<template>
  <div class="p-2">
    <button
      @click="downloadCSV"
      class="bg-blue-600 text-white p-3 rounded-full hover:bg-blue-700 focus:outline-none"
      aria-label="Download Tweets as CSV"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
      </svg>
    </button>
  </div>
</template>

<script>
export default {
  methods: {
    downloadCSV() {
      const csvUrl = 'http://127.0.0.1:8000/api/download-csv/';
      const link = document.createElement('a');
      link.href = csvUrl;
      link.setAttribute('download', 'tweets.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
}
</script>

<style scoped>
button {
  transition: all 0.2s ease;
}
button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>