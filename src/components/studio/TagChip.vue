<template>
  <span 
    class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-600 hover:bg-gray-200 transition-colors duration-200 cursor-default"
  >
    <slot></slot>
  </span>
</template>

<script setup>
defineOptions({
  name: 'TagChip'
})
</script>
