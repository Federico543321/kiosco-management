import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const usuario = ref(null)

  function cerrarSesion() {
  token.value = null
  usuario.value = null
  localStorage.removeItem('token')
}

  return {
    token,
    usuario,
    cerrarSesion,
  }
})
