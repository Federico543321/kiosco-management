<script setup>
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

function cerrarSesion() {
  authStore.cerrarSesion()
  router.push('/login')
}
</script>

<template>
  <main class="dashboard">
    <h1>Dashboard</h1>
    <p>Bienvenido a PuntoAgil.</p>

    <button @click="cerrarSesion">
      Cerrar sesión
    </button>
  </main>
</template>

<style scoped>
.dashboard {
  min-height: 100vh;
  padding: 32px;
  box-sizing: border-box;
}

h1 {
  margin: 0 0 8px;
}

p {
  margin: 0 0 20px;
}

button {
  padding: 10px 16px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}
</style>
