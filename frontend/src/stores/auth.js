import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(null)
  const usuario = ref(null)

  return {
    token,
    usuario,
  }
})