<template>
  <div class="group relative bg-white rounded-2xl p-6 border border-gray-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col h-full">
    <!-- Header -->
    <div class="flex items-start justify-between mb-4">
      <div class="p-3 bg-blue-50 text-primary rounded-xl group-hover:scale-110 transition-transform duration-300">
        <component :is="iconComponent" class="w-6 h-6" />
      </div>
      
      <button 
        @click="handleCopy"
        class="p-2 rounded-lg text-gray-400 hover:text-primary hover:bg-blue-50 transition-all duration-200"
        :class="{ 'text-green-500 bg-green-50 hover:text-green-600 hover:bg-green-100': isCopied }"
        :title="isCopied ? 'Copied!' : 'Copy Prompt'"
      >
        <Check v-if="isCopied" class="w-5 h-5" />
        <Copy v-else class="w-5 h-5" />
      </button>
    </div>

    <!-- Content -->
    <h3 class="text-lg font-bold text-gray-900 mb-2 group-hover:text-primary transition-colors duration-200">
      {{ prompt.title }}
    </h3>
    
    <p class="text-gray-500 text-sm leading-relaxed mb-6 line-clamp-3 flex-grow">
      {{ prompt.description }}
    </p>

    <!-- Footer -->
    <div class="flex flex-wrap gap-2 mt-auto pt-4 border-t border-gray-50">
      <TagChip v-for="tag in prompt.tags" :key="tag">
        {{ tag }}
      </TagChip>
    </div>

    <!-- Decorative Gradient Border (Bottom) -->
    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-b-2xl"></div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Copy, Check, CodeXml, Bug, Zap, Layers, Rocket, BookOpen, Code } from 'lucide-vue-next'
import TagChip from './TagChip.vue'

const props = defineProps({
  prompt: {
    type: Object,
    required: true
  }
})

const isCopied = ref(false)

// Map icon string names to actual components
const iconMap = {
  CodeXml,
  Bug,
  Zap,
  Layers,
  Rocket,
  BookOpen,
  Code
}

const iconComponent = computed(() => {
  // Handle case sensitivity or direct component passing if needed
  // For now assuming prompt.icon matches the key exactly or with case difference
  const iconName = props.prompt.icon
  // Try exact match
  if (iconMap[iconName]) return iconMap[iconName]
  
  // Try case-insensitive match
  const key = Object.keys(iconMap).find(k => k.toLowerCase() === iconName.toLowerCase())
  return key ? iconMap[key] : Code // Default fallback
})

const handleCopy = async () => {
  try {
    await navigator.clipboard.writeText(props.prompt.content)
    isCopied.value = true
    setTimeout(() => {
      isCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>
