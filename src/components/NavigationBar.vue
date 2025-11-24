<template>
  <nav class="fixed top-0 left-0 right-0 bg-white/95 backdrop-blur-sm shadow-lg z-50">
    <div class="container-custom">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <div class="flex-shrink-0">
          <router-link to="/" class="text-2xl font-bold text-primary">
            Portfolio
          </router-link>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:block">
          <div class="ml-10 flex items-baseline space-x-8">
            <!-- Home Link -->
            <router-link
              to="/"
              class="nav-link"
              :class="{ 'nav-link-active': $route.path === '/' }"
            >
              Home
            </router-link>

            <!-- Studio Mega Menu -->
            <div 
              class="relative group"
              @mouseenter="isStudioOpen = true"
              @mouseleave="isStudioOpen = false"
            >
              <button 
                class="nav-link flex items-center gap-1 group-hover:text-primary"
                :class="{ 'text-primary': isStudioOpen }"
              >
                Studio
                <ChevronDown 
                  class="w-4 h-4 transition-transform duration-200"
                  :class="{ 'rotate-180': isStudioOpen }"
                />
              </button>

              <!-- Mega Menu Dropdown -->
              <div 
                v-show="isStudioOpen"
                class="absolute top-full left-1/2 -translate-x-1/2 mt-2 w-[600px] bg-white/95 backdrop-blur-md rounded-xl shadow-xl border border-gray-100 overflow-hidden transition-all duration-300 transform origin-top"
                :class="{ 'opacity-100 scale-100': isStudioOpen, 'opacity-0 scale-95': !isStudioOpen }"
              >
                <div class="p-6 grid grid-cols-2 gap-4">
                  <router-link 
                    v-for="item in studioItems" 
                    :key="item.name"
                    :to="item.path"
                    class="flex items-start p-4 rounded-lg hover:bg-gray-50 transition-colors group/item"
                  >
                    <div class="p-2 bg-blue-50 text-primary rounded-lg group-hover/item:bg-primary group-hover/item:text-white transition-colors">
                      <component :is="item.icon" class="w-6 h-6" />
                    </div>
                    <div class="ml-4">
                      <h3 class="text-base font-semibold text-gray-900 group-hover/item:text-primary transition-colors">
                        {{ item.name }}
                      </h3>
                      <p class="text-sm text-gray-500 mt-1">
                        {{ item.description }}
                      </p>
                    </div>
                  </router-link>
                </div>
                
                <!-- Bottom Bar -->
                <div class="bg-gray-50 px-6 py-3 border-t border-gray-100">
                  <p class="text-xs text-gray-500 text-center">
                    Explore our digital studio resources and tools
                  </p>
                </div>
              </div>
            </div>

            <!-- Other Links -->
            <router-link
              v-for="item in navItems"
              :key="item.name"
              :to="item.path"
              class="nav-link"
              :class="{ 'nav-link-active': $route.path === item.path }"
            >
              {{ item.name }}
            </router-link>

            <button
              @click="$emit('openLogin')"
              class="btn-primary text-sm"
            >
              Login
            </button>
          </div>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            @click="toggleMobileMenu"
            class="text-gray-700 hover:text-primary focus:outline-none focus:text-primary"
          >
            <i class="fas fa-bars text-xl"></i>
          </button>
        </div>
      </div>

      <!-- Mobile Navigation -->
      <div v-if="isMobileMenuOpen" class="md:hidden h-[calc(100vh-4rem)] overflow-y-auto">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
          <!-- Mobile Home -->
          <router-link
            to="/"
            @click="closeMobileMenu"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === '/' }"
          >
            Home
          </router-link>

          <!-- Mobile Studio Menu -->
          <div class="space-y-1">
            <button 
              @click="isMobileStudioOpen = !isMobileStudioOpen"
              class="w-full flex items-center justify-between mobile-nav-link"
              :class="{ 'text-primary bg-blue-50': isMobileStudioOpen }"
            >
              Studio
              <ChevronDown 
                class="w-4 h-4 transition-transform duration-200"
                :class="{ 'rotate-180': isMobileStudioOpen }"
              />
            </button>
            
            <div v-show="isMobileStudioOpen" class="pl-4 space-y-1 bg-gray-50/50 rounded-lg mx-2">
              <router-link
                v-for="item in studioItems"
                :key="item.name"
                :to="item.path"
                @click="closeMobileMenu"
                class="flex items-center gap-3 px-3 py-3 text-gray-600 hover:text-primary rounded-md transition-colors"
              >
                <component :is="item.icon" class="w-4 h-4" />
                <span class="text-sm font-medium">{{ item.name }}</span>
              </router-link>
            </div>
          </div>

          <!-- Other Mobile Links -->
          <router-link
            v-for="item in navItems"
            :key="item.name"
            :to="item.path"
            @click="closeMobileMenu"
            class="mobile-nav-link"
            :class="{ 'mobile-nav-link-active': $route.path === item.path }"
          >
            {{ item.name }}
          </router-link>

          <button
            @click="$emit('openLogin'); closeMobileMenu()"
            class="w-full text-left mobile-nav-link"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { ChevronDown, Terminal, FileCode, Wrench, BookOpen } from 'lucide-vue-next'

export default {
  name: 'NavigationBar',
  components: {
    ChevronDown,
    Terminal,
    FileCode,
    Wrench,
    BookOpen
  },
  emits: ['openLogin'],
  data() {
    return {
      isMobileMenuOpen: false,
      isStudioOpen: false,
      isMobileStudioOpen: false,
      navItems: [
        { name: 'Projects', path: '/projects' },
        { name: 'Contact Us', path: '/contact' },
        { name: 'Hire a Developer', path: '/hire' }
      ],
      studioItems: [
        { 
          name: 'Prompts', 
          path: '/studio/prompts', 
          icon: 'Terminal',
          description: 'Curated AI prompts for developers'
        },
        { 
          name: 'Dotfiles & Scripts', 
          path: '/studio/dotfiles', 
          icon: 'FileCode',
          description: 'System configurations and automation'
        },
        { 
          name: 'Dev Tools', 
          path: '/studio/devtools', 
          icon: 'Wrench',
          description: 'Essential utilities for your workflow'
        },
        { 
          name: 'Resources', 
          path: '/studio/resources', 
          icon: 'BookOpen',
          description: 'Guides, assets, and learning materials'
        }
      ]
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false
      this.isMobileStudioOpen = false
    }
  },
  mounted() {
    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!this.$el.contains(e.target)) {
        this.isMobileMenuOpen = false
      }
    })
  }
}
</script>

<style scoped>
.nav-link {
  @apply text-gray-700 hover:text-primary px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 relative;
}

.nav-link:hover {
  @apply text-primary;
}

.nav-link-active {
  @apply text-primary;
}

.nav-link-active::after {
  content: '';
  @apply absolute bottom-0 left-0 right-0 h-0.5 bg-primary;
}

.mobile-nav-link {
  @apply text-gray-700 hover:text-primary hover:bg-gray-50 block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200;
}

.mobile-nav-link-active {
  @apply text-primary bg-blue-50;
}
</style>

