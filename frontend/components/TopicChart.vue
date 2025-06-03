<template>
  <Bar
    :data="chartData"
    :options="options"
    class="w-full max-w-xl"
  />
</template>

<script setup>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps({
  keywords: {
    type: Array,
    required: true
  }
})

const chartData = {
  labels: props.keywords.map(k => k.text),
  datasets: [
    {
      label: 'Keyword Weights',
      backgroundColor: '#3b82f6',
      data: props.keywords.map(k => k.weight * 100)
    }
  ]
}

const options = {
  responsive: true,
  plugins: {
    legend: { display: false },
    tooltip: { enabled: true }
  },
  scales: {
    x: { title: { display: true, text: 'Keywords' }},
    y: { title: { display: true, text: 'Weight (%)' }}
  }
}
</script>
