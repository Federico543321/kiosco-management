import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token'))
  const usuario = ref(null)
  const autenticacionVerificada = ref(false)

  function cerrarSesion() {
  token.value = null
  usuario.value = null
  localStorage.removeItem('token')
}

async function obtenerUsuario() {
  if (!token.value) {
    autenticacionVerificada.value = true
    return false
  }

  const respuesta = await fetch('http://localhost:5000/me', {
    headers: {
      Authorization: `Bearer ${token.value}`,
    },
  })

  if (!respuesta.ok) {
    token.value = null
    usuario.value = null
    localStorage.removeItem('token')

    autenticacionVerificada.value = true
    return false
  }

  const datos = await respuesta.json()

  usuario.value = datos

  autenticacionVerificada.value = true
  return true
}

async function iniciarSesion(nombreUsuario, password) {
  const respuesta = await fetch('http://localhost:5000/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      nombre_usuario: nombreUsuario,
      password: password,
    }),
  })

  const datos = await respuesta.json()

  if (!respuesta.ok) {
    return {
      ok: false,
      mensaje: datos.mensaje,
    }
  }

  token.value = datos.token
  usuario.value = datos.usuario

  localStorage.setItem('token', datos.token)

  return {
    ok: true,
  }
}

  return {
    token,
    usuario,
    cerrarSesion,
    obtenerUsuario,
    iniciarSesion,
    autenticacionVerificada,
  }
})
