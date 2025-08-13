<template>
  <div ref="containerRef" class="relative w-full max-w-6xl mx-auto py-16">
    
    <!-- SVG with connecting lines -->
    <svg class="absolute inset-0 w-full h-full" aria-hidden="true">
      <g>
        <path
          v-for="(path, i) in paths"
          :key="i"
          class="connector-path"
          :style="{ animationDelay: `${i * 100}ms` }"
          :d="path"
          stroke="hsl(var(--primary) / 0.6)"
          stroke-width="2"
          fill="none"
          stroke-linecap="round"
        />
      </g>
    </svg>
    
    <!-- Content -->
    <div class="relative z-10 flex flex-col items-center gap-8 md:gap-12 lg:gap-16">
      <!-- Header -->
      <div class="text-center">
        <h1 class="text-3xl font-bold tracking-tight text-foreground sm:text-4xl lg:text-5xl font-headline">
          My Development Workflow
        </h1>
        <p class="mt-4 text-base text-muted-foreground sm:text-lg">
          A glimpse into my creative and technical process.
        </p>
      </div>

      <!-- Frontend Skills Grid -->
      <div class="grid w-full grid-cols-2 gap-4 md:grid-cols-4 md:gap-6">
        <SkillCard
          v-for="skill in skills.frontend"
          :key="skill.id"
          :ref="el => setSkillRef(skill.id, el)"
          :icon="skill.icon"
          :title="skill.title"
          :description="skill.description"
        />
      </div>

      <!-- Central Skill -->
      <div class="w-full max-w-xs sm:max-w-sm md:max-w-md">
        <SkillCard
          ref="centralRef"
          :icon="centralSkill.icon"
          :title="centralSkill.title"
          :description="centralSkill.description"
          :is-central="true"
        />
      </div>

      <!-- Backend Skills Grid -->
      <div class="grid w-full grid-cols-2 gap-4 md:grid-cols-4 md:gap-6">
        <SkillCard
          v-for="skill in skills.backend"
          :key="skill.id"
          :ref="el => setSkillRef(skill.id, el)"
          :icon="skill.icon"
          :title="skill.title"
          :description="skill.description"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted, h } from 'vue'
import { Code, Database, Server, Settings } from 'lucide-vue-next'
import SkillCard from './SkillCard.vue'

const containerRef = ref(null)
const centralRef = ref(null)
const skillRefs = reactive({})
const paths = ref([])

let resizeObserver = null

// Icon Components - Using h() render function for custom SVG icons
const ReactIcon = () => h('svg', {
  viewBox: "-10.5 -9.45 21 18.9",
  fill: "none",
  xmlns: "http://www.w3.org/2000/svg",
  class: "h-7 w-7"
}, [
  h('circle', { cx: "0", cy: "0", r: "2.05", fill: "currentColor" }),
  h('g', { stroke: "currentColor", 'stroke-width': "1", fill: "none" }, [
    h('ellipse', { rx: "11", ry: "4.2" }),
    h('ellipse', { rx: "11", ry: "4.2", transform: "rotate(60)" }),
    h('ellipse', { rx: "11", ry: "4.2", transform: "rotate(120)" })
  ])
])

const VueIcon = () => h('svg', {
  viewBox: "0 0 256 221",
  xmlns: "http://www.w3.org/2000/svg",
  class: "h-7 w-7"
}, [
  h('path', { d: "M204.8 0H256L128 220.8L0 0h97.92L128 51.2L157.44 0h47.36Z", fill: "#41B883" }),
  h('path', { d: "m0 0l128 220.8L256 0h-51.2L128 132.48L51.2 0H0Z", fill: "#41B883" }),
  h('path', { d: "m51.2 0l76.8 133.12L204.8 0h-47.36L128 51.2L97.92 0H51.2Z", fill: "#35495E" })
])

const TailwindIcon = () => h('svg', {
  viewBox: "0 0 512 512",
  xmlns: "http://www.w3.org/2000/svg",
  class: "h-6 w-6"
}, [
  h('path', { 
    fill: "#38bdf8", 
    d: "M154.2 221.3c-6.8-11.8-12.8-24.3-17.4-37.7-4.3-12.8-8-26-10.9-39.7-2.2-10.4-3.4-21-3.4-31.9 0-22.7 6.3-43.9 18.9-63.5 12.5-19.5 30.6-33.8 54.2-42.7C220.2-1.9 244.5 0 266.3 7.6c21.8 7.6 40.2 20.6 55.1 39 14.9 18.4 23.4 40.8 25.4 67.2 2 26.3-2.3 52.4-12.9 78.2-10.6 25.8-25.2 49.3-43.7 69.8-18.6 20.4-40.4 36.6-65.4 48.4-25 11.9-52 18.4-80.9 19.6-4.2.2-8.5.2-12.7 0-13.1-.7-26.2-2.3-38.6-5-12.5-2.7-24.4-6.8-35.6-12.4-11.2-5.6-21.4-12.8-30.5-21.8-9.1-9-16.8-19.4-22.9-31.2-6.1-11.8-10.4-24.8-12.7-38.6-2-12-2.3-24.3-1-36.9.7-6.8 1.9-13.6 3.6-20.3 3.4-13.4 8.7-26.4 15.8-38.6 7.1-12.2 15.8-23.4 25.8-33.4 10-10 21.5-18.5 34.3-25.4 12.8-6.8 26.8-11.9 41.8-14.9 15-3 30.6-3.6 46.1-1.6 15.5 2 30.7 6.4 44.9 13.1 14.2 6.8 27.2 16 38.6 27.5 11.4 11.5 21 24.8 28.5 39.7" 
  }),
  h('path', { 
    fill: "#38bdf8", 
    d: "M357.8 290.7c6.8 11.8 12.8 24.3 17.4 37.7 4.3 12.8 8 26 10.9 39.7 2.2 10.4 3.4 21 3.4 31.9 0 22.7-6.3 43.9-18.9 63.5-12.5 19.5-30.6 33.8-54.2 42.7-23.6 8.9-47.9 10.5-71.7 4.9-21.8-7.6-40.2-20.6-55.1-39-14.9-18.4-23.4-40.8-25.4-67.2-2-26.3 2.3-52.4 12.9-78.2 10.6-25.8 25.2-49.3 43.7-69.8 18.6-20.4 40.4-36.6 65.4-48.4 25-11.9 52-18.4 80.9-19.6 4.2-.2 8.5-.2 12.7 0 13.1.7 26.2 2.3 38.6 5 12.5 2.7 24.4 6.8 35.6 12.4 11.2 5.6 21.4 12.8 30.5 21.8 9.1 9 16.8 19.4 22.9 31.2 6.1 11.8 10.4 24.8 12.7 38.6 2 12 2.3 24.3 1 36.9-.7 6.8-1.9 13.6-3.6 20.3-3.4 13.4-8.7 26.4-15.8 38.6-7.1 12.2-15.8 23.4-25.8 33.4-10 10-21.5 18.5-34.3 25.4-12.8 6.8-26.8 11.9-41.8 14.9-15 3-30.6 3.6-46.1 1.6-15.5-2-30.7-6.4-44.9-13.1-14.2-6.8-27.2-16-38.6-27.5-11.4-11.5-21-24.8-28.5-39.7" 
  })
])

const NodeIcon = () => h('svg', {
  viewBox: "0 0 256 256",
  xmlns: "http://www.w3.org/2000/svg",
  class: "h-7 w-7"
}, [
  h('path', { 
    d: "M225.2,117.3l-81-63.5c-8.6-6.8-21-6.8-29.6,0l-81,63.5c-7.4,5.8-11.7,14.6-11.7,24v1.8c0,11.3,5.6,21.6,14.8,27.7l81,50.7c9.3,5.8,20.9,5.8,30.2,0l81-50.7c9.2-6.1,14.8-16.4,14.8-27.7v-1.8C236.9,131.9,232.6,123.1,225.2,117.3z", 
    fill: "#8CC84B" 
  })
])

// Skills data - exact same as Next.js version
const skills = reactive({
  frontend: [
    { id: "fe-1", icon: ReactIcon, title: "Declarative UI Libraries", description: "Building dynamic user interfaces with React." },
    { id: "fe-2", icon: VueIcon, title: "Progressive JS Frameworks", description: "Creating adaptable applications with Vue.js." },
    { id: "fe-3", icon: TailwindIcon, title: "Utility-First CSS", description: "Rapidly styling with Tailwind CSS." },
    { id: "fe-4", icon: () => h(Settings, { class: "h-7 w-7" }), title: "Full-Stack React Frameworks", description: "Leveraging Next.js for performance and features." },
  ],
  backend: [
    { id: "be-1", icon: NodeIcon, title: "Server-Side Runtimes", description: "Using Node.js for scalable backends." },
    { id: "be-2", icon: () => h(Code, { class: "h-7 w-7" }), title: "Versatile Scripting Languages", description: "Employing Python for data and automation." },
    { id: "be-3", icon: () => h(Database, { class: "h-7 w-7" }), title: "NoSQL Database Management", description: "Structuring data with MongoDB." },
    { id: "be-4", icon: () => h(Server, { class: "h-7 w-7" }), title: "API & Business Logic", description: "Crafting robust server-side applications." },
  ]
})

const centralSkill = reactive({
  id: "central",
  icon: () => h(Settings, { class: "h-8 w-8" }),
  title: "Core Tech Stack",
  description: "Synergizing technologies for robust applications."
})

// Set skill ref function
const setSkillRef = (id, el) => {
  if (el && el.skillCardRef) {
    skillRefs[id] = el.skillCardRef
  }
}

// Calculate paths function - exact same logic as Next.js version
const calculatePaths = () => {
  if (!containerRef.value || !centralRef.value || !centralRef.value.skillCardRef) return
  
  const containerRect = containerRef.value.getBoundingClientRect()
  const centralRect = centralRef.value.skillCardRef.getBoundingClientRect()

  const newPaths = []

  const allSkills = [...skills.frontend, ...skills.backend]
  allSkills.forEach(skill => {
    const skillRef = skillRefs[skill.id]
    if (!skillRef) return
    
    const skillRect = skillRef.getBoundingClientRect()
    const isFrontend = skills.frontend.some(s => s.id === skill.id)

    const startX = (skillRect.left - containerRect.left) + skillRect.width / 2
    const startY = isFrontend 
      ? (skillRect.top - containerRect.top) + skillRect.height
      : (skillRect.top - containerRect.top)
    
    const endX = (centralRect.left - containerRect.left) + centralRect.width / 2
    const endY = isFrontend
      ? (centralRect.top - containerRect.top)
      : (centralRect.top - containerRect.top) + centralRect.height
    
    const c1y = startY + (endY - startY) * 0.5
    const c2y = endY - (endY - startY) * 0.5

    const path = `M ${startX} ${startY} C ${startX} ${c1y}, ${endX} ${c2y}, ${endX} ${endY}`
    newPaths.push(path)
  })
  
  paths.value = newPaths
}

onMounted(() => {
  // Calculate paths after a short delay to ensure all refs are set
  setTimeout(() => {
    calculatePaths()
    if (containerRef.value) {
      resizeObserver = new ResizeObserver(calculatePaths)
      resizeObserver.observe(containerRef.value)
    }
  }, 100)
})

onUnmounted(() => {
  if (resizeObserver) {
    resizeObserver.disconnect()
  }
})
</script>

<style scoped>
.connector-path {
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  animation: draw-line 1.5s ease-out forwards;
}

@keyframes draw-line {
  to {
    stroke-dashoffset: 0;
  }
}
</style>
