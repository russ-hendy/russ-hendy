<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav style="border-bottom: 1px solid #ccc; padding-bottom: 1rem; margin-bottom: 1rem; display: flex; justify-content: center; align-items: center;">
    <div class="links">
      <RouterLink to="/" style="font-weight: bold; text-decoration: none; color: inherit;">Home</RouterLink>
    </div>
  </nav>
</template>