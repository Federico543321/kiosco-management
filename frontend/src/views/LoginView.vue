<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'

const nombreUsuario = ref('')
const password = ref('')

const authStore = useAuthStore()


async function iniciarSesion() {
    const respuesta = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            nombre_usuario: nombreUsuario.value,
            password: password.value,
        }),
    })

    const datos = await respuesta.json()
    authStore.token = datos.token
    authStore.usuario = datos.usuario
}
</script>

<template>
  <main>
    <h1>Iniciar sesión</h1>

    <form @submit.prevent="iniciarSesion">
      <label>Usuario</label>
      <input type="text" v-model="nombreUsuario" />

      <label>Contraseña</label>
      <input type="password" v-model="password" />

      <button type="submit">Iniciar sesión</button>
    </form>

  </main>
</template>