<template>
  <section class="bg-gray-900 text-white section-padding">
    <div class="container-custom text-center">
      <h2 class="text-3xl md:text-4xl font-bold mb-4">My Development Workflow</h2>
      <p class="text-lg text-gray-400 mb-16 max-w-2xl mx-auto">
        From crafting intuitive interfaces to building robust server-side logic.
      </p>

      <div class="workflow-grid">
        <!-- Top Row: Frontend -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8" id="frontend-row">
          <div v-for="skill in frontendSkills" :key="skill.name" class="workflow-item">
            <div class="workflow-box">
              <span class="text-lg font-semibold">{{ skill.name }}</span>
            </div>
          </div>
        </div>

        <!-- Connector Lines to Center -->
        <div class="relative h-16">
          <svg class="absolute inset-0 w-full h-full" viewBox="0 0 100 16" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="connector-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#4A5568;" />
                <stop offset="100%" style="stop-color:#6B7280;" />
              </linearGradient>
            </defs>
            <!-- Vertical lines from frontend boxes -->
            <line x1="12.5" y1="0" x2="12.5" y2="16" stroke="url(#connector-gradient)" stroke-width="0.3"/>
            <line x1="37.5" y1="0" x2="37.5" y2="8" stroke="url(#connector-gradient)" stroke-width="0.3"/>
            <line x1="62.5" y1="0" x2="62.5" y2="8" stroke="url(#connector-gradient)" stroke-width="0.3"/>
            <line x1="87.5" y1="0" x2="87.5" y2="16" stroke="url(#connector-gradient)" stroke-width="0.3"/>
            <!-- Horizontal connecting line -->
            <line x1="12.5" y1="16" x2="87.5" y2="16" stroke="url(#connector-gradient)" stroke-width="0.3"/>
            <!-- Center connecting line -->
            <line x1="50" y1="8" x2="50" y2="16" stroke="url(#connector-gradient)" stroke-width="0.3" stroke-dasharray="1 1"/>
          </svg>
        </div>

        <!-- Central Box -->
        <div class="flex justify-center items-center" id="center-box">
          <div class="workflow-box central-box bg-secondary">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 mb-3 mx-auto text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
            </svg>
            <span class="text-xl font-bold">Core Tech Stack</span>
          </div>
        </div>

        <!-- Connector Lines to Bottom -->
        <div class="relative h-16">
          <svg class="absolute inset-0 w-full h-full" viewBox="0 0 100 16" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="blue-gradient" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#1E40AF;" />
                <stop offset="100%" style="stop-color:#3B82F6;" />
              </linearGradient>
            </defs>
            <!-- Center to horizontal line -->
            <line x1="50" y1="0" x2="50" y2="8" stroke="url(#blue-gradient)" stroke-width="0.4"/>
            <!-- Main horizontal line -->
            <line x1="12.5" y1="8" x2="87.5" y2="8" stroke="url(#blue-gradient)" stroke-width="0.4"/>
            <!-- Vertical lines to backend boxes -->
            <line x1="12.5" y1="8" x2="12.5" y2="16" stroke="url(#blue-gradient)" stroke-width="0.4"/>
            <line x1="37.5" y1="8" x2="37.5" y2="16" stroke="url(#blue-gradient)" stroke-width="0.4"/>
            <line x1="62.5" y1="8" x2="62.5" y2="16" stroke="url(#blue-gradient)" stroke-width="0.4"/>
            <line x1="87.5" y1="8" x2="87.5" y2="16" stroke="url(#blue-gradient)" stroke-width="0.4"/>
          </svg>
        </div>

        <!-- Bottom Row: Backend -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8" id="backend-row">
          <div v-for="skill in backendSkills" :key="skill.name" class="workflow-item">
            <div class="workflow-box detailed-box">
              <h4 class="text-lg font-semibold text-primary mb-2">{{ skill.name }}</h4>
              <p class="text-gray-400 text-sm">{{ skill.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TechStack',
  setup() {
    const frontendSkills = [
      { name: 'Vue.js' },
      { name: 'React' },
      { name: 'JavaScript (ES6+)' },
      { name: 'Tailwind CSS' },
    ];

    const backendSkills = [
      {
        name: 'Node.js & Express',
        description: 'For building fast, scalable REST APIs.',
      },
      {
        name: 'Python & Django',
        description: 'For complex applications and data processing.',
      },
      {
        name: 'Database Architecture',
        description: 'Using MongoDB for flexible, scalable data storage.',
      },
      {
        name: 'Server-Side Logic',
        description: 'Crafting secure and efficient backend systems.',
      },
    ];

    return {
      frontendSkills,
      backendSkills,
    };
  },
};
</script>

<style scoped>
.workflow-box {
  @apply bg-gray-800 border border-gray-700 rounded-xl p-6 h-full transition-all duration-300;
}

.workflow-item:hover .workflow-box {
  @apply border-primary transform -translate-y-2 shadow-lg shadow-primary/20;
}

.central-box {
  @apply border-primary shadow-2xl shadow-primary/30 max-w-xs mx-auto;
}

.detailed-box {
  @apply flex flex-col justify-start text-left;
}

/* Ensure proper sizing for connector containers */
.relative.h-16 svg {
  overflow: visible;
}

/* Hiding SVG on mobile for a cleaner look */
@media (max-width: 767px) {
  .relative.h-16 {
    display: none;
  }
  #center-box {
    margin-top: 2rem;
    margin-bottom: 2rem;
  }
}
</style>
