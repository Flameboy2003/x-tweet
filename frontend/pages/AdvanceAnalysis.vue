<template>
  <div class="p-6 bg-[#1b1c1e] bg-cover bg-center text-center bg-no-repeat bg-fixed">
    <h2 class="title text-4xl font-bold text-white bg-clip-text p-3 mb-2" data-aos="fade-right" data-aos-delay="300">Advanced Analysis</h2>
    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-2 gap-6">
      <TimeChart />
      <WordCloud />
    </div>
    <div class="grid grid-cols-1 gap-6">
      <Influencer />
    </div>
    <div class="grid grid-cols-1 gap-6">
      <Topics />
    </div>
    <div class="box grid grid-cols-1 md:grid-cols-2 xl:grid-cols-2 gap-6">
      <HashtagBar />
      <BotVsHumanChart />
    </div>
    
    <!-- Draggable Download Button -->
    <div 
      ref="draggableButton"
      class="fixed cursor-move z-50"
      :style="buttonStyle"
      @mousedown="startDrag"
      @touchstart="startDrag"
    >
      <Download 
        class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105"
      />
    </div>
  </div>
</template>

<script>
import TimeChart from "/components/TimeChart.vue";
import Influencer from "/components/influencer.vue";
import WordCloud from "/components/WordCloud.vue";
import HashtagBar from "/components/HashtagBar.vue";
import ComparativeChart from "/components/ComparativeChart.vue";
import BotVsHumanChart from '/components/BotVsHumanChart.vue'
import Topics from "~/components/Topics.vue";
import Download from "~/components/Download.vue";
import AOS from "aos";
import "aos/dist/aos.css";
import { ref, onMounted } from 'vue';

export default {
  components: {
    TimeChart,
    Influencer,
    WordCloud,
    HashtagBar,
    ComparativeChart,
    BotVsHumanChart,
    Topics,
    Download,
  },
  setup() {
    const draggableButton = ref(null);
    const isDragging = ref(false);
    const startX = ref(0);
    const startY = ref(0);
    const startLeft = ref(0);
    const startTop = ref(0);
    const buttonStyle = ref({
      left: '20px',
      bottom: '20px',
      transform: 'translate(0, 0)'
    });

    const startDrag = (e) => {
      isDragging.value = true;
      
      // Get initial position
      if (e.type === 'mousedown') {
        startX.value = e.clientX;
        startY.value = e.clientY;
      } else {
        startX.value = e.touches[0].clientX;
        startY.value = e.touches[0].clientY;
      }
      
      // Get current button position
      const style = window.getComputedStyle(draggableButton.value);
      startLeft.value = parseInt(style.left, 10) || 0;
      startTop.value = parseInt(style.top, 10) || 0;
      
      // Add event listeners
      document.addEventListener('mousemove', drag);
      document.addEventListener('touchmove', drag);
      document.addEventListener('mouseup', stopDrag);
      document.addEventListener('touchend', stopDrag);
    };

    const drag = (e) => {
      if (!isDragging.value) return;
      
      let clientX, clientY;
      if (e.type === 'mousemove') {
        clientX = e.clientX;
        clientY = e.clientY;
      } else {
        clientX = e.touches[0].clientX;
        clientY = e.touches[0].clientY;
      }
      
      // Calculate new position
      const dx = clientX - startX.value;
      const dy = clientY - startY.value;
      
      buttonStyle.value = {
        left: `${startLeft.value + dx}px`,
        top: `${startTop.value + dy}px`,
        transform: 'none'
      };
    };

    const stopDrag = () => {
      isDragging.value = false;
      
      // Remove event listeners
      document.removeEventListener('mousemove', drag);
      document.removeEventListener('touchmove', drag);
      document.removeEventListener('mouseup', stopDrag);
      document.removeEventListener('touchend', stopDrag);
    };

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

    return {
      draggableButton,
      buttonStyle,
      startDrag,
    };
  }
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

/* Optional: Add some transition for smoother movement */
.fixed {
  transition: transform 0.1s ease, left 0.1s ease, top 0.1s ease;
}
</style>