<template>
  <div class="min-h-screen pt-16 bg-gray-50 flex flex-col">
    <!-- Header -->
    <div class="bg-white border-b border-gray-200 px-6 py-4">
      <div class="container-custom">
        <h1 class="text-2xl font-bold text-gray-900">Dev Tools</h1>
        <p class="text-sm text-gray-500">Essential utilities for your daily workflow</p>
      </div>
    </div>

    <!-- Dashboard Container -->
    <div class="flex-1 container-custom py-6 h-[calc(100vh-8rem)] min-h-[600px]">
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden flex h-full">
        <!-- Sidebar -->
        <div class="w-64 bg-gray-50 border-r border-gray-200 flex flex-col">
          <div class="p-4 border-b border-gray-200">
            <h2 class="text-xs font-semibold text-gray-500 uppercase tracking-wider">Tools</h2>
          </div>
          <div class="flex-1 overflow-y-auto py-2">
            <button
              v-for="tool in tools"
              :key="tool.id"
              @click="activeTool = tool.id"
              class="w-full text-left px-4 py-3 text-sm flex items-center gap-3 transition-colors border-l-2"
              :class="activeTool === tool.id ? 'bg-white border-primary text-primary font-medium' : 'border-transparent text-gray-600 hover:bg-gray-100 hover:text-gray-900'"
            >
              <component :is="tool.icon" class="w-4 h-4" />
              {{ tool.name }}
            </button>
          </div>
        </div>

        <!-- Main Content Area -->
        <div class="flex-1 flex flex-col bg-white overflow-y-auto">
          <!-- JSON Formatter -->
          <div v-if="activeTool === 'json'" class="p-6 h-full flex flex-col">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-gray-900">JSON Formatter</h3>
              <div class="flex gap-2">
                <button @click="formatJson" class="btn-tool">Prettify</button>
                <button @click="minifyJson" class="btn-tool">Minify</button>
                <button @click="clearJson" class="btn-tool-secondary">Clear</button>
              </div>
            </div>
            <div class="flex-1 grid grid-cols-2 gap-4 min-h-0">
              <div class="flex flex-col">
                <label class="text-xs font-medium text-gray-500 mb-1">Input</label>
                <textarea 
                  v-model="jsonInput" 
                  class="flex-1 w-full p-3 font-mono text-sm bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none resize-none"
                  placeholder="Paste JSON here..."
                ></textarea>
              </div>
              <div class="flex flex-col">
                <label class="text-xs font-medium text-gray-500 mb-1">Output</label>
                <div class="flex-1 relative">
                  <textarea 
                    readonly
                    :value="jsonOutput" 
                    class="w-full h-full p-3 font-mono text-sm bg-gray-900 text-gray-100 border border-gray-200 rounded-lg outline-none resize-none"
                    placeholder="Result will appear here..."
                  ></textarea>
                  <button 
                    v-if="jsonOutput"
                    @click="copyToClipboard(jsonOutput)"
                    class="absolute top-2 right-2 p-1.5 bg-gray-800 text-gray-400 hover:text-white rounded-md transition-colors"
                  >
                    <Copy class="w-4 h-4" />
                  </button>
                </div>
              </div>
            </div>
            <p v-if="jsonError" class="mt-2 text-sm text-red-500">{{ jsonError }}</p>
          </div>

          <!-- Base64 Converter -->
          <div v-if="activeTool === 'base64'" class="p-6 h-full flex flex-col">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-gray-900">Base64 Converter</h3>
              <div class="flex gap-2">
                <button @click="encodeBase64" class="btn-tool">Encode</button>
                <button @click="decodeBase64" class="btn-tool">Decode</button>
                <button @click="clearBase64" class="btn-tool-secondary">Clear</button>
              </div>
            </div>
            <div class="flex-1 grid grid-cols-2 gap-4 min-h-0">
              <div class="flex flex-col">
                <label class="text-xs font-medium text-gray-500 mb-1">Text Input</label>
                <textarea 
                  v-model="base64Input" 
                  class="flex-1 w-full p-3 font-mono text-sm bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none resize-none"
                  placeholder="Type text to encode/decode..."
                ></textarea>
              </div>
              <div class="flex flex-col">
                <label class="text-xs font-medium text-gray-500 mb-1">Result</label>
                <div class="flex-1 relative">
                  <textarea 
                    readonly
                    :value="base64Output" 
                    class="w-full h-full p-3 font-mono text-sm bg-gray-50 border border-gray-200 rounded-lg outline-none resize-none"
                    placeholder="Result..."
                  ></textarea>
                  <button 
                    v-if="base64Output"
                    @click="copyToClipboard(base64Output)"
                    class="absolute top-2 right-2 p-1.5 bg-white border border-gray-200 text-gray-500 hover:text-primary rounded-md transition-colors shadow-sm"
                  >
                    <Copy class="w-4 h-4" />
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Color Converter -->
          <div v-if="activeTool === 'color'" class="p-6 h-full">
            <h3 class="text-lg font-semibold text-gray-900 mb-6">Color Converter</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div class="space-y-4">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">HEX</label>
                  <input 
                    v-model="colorHex" 
                    @input="updateFromHex"
                    type="text" 
                    class="w-full p-2 border border-gray-300 rounded-md focus:ring-primary focus:border-primary uppercase"
                    placeholder="#000000"
                  >
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-1">RGB</label>
                  <div class="flex gap-2">
                    <input v-model.number="colorRgb.r" @input="updateFromRgb" type="number" min="0" max="255" class="w-full p-2 border border-gray-300 rounded-md" placeholder="R">
                    <input v-model.number="colorRgb.g" @input="updateFromRgb" type="number" min="0" max="255" class="w-full p-2 border border-gray-300 rounded-md" placeholder="G">
                    <input v-model.number="colorRgb.b" @input="updateFromRgb" type="number" min="0" max="255" class="w-full p-2 border border-gray-300 rounded-md" placeholder="B">
                  </div>
                </div>
              </div>
              
              <div class="flex flex-col items-center justify-center p-8 bg-gray-50 rounded-xl border border-gray-200">
                <div 
                  class="w-32 h-32 rounded-full shadow-lg border-4 border-white mb-4 transition-colors duration-200"
                  :style="{ backgroundColor: colorHex }"
                ></div>
                <p class="font-mono text-lg font-bold text-gray-900">{{ colorHex }}</p>
                <p class="font-mono text-sm text-gray-500">rgb({{ colorRgb.r }}, {{ colorRgb.g }}, {{ colorRgb.b }})</p>
              </div>
            </div>
          </div>

          <!-- Lorem Ipsum -->
          <div v-if="activeTool === 'lorem'" class="p-6 h-full flex flex-col">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-semibold text-gray-900">Lorem Ipsum Generator</h3>
              <div class="flex items-center gap-4">
                <div class="flex items-center gap-2">
                  <label class="text-sm text-gray-600">Paragraphs:</label>
                  <input 
                    v-model.number="loremCount" 
                    type="number" 
                    min="1" 
                    max="10" 
                    class="w-16 p-1 border border-gray-300 rounded-md text-center"
                  >
                </div>
                <button @click="generateLorem" class="btn-tool">Generate</button>
              </div>
            </div>
            <div class="flex-1 relative">
              <textarea 
                readonly
                :value="loremOutput" 
                class="w-full h-full p-4 text-base leading-relaxed text-gray-700 bg-gray-50 border border-gray-200 rounded-lg outline-none resize-none"
              ></textarea>
              <button 
                v-if="loremOutput"
                @click="copyToClipboard(loremOutput)"
                class="absolute top-4 right-4 p-2 bg-white border border-gray-200 text-gray-500 hover:text-primary rounded-md transition-colors shadow-sm"
              >
                <Copy class="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { FileJson, Code, Palette, Type, Copy } from 'lucide-vue-next'

export default {
  name: 'DevTools',
  components: {
    FileJson,
    Code,
    Palette,
    Type,
    Copy
  },
  data() {
    return {
      activeTool: 'json',
      tools: [
        { id: 'json', name: 'JSON Formatter', icon: 'FileJson' },
        { id: 'base64', name: 'Base64 Converter', icon: 'Code' },
        { id: 'color', name: 'Color Converter', icon: 'Palette' },
        { id: 'lorem', name: 'Lorem Ipsum', icon: 'Type' }
      ],
      // JSON Tool
      jsonInput: '',
      jsonOutput: '',
      jsonError: '',
      // Base64 Tool
      base64Input: '',
      base64Output: '',
      // Color Tool
      colorHex: '#3B82F6',
      colorRgb: { r: 59, g: 130, b: 246 },
      // Lorem Tool
      loremCount: 3,
      loremOutput: ''
    }
  },
  mounted() {
    this.generateLorem()
  },
  methods: {
    // JSON Methods
    formatJson() {
      try {
        const parsed = JSON.parse(this.jsonInput)
        this.jsonOutput = JSON.stringify(parsed, null, 2)
        this.jsonError = ''
      } catch (e) {
        this.jsonError = 'Invalid JSON: ' + e.message
        this.jsonOutput = ''
      }
    },
    minifyJson() {
      try {
        const parsed = JSON.parse(this.jsonInput)
        this.jsonOutput = JSON.stringify(parsed)
        this.jsonError = ''
      } catch (e) {
        this.jsonError = 'Invalid JSON: ' + e.message
        this.jsonOutput = ''
      }
    },
    clearJson() {
      this.jsonInput = ''
      this.jsonOutput = ''
      this.jsonError = ''
    },
    
    // Base64 Methods
    encodeBase64() {
      try {
        this.base64Output = btoa(this.base64Input)
      } catch (e) {
        this.base64Output = 'Error encoding text'
      }
    },
    decodeBase64() {
      try {
        this.base64Output = atob(this.base64Input)
      } catch (e) {
        this.base64Output = 'Error decoding Base64'
      }
    },
    clearBase64() {
      this.base64Input = ''
      this.base64Output = ''
    },

    // Color Methods
    updateFromHex() {
      let hex = this.colorHex
      if (hex.startsWith('#')) hex = hex.slice(1)
      if (hex.length === 3) hex = hex.split('').map(c => c + c).join('')
      
      if (hex.length === 6) {
        const r = parseInt(hex.substring(0, 2), 16)
        const g = parseInt(hex.substring(2, 4), 16)
        const b = parseInt(hex.substring(4, 6), 16)
        this.colorRgb = { r, g, b }
      }
    },
    updateFromRgb() {
      const { r, g, b } = this.colorRgb
      const toHex = (c) => {
        const hex = Math.max(0, Math.min(255, c)).toString(16)
        return hex.length === 1 ? '0' + hex : hex
      }
      this.colorHex = '#' + toHex(r) + toHex(g) + toHex(b)
    },

    // Lorem Methods
    generateLorem() {
      const lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
      this.loremOutput = Array(this.loremCount).fill(lorem).join('\n\n')
    },

    // Utility
    async copyToClipboard(text) {
      try {
        await navigator.clipboard.writeText(text)
        alert('Copied to clipboard!')
      } catch (err) {
        console.error('Failed to copy', err)
      }
    }
  }
}
</script>

<style scoped>
.btn-tool {
  @apply px-3 py-1.5 bg-primary text-white text-sm font-medium rounded-md hover:bg-blue-600 transition-colors;
}

.btn-tool-secondary {
  @apply px-3 py-1.5 bg-gray-100 text-gray-700 text-sm font-medium rounded-md hover:bg-gray-200 transition-colors;
}
</style>
