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
              class="px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 relative text-gray-700 hover:text-primary"
              active-class="text-primary after:content-[''] after:absolute after:bottom-0 after:left-0 after:right-0 after:h-0.5 after:bg-primary"
            >
              Home
            </router-link>

            <!-- Studio Mega Menu -->
            <div 
              class="relative group"
              @mouseenter="openStudio"
              @mouseleave="closeStudio"
            >
              <button 
                class="flex items-center gap-1 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 relative text-gray-700 hover:text-primary group-hover:text-primary"
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
                class="absolute top-full left-1/2 -translate-x-1/2 mt-4 w-[640px] bg-white/95 backdrop-blur-xl rounded-2xl shadow-2xl border border-gray-100 overflow-hidden transition-all duration-300 transform origin-top ring-1 ring-black/5"
                :class="{ 'opacity-100 scale-100 translate-y-0': isStudioOpen, 'opacity-0 scale-95 -translate-y-2': !isStudioOpen }"
                @mouseenter="openStudio"
                @mouseleave="closeStudio"
              >
                <!-- Decorative Top Line -->
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500"></div>

                <div class="p-8 grid grid-cols-2 gap-6">
                  <router-link 
                    v-for="item in studioItems" 
                    :key="item.name"
                    :to="item.path"
                    class="flex items-start p-4 rounded-xl hover:bg-gray-50/80 transition-all duration-300 group/item border border-transparent hover:border-gray-100"
                  >
                    <!-- Icon Container -->
                    <div class="relative flex-shrink-0">
                      <div class="w-16 h-16 rounded-full bg-blue-50 flex items-center justify-center group-hover/item:bg-white group-hover/item:shadow-md group-hover/item:scale-110 transition-all duration-300 border border-blue-100/50">
                        <img :src="item.icon" :alt="item.name" class="w-8 h-8 object-contain transition-transform duration-300" />
                      </div>
                      <!-- Tech decoration dots -->
                      <div class="absolute -top-1 -right-1 w-2 h-2 bg-green-400 rounded-full border-2 border-white opacity-0 group-hover/item:opacity-100 transition-opacity duration-300"></div>
                    </div>
                    
                    <div class="ml-5">
                      <h3 class="text-base font-bold font-mono text-gray-900 group-hover/item:text-primary transition-colors flex items-center gap-2">
                        {{ item.name }}
                        <span class="opacity-0 group-hover/item:opacity-100 transition-opacity text-xs text-primary">-></span>
                      </h3>
                      <p class="text-sm text-gray-500 mt-1.5 leading-relaxed">
                        {{ item.description }}
                      </p>
                    </div>
                  </router-link>
                </div>
                
                <!-- Bottom Bar -->
                <div class="bg-gray-50/80 px-8 py-4 border-t border-gray-100 flex items-center justify-between">
                  <div class="flex items-center gap-2 text-xs text-gray-500 font-mono">
                    <span class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
                    System Online
                  </div>
                  <p class="text-xs text-gray-400 font-mono">
                    // Explore our digital studio resources
                  </p>
                </div>
              </div>
            </div>

            <!-- Other Links -->
            <router-link
              v-for="item in navItems"
              :key="item.name"
              :to="item.path"
              class="px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 relative text-gray-700 hover:text-primary"
              active-class="text-primary after:content-[''] after:absolute after:bottom-0 after:left-0 after:right-0 after:h-0.5 after:bg-primary"
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
            class="block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200 text-gray-700 hover:text-primary hover:bg-gray-50"
            active-class="text-primary bg-blue-50"
          >
            Home
          </router-link>

          <!-- Mobile Studio Menu -->
          <div class="space-y-1">
            <button 
              @click="isMobileStudioOpen = !isMobileStudioOpen"
              class="w-full flex items-center justify-between block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200 text-gray-700 hover:text-primary hover:bg-gray-50"
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
                <img :src="item.icon" :alt="item.name" class="w-4 h-4 object-contain" />
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
            class="block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200 text-gray-700 hover:text-primary hover:bg-gray-50"
            active-class="text-primary bg-blue-50"
          >
            {{ item.name }}
          </router-link>

          <button
            @click="$emit('openLogin'); closeMobileMenu()"
            class="w-full text-left block px-3 py-2 rounded-md text-base font-medium transition-colors duration-200 text-gray-700 hover:text-primary hover:bg-gray-50"
          >
            Login
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { ChevronDown } from 'lucide-vue-next'

export default {
  name: 'NavigationBar',
  components: {
    ChevronDown
  },
  emits: ['openLogin'],
  data() {
    return {
      isMobileMenuOpen: false,
      isStudioOpen: false,
      isMobileStudioOpen: false,
      closeTimer: null,
      navItems: [
        { name: 'Projects', path: '/projects' },
        { name: 'Contact Us', path: '/contact' },
        { name: 'Hire a Developer', path: '/hire' }
      ],
      studioItems: [
        { 
          name: 'Prompts', 
          path: '/studio/prompts', 
          icon: 'https://cdn-icons-png.flaticon.com/512/15311/15311499.png',
          description: 'Curated AI prompts for developers'
        },
        { 
          name: 'Dotfiles & Scripts', 
          path: '/studio/dotfiles', 
          icon: 'https://cdn-icons-png.flaticon.com/512/4248/4248082.png',
          description: 'System configurations and automation'
        },
        { 
          name: 'Dev Tools', 
          path: '/studio/devtools', 
          icon: 'https://cdn-icons-png.flaticon.com/512/7991/7991055.png',
          description: 'Essential utilities for your workflow'
        },
        { 
          name: 'Resources', 
          path: '/studio/resources', 
          icon: 'https://cdn-icons-png.flaticon.com/512/1927/1927656.png',
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
    },
    openStudio() {
      if (this.closeTimer) {
        clearTimeout(this.closeTimer)
        this.closeTimer = null
      }
      this.isStudioOpen = true
    },
    closeStudio() {
      this.closeTimer = setTimeout(() => {
        this.isStudioOpen = false
      }, 300)
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
/* Styles removed and moved to template to fix @apply linting issues */
</style>
