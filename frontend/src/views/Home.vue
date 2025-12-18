<script setup>
import { ref, onMounted } from 'vue'

const message = ref('')
const backendStatus = ref('Checking backend...')

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/status')
    if (response.ok) {
        const data = await response.json()
        backendStatus.value = `Backend says: ${data.status}`
    } else {
        backendStatus.value = 'Backend unreachable'
    }
  } catch (e) {
    backendStatus.value = 'Backend unreachable (is uvicorn running?)'
  }
})
</script>

<template>
  <div class="home" style="text-align: center; margin-top: 50px;">
    <h1>Russ Hendy</h1>
    <p>Personal Website</p>
    <p><em>Coming Soon...</em></p>
    
    <div style="margin-top: 2rem; padding: 1rem; background: #f0f0f0; border-radius: 8px; display: inline-block;">
        <p><small>{{ backendStatus }}</small></p>
    </div>
  </div>
</template>