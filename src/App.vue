<template>
  <div id="app">
    <!-- Navigation Bar -->
    <NavigationBar @openLogin="showLoginModal = true" />
    
    <!-- Main Content -->
    <main>
      <router-view />
    </main>
    
    <!-- Footer -->
    <FooterSection />
    
    <!-- Login Modal -->
    <LoginModal 
      :isVisible="showLoginModal" 
      @close="showLoginModal = false" 
    />
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import FooterSection from './components/FooterSection.vue'
import LoginModal from './components/LoginModal.vue'

export default {
  name: 'App',
  components: {
    NavigationBar,
    FooterSection,
    LoginModal
  },
  data() {
    return {
      showLoginModal: false
    }
  }
}
</script>

<style>
/* Global styles are imported in main.js */
</style>

