<template>
  <div class="bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 overflow-hidden group">
    <!-- Project Image -->
    <div class="relative overflow-hidden rounded-t-xl">
      <div class="relative overflow-hidden">
        <!-- Placeholder for project image -->
        <div class="w-full h-48 bg-gradient-to-br from-blue-400 to-purple-500 flex items-center justify-center">
          <i class="fas fa-image text-4xl text-white opacity-50"></i>
        </div>
        <!-- You can replace the above div with an actual image: -->
        <!-- <img :src="project.image" :alt="project.title" class="w-full h-48 object-cover"> -->
      </div>
      
      <!-- Overlay with buttons -->
      <div class="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-70 transition-all duration-300 flex items-center justify-center opacity-0 group-hover:opacity-100">
        <div class="flex space-x-4">
          <a 
            :href="project.liveUrl" 
            target="_blank" 
            rel="noopener noreferrer"
            class="bg-white text-gray-900 px-4 py-2 rounded-lg font-medium hover:bg-gray-100 transition-colors duration-200 transform hover:scale-105"
          >
            <i class="fas fa-external-link-alt mr-2"></i>
            Live Preview
          </a>
          <a 
            :href="project.githubUrl" 
            target="_blank" 
            rel="noopener noreferrer"
            class="bg-transparent border-2 border-white text-white px-4 py-2 rounded-lg font-medium hover:bg-white hover:text-gray-900 transition-all duration-200 transform hover:scale-105"
          >
            <i class="fab fa-github mr-2"></i>
            Code
          </a>
        </div>
      </div>

      <!-- Category Badge -->
      <div class="absolute top-4 left-4">
        <span class="bg-primary text-white px-3 py-1 rounded-full text-xs font-medium">
          {{ project.category }}
        </span>
      </div>
    </div>

    <!-- Project Content -->
    <div class="p-6">
      <h3 class="text-xl font-semibold text-gray-900 mb-3 group-hover:text-primary transition-colors duration-300">
        {{ project.title }}
      </h3>
      <p class="text-gray-600 mb-4 leading-relaxed">
        {{ project.description }}
      </p>

      <!-- Tech Stack -->
      <div class="mb-4">
        <h4 class="text-sm font-medium text-gray-700 mb-2">Tech Stack:</h4>
        <div class="flex flex-wrap gap-2">
          <span 
            v-for="tech in project.techStack" 
            :key="tech"
            class="bg-gray-100 text-gray-700 px-3 py-1 rounded-full text-xs font-medium hover:bg-gray-200 transition-colors duration-200"
          >
            {{ tech }}
          </span>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex space-x-3">
        <a 
          :href="project.liveUrl" 
          target="_blank" 
          rel="noopener noreferrer"
          class="bg-primary hover:bg-secondary text-white font-medium py-2 px-4 rounded-lg transition-all duration-300 transform hover:scale-105 text-sm flex-1 text-center"
        >
          <i class="fas fa-eye mr-2"></i>
          Live Preview
        </a>
        <a 
          :href="project.githubUrl" 
          target="_blank" 
          rel="noopener noreferrer"
          class="bg-gray-100 hover:bg-gray-200 text-gray-700 font-medium py-2 px-3 rounded-lg transition-all duration-300 transform hover:scale-105"
        >
          <i class="fab fa-github"></i>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectCard',
  props: {
    project: {
      type: Object,
      required: true
    }
  }
}
</script>

<style scoped>
/* Styles removed and moved to template to fix @apply linting issues */
</style>
