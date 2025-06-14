<template>
  <footer class="bg-gray-900 text-white">
    <!-- Main Footer Content -->
    <div class="section-padding">
      <div class="container-custom">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <!-- Brand Section -->
          <div class="lg:col-span-2">
            <div class="mb-6">
              <h3 class="text-2xl font-bold text-white mb-4">
                Alex Johnson
              </h3>
              <p class="text-gray-300 leading-relaxed max-w-md">
                Passionate web developer creating beautiful, responsive websites and web applications. 
                Let's build something amazing together.
              </p>
            </div>
            
            <!-- Social Media Links -->
            <div class="flex space-x-4">
              <a 
                href="https://github.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="social-icon"
                aria-label="GitHub"
              >
                <i class="fab fa-github"></i>
              </a>
              <a 
                href="https://linkedin.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="social-icon"
                aria-label="LinkedIn"
              >
                <i class="fab fa-linkedin"></i>
              </a>
              <a 
                href="https://twitter.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="social-icon"
                aria-label="Twitter"
              >
                <i class="fab fa-twitter"></i>
              </a>
              <a 
                href="https://dribbble.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="social-icon"
                aria-label="Dribbble"
              >
                <i class="fab fa-dribbble"></i>
              </a>
              <a 
                href="https://instagram.com" 
                target="_blank" 
                rel="noopener noreferrer"
                class="social-icon"
                aria-label="Instagram"
              >
                <i class="fab fa-instagram"></i>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div>
            <h4 class="text-lg font-semibold mb-6">Quick Links</h4>
            <ul class="space-y-3">
              <li>
                <router-link to="/" class="footer-link">
                  Home
                </router-link>
              </li>
              <li>
                <router-link to="/projects" class="footer-link">
                  Projects
                </router-link>
              </li>
              <li>
                <router-link to="/contact" class="footer-link">
                  Contact
                </router-link>
              </li>
              <li>
                <router-link to="/hire" class="footer-link">
                  Hire Me
                </router-link>
              </li>
            </ul>
          </div>

          <!-- Services -->
          <div>
            <h4 class="text-lg font-semibold mb-6">Services</h4>
            <ul class="space-y-3">
              <li>
                <a href="#" class="footer-link">
                  Web Development
                </a>
              </li>
              <li>
                <a href="#" class="footer-link">
                  UI/UX Design
                </a>
              </li>
              <li>
                <a href="#" class="footer-link">
                  SEO Optimization
                </a>
              </li>
              <li>
                <a href="#" class="footer-link">
                  Consulting
                </a>
              </li>
            </ul>
          </div>
        </div>

        <!-- Newsletter Signup -->
        <div class="mt-12 pt-8 border-t border-gray-700">
          <div class="text-center lg:text-left lg:flex lg:items-center lg:justify-between">
            <div class="mb-6 lg:mb-0">
              <h4 class="text-lg font-semibold mb-2">Stay Updated</h4>
              <p class="text-gray-300">Get notified about new projects and updates.</p>
            </div>
            <div class="flex flex-col sm:flex-row gap-4 lg:max-w-md">
              <input
                type="email"
                placeholder="Enter your email"
                class="newsletter-input"
              >
              <button class="newsletter-btn">
                Subscribe
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Footer -->
    <div class="border-t border-gray-700">
      <div class="container-custom py-6">
        <div class="flex flex-col md:flex-row items-center justify-between">
          <!-- Copyright -->
          <div class="text-center md:text-left mb-4 md:mb-0">
            <p class="text-gray-300">
              © {{ currentYear }} Alex Johnson. All rights reserved.
            </p>
          </div>

          <!-- Back to Top & Additional Links -->
          <div class="flex items-center space-x-6">
            <a href="#" class="footer-link text-sm">Privacy Policy</a>
            <a href="#" class="footer-link text-sm">Terms of Service</a>
            
            <!-- Back to Top Button -->
            <button 
              @click="scrollToTop"
              class="back-to-top"
              aria-label="Back to top"
            >
              <i class="fas fa-chevron-up"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  },
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      })
    }
  }
}
</script>

<style scoped>
.social-icon {
  @apply w-10 h-10 bg-gray-700 hover:bg-primary text-gray-300 hover:text-white rounded-full flex items-center justify-center text-lg transition-all duration-300 transform hover:scale-110;
}

.footer-link {
  @apply text-gray-300 hover:text-white transition-colors duration-200;
}

.newsletter-input {
  @apply flex-1 px-4 py-3 bg-gray-800 border border-gray-600 rounded-lg text-white placeholder-gray-400 focus:ring-2 focus:ring-primary focus:border-transparent;
}

.newsletter-btn {
  @apply bg-primary hover:bg-secondary text-white font-semibold px-6 py-3 rounded-lg transition-all duration-300 transform hover:scale-105;
}

.back-to-top {
  @apply w-10 h-10 bg-primary hover:bg-secondary text-white rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-110;
}
</style>

