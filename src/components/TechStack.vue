<template>
  <section class="bg-gray-900 text-white min-h-screen py-20">
    <div class="max-w-6xl mx-auto px-6">
      <!-- Header -->
      <div class="text-center mb-20">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">
          <span class="text-blue-400">The complete development platform.</span>
        </h1>
        <h2 class="text-2xl md:text-3xl font-light text-gray-300">
          Built for developers. Powered by innovation.
        </h2>
      </div>

      <!-- Workflow Diagram -->
      <div class="relative">
        <!-- Top Row - Frontend Technologies -->
        <div class="flex justify-center gap-8 mb-16">
          <div 
            v-for="tech in frontendTechs" 
            :key="tech"
            class="workflow-box"
          >
            {{ tech }}
          </div>
        </div>

        <!-- Connection Lines Container -->
        <div class="absolute inset-0 pointer-events-none">
          <!-- SVG for all connection lines -->
          <svg class="w-full h-full" style="position: absolute; top: 0; left: 0;">
            <defs>
              <!-- Gray gradient for top connections -->
              <linearGradient id="topGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#6B7280"/>
                <stop offset="100%" style="stop-color:#9CA3AF"/>
              </linearGradient>
              <!-- Blue gradient for bottom connections -->
              <linearGradient id="bottomGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:#1E40AF"/>
                <stop offset="100%" style="stop-color:#3B82F6"/>
              </linearGradient>
            </defs>
            
            <!-- Top connections (Frontend to Center) -->
            <!-- Vertical lines down from each frontend box -->
            <line x1="20%" y1="15%" x2="20%" y2="30%" stroke="url(#topGrad)" stroke-width="2"/>
            <line x1="40%" y1="15%" x2="40%" y2="25%" stroke="url(#topGrad)" stroke-width="2"/>
            <line x1="60%" y1="15%" x2="60%" y2="25%" stroke="url(#topGrad)" stroke-width="2"/>
            <line x1="80%" y1="15%" x2="80%" y2="30%" stroke="url(#topGrad)" stroke-width="2"/>
            
            <!-- Horizontal connecting lines -->
            <line x1="20%" y1="30%" x2="80%" y2="30%" stroke="url(#topGrad)" stroke-width="2"/>
            <line x1="40%" y1="25%" x2="60%" y2="25%" stroke="url(#topGrad)" stroke-width="2"/>
            
            <!-- Center connection -->
            <line x1="50%" y1="25%" x2="50%" y2="30%" stroke="url(#topGrad)" stroke-width="2"/>
            <line x1="50%" y1="30%" x2="50%" y2="40%" stroke="url(#topGrad)" stroke-width="2" stroke-dasharray="5,5"/>

            <!-- Bottom connections (Center to Backend) -->
            <!-- Center down -->
            <line x1="50%" y1="60%" x2="50%" y2="70%" stroke="url(#bottomGrad)" stroke-width="3"/>
            <!-- Horizontal distribution -->
            <line x1="15%" y1="70%" x2="85%" y2="70%" stroke="url(#bottomGrad)" stroke-width="3"/>
            <!-- Vertical lines to backend boxes -->
            <line x1="22.5%" y1="70%" x2="22.5%" y2="85%" stroke="url(#bottomGrad)" stroke-width="3"/>
            <line x1="40%" y1="70%" x2="40%" y2="85%" stroke="url(#bottomGrad)" stroke-width="3"/>
            <line x1="60%" y1="70%" x2="60%" y2="85%" stroke="url(#bottomGrad)" stroke-width="3"/>
            <line x1="77.5%" y1="70%" x2="77.5%" y2="85%" stroke="url(#bottomGrad)" stroke-width="3"/>
          </svg>
        </div>

        <!-- Center Box -->
        <div class="flex justify-center mb-16" style="position: relative; z-index: 10;">
          <div class="workflow-box center-box">
            <div class="flex flex-col items-center">
              <div class="w-8 h-8 mb-3 text-blue-400">
                <svg fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M3 4a1 1 0 011-1h4a1 1 0 010 2H6.414l2.293 2.293a1 1 0 01-1.414 1.414L5 6.414V8a1 1 0 01-2 0V4zm9 1a1 1 0 010-2h4a1 1 0 011 1v4a1 1 0 01-2 0V6.414l-2.293 2.293a1 1 0 11-1.414-1.414L13.586 5H12zm-9 7a1 1 0 012 0v1.586l2.293-2.293a1 1 0 111.414 1.414L6.414 15H8a1 1 0 010 2H4a1 1 0 01-1-1v-4zm13-1a1 1 0 011 1v4a1 1 0 01-1 1h-4a1 1 0 010-2h1.586l-2.293-2.293a1 1 0 111.414-1.414L15 13.586V12a1 1 0 011-1z" clip-rule="evenodd"/>
                </svg>
              </div>
              <span class="text-xl font-bold">Core Tech Stack</span>
            </div>
          </div>
        </div>

        <!-- Bottom Row - Backend Technologies -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          <div 
            v-for="tech in backendTechs" 
            :key="tech.name"
            class="workflow-box backend-box"
          >
            <div class="text-left">
              <h3 class="text-lg font-semibold text-blue-400 mb-2">{{ tech.name }}</h3>
              <p class="text-sm text-gray-400 leading-relaxed">{{ tech.description }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TechWorkflow',
  data() {
    return {
      frontendTechs: [
        'Vue.js',
        'React',
        'JavaScript (ES6+)',
        'Tailwind CSS'
      ],
      backendTechs: [
        {
          name: 'Node.js & Express',
          description: 'For building fast, scalable REST APIs and server-side applications.'
        },
        {
          name: 'Python & Django',
          description: 'For complex web applications and data processing workflows.'
        },
        {
          name: 'Database Architecture',
          description: 'Using MongoDB and PostgreSQL for flexible, scalable data storage.'
        },
        {
          name: 'Server-Side Logic',
          description: 'Crafting secure and efficient backend systems and microservices.'
        }
      ]
    }
  }
}
</script>

<style scoped>
/* Workflow boxes */
.workflow-box {
  background: rgba(31, 41, 55, 0.8);
  border: 1px solid rgba(75, 85, 99, 0.6);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  position: relative;
  z-index: 5;
}

.workflow-box:hover {
  border-color: rgba(59, 130, 246, 0.8);
  transform: translateY(-4px);
  box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
  background: rgba(31, 41, 55, 0.95);
}

/* Center box styling */
.center-box {
  background: linear-gradient(135deg, rgba(30, 64, 175, 0.3), rgba(59, 130, 246, 0.2));
  border: 2px solid rgba(59, 130, 246, 0.8);
  box-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
  min-width: 250px;
}

/* Backend boxes */
.backend-box {
  min-height: 140px;
  display: flex;
  align-items: flex-start;
}

/* SVG lines */
svg {
  overflow: visible;
}

svg line {
  opacity: 0.8;
}

svg line:hover {
  opacity: 1;
}

/* Responsive adjustments */
@media (max-width: 1024px) {
  .workflow-box {
    padding: 1rem;
    font-size: 0.9rem;
  }
  
  /* Hide connection lines on smaller screens */
  svg {
    display: none;
  }
}

@media (max-width: 768px) {
  .flex.justify-center.gap-8 {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }
  
  .workflow-box {
    width: 100%;
    max-width: 300px;
  }
  
  .center-box {
    min-width: 200px;
  }
}

/* Animation for smooth appearance */
.workflow-box {
  animation: fadeInUp 0.6s ease-out forwards;
}

.workflow-box:nth-child(1) { animation-delay: 0.1s; }
.workflow-box:nth-child(2) { animation-delay: 0.2s; }
.workflow-box:nth-child(3) { animation-delay: 0.3s; }
.workflow-box:nth-child(4) { animation-delay: 0.4s; }

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
