<template>
  <div ref="skillCardRef" :class="className">
    <div
      :class="cn(
        'w-full h-full flex flex-col justify-center items-center text-center shadow-lg hover:shadow-primary/20 transition-all duration-300 ease-in-out transform hover:-translate-y-1 rounded-lg border bg-card text-card-foreground shadow-sm',
        isCentral
          ? 'border-primary border-2 bg-card scale-105'
          : 'border'
      )"
    >
      <div class="p-4 pb-2 md:p-6 md:pb-2 flex flex-col space-y-1.5">
        <div
          :class="cn(
            'mx-auto flex h-12 w-12 items-center justify-center rounded-full',
            isCentral ? 'bg-primary text-primary-foreground' : 'bg-primary/10 text-primary'
          )"
        >
          <component :is="icon" />
        </div>
      </div>
      <div class="p-4 pt-2 md:p-6 md:pt-2">
        <div class="text-sm font-bold md:text-base mb-1 text-2xl font-semibold leading-none tracking-tight">
          {{ title }}
        </div>
        <div class="text-xs md:text-sm text-sm text-muted-foreground">
          {{ description }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { cn } from '../utils/cn.js'

defineProps({
  icon: {
    type: [Object, Function, String],
    required: true
  },
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  className: {
    type: String,
    default: ''
  },
  isCentral: {
    type: Boolean,
    default: false
  }
})

const skillCardRef = ref(null)

defineExpose({
  skillCardRef
})
</script>
