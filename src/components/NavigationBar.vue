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
      <div v-if="isMobileMenuOpen" class="md:hidden">
        <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
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
export default {
  name: 'NavigationBar',
  emits: ['openLogin'],
  data() {
    return {
      isMobileMenuOpen: false,
      navItems: [
        { name: 'Home', path: '/' },
        { name: 'Projects', path: '/projects' },
        { name: 'Contact Us', path: '/contact' },
        { name: 'Hire a Developer', path: '/hire' }
      ]
    }
  },
  methods: {
    toggleMobileMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen
    },
    closeMobileMenu() {
      this.isMobileMenuOpen = false
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

