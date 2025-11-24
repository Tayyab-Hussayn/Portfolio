import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Projects from '../views/Projects.vue'
import Contact from '../views/Contact.vue'
import Hire from '../views/Hire.vue'
import Prompts from '../views/studio/Prompts.vue'
import Dotfiles from '../views/studio/Dotfiles.vue'
import DevTools from '../views/studio/DevTools.vue'
import Resources from '../views/studio/Resources.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
  {
    path: '/hire',
    name: 'Hire',
    component: Hire
  },
  {
    path: '/studio/prompts',
    name: 'Prompts',
    component: Prompts
  },
  {
    path: '/studio/dotfiles',
    name: 'Dotfiles',
    component: Dotfiles
  },
  {
    path: '/studio/devtools',
    name: 'DevTools',
    component: DevTools
  },
  {
    path: '/studio/resources',
    name: 'Resources',
    component: Resources
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router

