<template>
  <div>
    <Navbar />
    <NuxtPage />
  </div>
</template>

<script setup>
import Navbar from '~/components/Navbar.vue'
useHead({ title: 'X-Tweet' })
</script>
