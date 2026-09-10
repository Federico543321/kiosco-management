import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import DashboardView from '../views/DashboardView.vue'
import { useAuthStore } from '../stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: {
        requiereAuth: true,
      },
    }
  ],
})

router.beforeEach(async (to) => {
  const authStore = useAuthStore()

  if (!authStore.autenticacionVerificada) {
    await authStore.obtenerUsuario()
  }

  if (to.meta.requiereAuth && !authStore.token) {
    return '/login'
  }

  if (to.path === '/login' && authStore.token) {
    return '/dashboard'
  }
})

export default router
