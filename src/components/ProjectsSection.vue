<template>
  <section class="section-padding bg-white">
    <div class="container-custom">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
          Featured Projects
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Here are some of my recent projects that showcase my skills and expertise in web development
        </p>
      </div>

      <!-- Projects Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard
          v-for="project in projects"
          :key="project.id"
          :project="project"
        />
      </div>

      <!-- View All Projects Button -->
      <div class="text-center mt-16">
        <router-link to="/projects" class="btn-secondary">
          <i class="fas fa-folder-open mr-2"></i>
          View All Projects
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import ProjectCard from './ProjectCard.vue'

export default {
  name: 'ProjectsSection',
  components: {
    ProjectCard
  },
  data() {
    return {
      projects: [
        {
          id: 1,
          title: 'E-Commerce Platform',
          description: 'A full-stack e-commerce solution with user authentication, payment integration, and admin dashboard.',
          image: '/api/placeholder/400/250',
          techStack: ['Vue.js', 'Node.js', 'MongoDB', 'Stripe'],
          liveUrl: 'https://example-ecommerce.com',
          githubUrl: 'https://github.com/example/ecommerce',
          category: 'Full Stack'
        },
        {
          id: 2,
          title: 'Task Management App',
          description: 'A collaborative task management application with real-time updates and team collaboration features.',
          image: '/api/placeholder/400/250',
          techStack: ['React', 'Firebase', 'Material-UI', 'Socket.io'],
          liveUrl: 'https://example-taskapp.com',
          githubUrl: 'https://github.com/example/taskapp',
          category: 'Frontend'
        },
        {
          id: 3,
          title: 'Restaurant Website',
          description: 'A modern restaurant website with online reservation system and menu management.',
          image: '/api/placeholder/400/250',
          techStack: ['Vue.js', 'Tailwind CSS', 'PHP', 'MySQL'],
          liveUrl: 'https://example-restaurant.com',
          githubUrl: 'https://github.com/example/restaurant',
          category: 'Frontend'
        },
        {
          id: 4,
          title: 'Weather Dashboard',
          description: 'A responsive weather dashboard with location-based forecasts and interactive charts.',
          image: '/api/placeholder/400/250',
          techStack: ['JavaScript', 'Chart.js', 'OpenWeather API', 'CSS3'],
          liveUrl: 'https://example-weather.com',
          githubUrl: 'https://github.com/example/weather',
          category: 'Frontend'
        },
        {
          id: 5,
          title: 'Blog Platform',
          description: 'A content management system for bloggers with rich text editor and SEO optimization.',
          image: '/api/placeholder/400/250',
          techStack: ['Next.js', 'Prisma', 'PostgreSQL', 'Vercel'],
          liveUrl: 'https://example-blog.com',
          githubUrl: 'https://github.com/example/blog',
          category: 'Full Stack'
        },
        {
          id: 6,
          title: 'Portfolio Website',
          description: 'A responsive portfolio website showcasing creative work with smooth animations.',
          image: '/api/placeholder/400/250',
          techStack: ['Vue.js', 'GSAP', 'Tailwind CSS', 'Netlify'],
          liveUrl: 'https://example-portfolio.com',
          githubUrl: 'https://github.com/example/portfolio',
          category: 'Frontend'
        }
      ]
    }
  }
}
</script>

