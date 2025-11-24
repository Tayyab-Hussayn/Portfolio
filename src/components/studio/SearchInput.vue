<template>
  <div class="relative group">
    <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
      <Search class="h-5 w-5 text-gray-400 group-focus-within:text-primary transition-colors duration-200" />
    </div>
    <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      type="text"
      class="block w-full pl-11 pr-4 py-3 bg-white border border-gray-200 rounded-xl text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all duration-200 shadow-sm hover:shadow-md"
      :placeholder="placeholder"
    />
  </div>
</template>

<script setup>
import { Search } from 'lucide-vue-next'

defineProps({
  modelValue: {
    type: String,
    default: ''
  },
  placeholder: {
    type: String,
    default: 'Search...'
  }
})

defineEmits(['update:modelValue'])
</script>
