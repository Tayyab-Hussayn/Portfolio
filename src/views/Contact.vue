<template>
  <div class="contact-page">
    <!-- Page Header -->
    <section class="page-header">
      <div class="container-custom">
        <div class="text-center">
          <h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
            Get In Touch
          </h1>
          <p class="text-xl text-blue-100 max-w-3xl mx-auto">
            Have a project in mind? Let's discuss how we can work together to bring your ideas to life.
          </p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <ContactSection />
  </div>
</template>

<script>
import ContactSection from '../components/ContactSection.vue'

export default {
  name: 'Contact',
  components: {
    ContactSection
  }
}
</script>

<style scoped>
.page-header {
  @apply bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800 section-padding;
  padding-top: 8rem; /* Account for fixed navbar */
}
</style>

