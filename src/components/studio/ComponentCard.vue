<template>
  <div class="bg-white rounded-2xl border border-gray-200 overflow-hidden shadow-sm hover:shadow-md transition-all duration-300">
    <div class="p-6 border-b border-gray-100">
      <div class="flex items-start justify-between">
        <div>
          <h3 class="text-xl font-bold text-gray-900 mb-2">{{ title }}</h3>
          <p class="text-gray-500 text-sm">{{ description }}</p>
        </div>
        <div class="flex bg-gray-100 rounded-lg p-1">
          <button 
            @click="activeTab = 'preview'"
            class="px-3 py-1.5 text-xs font-medium rounded-md transition-all duration-200"
            :class="activeTab === 'preview' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700'"
          >
            Preview
          </button>
          <button 
            @click="activeTab = 'code'"
            class="px-3 py-1.5 text-xs font-medium rounded-md transition-all duration-200"
            :class="activeTab === 'code' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700'"
          >
            Code
          </button>
        </div>
      </div>
    </div>

    <div class="relative group">
      <!-- Preview Tab -->
      <div v-if="activeTab === 'preview'" class="bg-gray-50 min-h-[300px] max-h-[500px] overflow-y-auto relative">
        <!-- Render the HTML content inside a shadow DOM or iframe-like container would be ideal, 
             but for simplicity we'll render it directly or use an iframe if styles conflict. 
             Given the styles are scoped in the HTML string, we might need to be careful.
             For now, let's use a safe iframe approach to isolate styles. -->
        <iframe 
          :srcdoc="code" 
          class="w-full h-full min-h-[400px] border-none"
          title="Component Preview"
        ></iframe>
      </div>

      <!-- Code Tab -->
      <div v-else class="bg-[#0d0d12] min-h-[300px] max-h-[500px] overflow-y-auto p-4">
        <pre class="text-xs font-mono text-gray-300 whitespace-pre-wrap"><code>{{ code }}</code></pre>
      </div>

      <!-- Copy Button (Floating) -->
      <div class="absolute top-4 right-4 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
        <button 
          @click="handleCopy"
          class="p-2 bg-white/10 backdrop-blur-md border border-white/20 rounded-lg text-white hover:bg-white/20 transition-colors shadow-lg"
          :class="{ 'bg-green-500/20 border-green-500/50 text-green-400': isCopied }"
          title="Copy Code"
        >
          <Check v-if="isCopied" class="w-5 h-5" />
          <Copy v-else class="w-5 h-5" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Copy, Check } from 'lucide-vue-next'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  code: {
    type: String,
    required: true
  }
})

const activeTab = ref('preview')
const isCopied = ref(false)

const handleCopy = async () => {
  try {
    await navigator.clipboard.writeText(props.code)
    isCopied.value = true
    setTimeout(() => {
      isCopied.value = false
    }, 2000)
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}
</script>
