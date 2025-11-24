<template>
  <div class="relative bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2 cursor-pointer overflow-hidden group">
    <!-- Icon Container -->
    <div class="w-16 h-16 rounded-full flex items-center justify-center mx-auto mt-8 mb-4 transition-all duration-300" :class="iconColorClass">
      <i :class="service.icon" class="text-3xl"></i>
    </div>

    <!-- Content -->
    <div class="p-6">
      <h3 class="text-xl font-semibold text-gray-900 mb-4 group-hover:text-primary transition-colors duration-300">
        {{ service.title }}
      </h3>
      <p class="text-gray-600 leading-relaxed">
        {{ service.description }}
      </p>
    </div>

    <!-- Hover Effect Overlay -->
    <div class="absolute inset-0 bg-gradient-to-br opacity-0 group-hover:opacity-10 transition-opacity duration-300 rounded-xl"
         :class="gradientClass">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ServiceCard',
  props: {
    service: {
      type: Object,
      required: true
    }
  },
  computed: {
    iconColorClass() {
      const colorMap = {
        blue: 'bg-blue-100 text-blue-600 group-hover:bg-blue-600 group-hover:text-white',
        purple: 'bg-purple-100 text-purple-600 group-hover:bg-purple-600 group-hover:text-white',
        green: 'bg-green-100 text-green-600 group-hover:bg-green-600 group-hover:text-white',
        orange: 'bg-orange-100 text-orange-600 group-hover:bg-orange-600 group-hover:text-white'
      }
      return colorMap[this.service.color] || colorMap.blue
    },
    gradientClass() {
      const gradientMap = {
        blue: 'from-blue-400 to-blue-600',
        purple: 'from-purple-400 to-purple-600',
        green: 'from-green-400 to-green-600',
        orange: 'from-orange-400 to-orange-600'
      }
      return gradientMap[this.service.color] || gradientMap.blue
    }
  }
}
</script>

<style scoped>
/* Styles removed and moved to template to fix @apply linting issues */
</style>
