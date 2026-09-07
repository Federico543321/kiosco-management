<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRouter } from 'vue-router'

const nombreUsuario = ref('')
const password = ref('')
const error = ref('')

const authStore = useAuthStore()
const router = useRouter()

async function iniciarSesion() {
  error.value = ''

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

  if (!respuesta.ok){
    error.value = datos.mensaje
    return
  }

  authStore.token = datos.token
  localStorage.setItem('token', datos.token)

  authStore.usuario = datos.usuario

  router.push('/dashboard')
}
</script>

<template>
  <main class="login-page">
    <section class="login-card">

      <div class="brand">
        <div class="brand-icon">
          <span></span>
          <span></span>
          <span></span>
        </div>

        <h1>Punto<span>Agil</span></h1>
      </div>

      <div class="welcome">
        <h2>Bienvenido</h2>
        <p>Iniciá sesión para comenzar a administrar tu negocio.</p>
      </div>

      <form @submit.prevent="iniciarSesion">

        <div class="campo">
          <label for="usuario">Usuario</label>

          <input
            id="usuario"
            type="text"
            v-model="nombreUsuario"
            placeholder="Ingresá tu usuario"
            autocomplete="off"
          />
        </div>

        <div class="campo">
          <label for="password">Contraseña</label>

          <input
            id="password"
            type="password"
            v-model="password"
            placeholder="Ingresá tu contraseña"
            autocomplete="new-password"
          />
        </div>
        <p v-if="error" class="error-message">
          {{ error }}
        </p>
        <button type="submit">
          Iniciar sesión
          <span class="arrow">→</span>
        </button>

      </form>

      <p class="footer-text">
        Una forma más simple de llevar tu negocio.
      </p>

    </section>
  </main>
</template>

<style scoped>
.login-page {
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 24px;
  box-sizing: border-box;

  background:
    radial-gradient(
      circle at 15% 20%,
      rgba(111, 218, 188, 0.12),
      transparent 28%
    ),
    radial-gradient(
      circle at 85% 80%,
      rgba(116, 200, 220, 0.12),
      transparent 28%
    ),
    #f5f8f7;
}

.login-card {
  width: 100%;
  max-width: 420px;
  padding: 40px;
  box-sizing: border-box;

  background: #ffffff;
  border: 1px solid #e5eeeb;
  border-radius: 20px;

  box-shadow: 0 12px 35px rgba(35, 72, 63, 0.08);
}

/* Marca */

.brand {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 32px;
}

.brand h1 {
  margin: 0;
  color: #263a35;
  font-size: 28px;
  font-weight: 750;
  letter-spacing: -0.8px;
}

.brand h1 span {
  color: #42a88d;
}

/* Ícono */

.brand-icon {
  width: 38px;
  height: 38px;
  position: relative;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 3px;

  background: #e5f6f1;
  border-radius: 11px;
}

.brand-icon span {
  display: block;
  width: 5px;
  border-radius: 3px;
  background: #42a88d;
}

.brand-icon span:nth-child(1) {
  height: 13px;
}

.brand-icon span:nth-child(2) {
  height: 20px;
  background: #65bcd0;
}

.brand-icon span:nth-child(3) {
  height: 16px;
}

/* Bienvenida */

.welcome {
  margin-bottom: 28px;
}

.welcome h2 {
  margin: 0 0 8px;
  color: #263a35;
  font-size: 23px;
  font-weight: 700;
}

.welcome p {
  margin: 0;
  color: #71807c;
  font-size: 15px;
  line-height: 1.5;
}

/* Campos */

.campo {
  margin-bottom: 20px;
}

.campo label {
  display: block;
  margin-bottom: 7px;

  color: #394b46;
  font-size: 14px;
  font-weight: 650;
}

.campo input {
  width: 100%;
  box-sizing: border-box;
  padding: 13px 14px;

  background: #fbfcfc;
  border: 1px solid #dce7e3;
  border-radius: 10px;

  color: #263a35;
  font-family: inherit;
  font-size: 15px;

  transition:
    border-color 0.2s ease,
    box-shadow 0.2s ease,
    background 0.2s ease;
}

.campo input::placeholder {
  color: #a0aaa7;
}

.campo input:focus {
  outline: none;
  background: #ffffff;
  border-color: #5bbda4;
  box-shadow: 0 0 0 3px rgba(91, 189, 164, 0.12);
}

/* Botón */

button {
  width: 100%;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 9px;

  margin-top: 8px;
  padding: 13px 16px;

  border: none;
  border-radius: 10px;

  background: #42a88d;
  color: #ffffff;

  font-family: inherit;
  font-size: 15px;
  font-weight: 650;

  cursor: pointer;

  transition:
    background 0.2s ease,
    transform 0.15s ease;
}

button:hover {
  background: #378f78;
}

button:active {
  transform: translateY(1px);
}

.arrow {
  font-size: 18px;
  line-height: 1;
}

/* Texto inferior */

.footer-text {
  margin: 26px 0 0;

  color: #9aa5a2;
  font-size: 13px;
  text-align: center;
}

/* Tablet */

@media (max-width: 600px) {
  .login-page {
    padding: 20px;
  }

  .login-card {
    max-width: 460px;
    padding: 36px;
  }
}

/* Celular */

@media (max-width: 480px) {
  .login-page {
    padding: 16px;
  }

  .login-card {
    padding: 30px 22px;
    border-radius: 18px;
  }

  .brand {
    margin-bottom: 28px;
  }

  .brand h1 {
    font-size: 27px;
  }

  .welcome h2 {
    font-size: 21px;
  }
}

.error-message {
  margin: -4px 0 16px;

  color: #c65b5b;
  font-size: 13px;
  line-height: 1.4;
}
</style>