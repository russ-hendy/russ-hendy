import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import NotFound from '../views/NotFound.vue'

const router = createRouter({
  // createWebHistory enables clean URLs (e.g., /page-2) without hashes (#)
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      // This is a Regex that matches any string
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: NotFound
    }
  ]
})

export default router