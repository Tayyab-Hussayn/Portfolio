<template>
  <section class="section-padding bg-gray-50">
    <div class="container-custom">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
          Our Services
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          I offer a comprehensive range of web development services to help bring your digital vision to life
        </p>
      </div>

      <!-- Services Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <ServiceCard
          v-for="service in services"
          :key="service.id"
          :service="service"
        />
      </div>

      <!-- Call to Action -->
      <div class="text-center mt-16">
        <p class="text-lg text-gray-600 mb-8">
          Ready to start your project? Let's discuss your requirements.
        </p>
        <router-link to="/contact" class="btn-primary">
          Get Started Today
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import ServiceCard from './ServiceCard.vue'

export default {
  name: 'ServicesSection',
  components: {
    ServiceCard
  },
  data() {
    return {
      services: [
        {
          id: 1,
          title: 'Web Development',
          description: 'Custom websites and web applications built with modern technologies like Vue.js, React, and Node.js.',
          icon: 'fas fa-code',
          color: 'blue'
        },
        {
          id: 2,
          title: 'UI/UX Design',
          description: 'Beautiful, user-friendly interfaces designed to provide exceptional user experiences across all devices.',
          icon: 'fas fa-palette',
          color: 'purple'
        },
        {
          id: 3,
          title: 'SEO Optimization',
          description: 'Improve your website\'s visibility and ranking on search engines to drive more organic traffic.',
          icon: 'fas fa-search',
          color: 'green'
        },
        {
          id: 4,
          title: 'Freelancing',
          description: 'Flexible freelance services for short-term projects, ongoing maintenance, and technical consulting.',
          icon: 'fas fa-handshake',
          color: 'orange'
        }
      ]
    }
  }
}
</script>

