<template>
  <div class="home">
    <!-- Hero Section -->
    <HeroSection />
    
    <!-- Services Section -->
    <ServicesSection />

    <!-- Techstack -->
    <SkillGraph />
    
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
import SkillGraph from '../components/SkillGraph.vue'

export default {
  name: 'Home',
  components: {
    HeroSection,
    ServicesSection,
    ProjectsSection,
    ContactSection,
    SkillGraph
  }
}
</script>

