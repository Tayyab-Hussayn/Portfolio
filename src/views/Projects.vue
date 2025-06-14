<template>
  <div class="projects-page">
    <!-- Page Header -->
    <section class="page-header">
      <div class="container-custom">
        <div class="text-center">
          <h1 class="text-4xl md:text-5xl font-bold text-white mb-6">
            My Projects
          </h1>
          <p class="text-xl text-blue-100 max-w-3xl mx-auto">
            Explore my portfolio of web development projects, showcasing various technologies and creative solutions.
          </p>
        </div>
      </div>
    </section>

    <!-- Projects Grid -->
    <section class="section-padding bg-gray-50">
      <div class="container-custom">
        <!-- Filter Buttons -->
        <div class="flex flex-wrap justify-center gap-4 mb-12">
          <button
            v-for="filter in filters"
            :key="filter"
            @click="activeFilter = filter"
            class="filter-btn"
            :class="{ 'filter-btn-active': activeFilter === filter }"
          >
            {{ filter }}
          </button>
        </div>

        <!-- Projects Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <ProjectCard
            v-for="project in filteredProjects"
            :key="project.id"
            :project="project"
          />
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import ProjectCard from '../components/ProjectCard.vue'

export default {
  name: 'Projects',
  components: {
    ProjectCard
  },
  data() {
    return {
      activeFilter: 'All',
      filters: ['All', 'Frontend', 'Full Stack', 'Mobile'],
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
  },
  computed: {
    filteredProjects() {
      if (this.activeFilter === 'All') {
        return this.projects
      }
      return this.projects.filter(project => project.category === this.activeFilter)
    }
  }
}
</script>

<style scoped>
.page-header {
  @apply bg-gradient-to-br from-blue-600 via-purple-600 to-blue-800 section-padding;
  padding-top: 8rem; /* Account for fixed navbar */
}

.filter-btn {
  @apply px-6 py-3 rounded-full border-2 border-primary text-primary hover:bg-primary hover:text-white transition-all duration-300 font-medium;
}

.filter-btn-active {
  @apply bg-primary text-white;
}
</style>

