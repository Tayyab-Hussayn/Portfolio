<template>
  <div class="home">
    <!-- Hero Section -->
    <HeroSection />
    
    <!-- Services Section -->
    <ServicesSection />

    <!-- Techstack -->
    <TechStack />
    
    <!-- Projects Section -->
    <ProjectsSection />
    
    <!-- Contact Section -->
    <ContactSection />
  </div>
</template>

<script>
import HeroSection from '../components/HeroSection.vue'
import ServicesSection from '../components/ServicesSection.vue'
import ProjectsSection from '../components/ProjectsSection.vue'
import ContactSection from '../components/ContactSection.vue'
import TechStack from '../components/TechStack.vue'

export default {
  name: 'Home',
  components: {
    HeroSection,
    ServicesSection,
    ProjectsSection,
    ContactSection,
    TechStack
  }
}
</script>

