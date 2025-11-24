<template>
  <section class="hero-section relative min-h-screen flex items-center justify-center overflow-hidden">
    <!-- Background Gradient -->
    <div class="absolute inset-0 bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800"></div>
    
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute inset-0 bg-pattern"></div>
    </div>

    <div class="container-custom relative z-10">
      <div class="flex flex-col lg:flex-row items-center justify-between">
        <!-- Content -->
        <div class="lg:w-1/2 text-center lg:text-left mb-12 lg:mb-0">
          <div class="animate-fade-in-up">
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-6 leading-tight">
              Hi, I'm <span class="text-yellow-400">Tayyab Hussayn</span>
            </h1>
            <h2 class="text-xl md:text-2xl lg:text-3xl text-blue-100 mb-8 font-light">
              A Passionate Web Developer
            </h2>
            <p class="text-lg text-blue-100 mb-10 max-w-2xl">
              I create beautiful, responsive websites and web applications using modern technologies. 
              Let's bring your ideas to life with clean code and stunning design.
            </p>
            
            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <router-link to="/hire" class="bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold py-4 px-8 rounded-full transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl">
                <i class="fas fa-handshake mr-2"></i>
                Hire Me
              </router-link>
              <router-link to="/projects" class="bg-transparent border-2 border-white text-white hover:bg-white hover:text-gray-900 font-semibold py-4 px-8 rounded-full transition-all duration-300 transform hover:scale-105">
                <i class="fas fa-eye mr-2"></i>
                View Projects
              </router-link>
            </div>
          </div>
        </div>

        <!-- Profile Image -->
        <div class="lg:w-1/2 flex justify-center lg:justify-end">
          <div class="relative animate-fade-in-right">
            <!-- Profile Image Container -->
            <div class="relative w-80 h-80 md:w-96 md:h-96">
              <!-- Decorative Elements -->
              <div class="absolute -top-4 -left-4 w-full h-full bg-yellow-400 rounded-full opacity-20 animate-pulse"></div>
              <div class="absolute -bottom-4 -right-4 w-full h-full bg-blue-300 rounded-full opacity-20 animate-pulse delay-1000"></div>
              
              <!-- Profile Image -->
              <div class="relative w-full h-full bg-gray-300 rounded-full overflow-hidden border-4 border-white shadow-2xl">

                <!-- You can replace the above div with an actual image: -->
                <img src="/src/assets/images/profile.png" alt="Tayyab Hussayn" class="w-full h-full object-cover">
              </div>
            </div>

            <!-- Floating Elements -->
            <div class="absolute top-10 -right-10 bg-white/20 backdrop-blur-sm rounded-lg p-4 animate-float">
              <i class="fas fa-code text-2xl text-white"></i>
            </div>
            <div class="absolute bottom-10 -left-10 bg-white/20 backdrop-blur-sm rounded-lg p-4 animate-float delay-500">
              <i class="fas fa-palette text-2xl text-white"></i>
            </div>
          </div>
        </div>
      </div>

      <!-- Scroll Down Indicator -->
      <div class="absolute bottom 8 left-1/2 transform -translate-x-1/2 animate-bounce">
        <div class="flex flex-col items-center text-white">
          <span class="text-sm mb-2">Scroll Down</span>
          <i class="fas fa-chevron-down text-xl"></i>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection'
}
</script>

<style scoped>
.hero-section {
  padding-top: 4rem; /* Account for fixed navbar */
}

.bg-pattern {
  background-image: radial-gradient(circle, rgba(255,255,255,0.1) 2px, transparent 2px);
  background-size: 60px 60px;
}

@keyframes fade-in-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in-right {
  from {
    opacity: 0;
    transform: translateX(30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-10px);
  }
}

.animate-fade-in-up {
  animation: fade-in-up 1s ease-out;
}

.animate-fade-in-right {
  animation: fade-in-right 1s ease-out 0.3s both;
}

.animate-float {
  animation: float 3s ease-in-out infinite;
}

.delay-500 {
  animation-delay: 0.5s;
}

.delay-1000 {
  animation-delay: 1s;
}
</style>
