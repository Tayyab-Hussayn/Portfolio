<template>
  <div class="min-h-screen pt-16 bg-gray-50">
    <!-- Hero Section -->
    <section class="bg-white border-b border-gray-100">
      <div class="container-custom py-16 md:py-24 text-center">
        <h1 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
          AI Prompts for <span class="text-primary">Developers</span>
        </h1>
        <p class="text-xl text-gray-600 max-w-2xl mx-auto mb-10">
          A curated collection of high-quality prompts to boost your coding productivity, debugging, and system design.
        </p>
        
        <!-- Search Bar -->
        <div class="max-w-xl mx-auto relative">
          <input 
            v-model="searchQuery"
            type="text" 
            placeholder="Search prompts (e.g., 'React', 'Debug', 'Refactor')..."
            class="w-full pl-12 pr-4 py-4 rounded-xl border border-gray-200 shadow-sm focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all outline-none text-lg"
          >
          <Search class="absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 w-5 h-5" />
        </div>
      </div>
    </section>

    <!-- Prompts Grid -->
    <section class="container-custom py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="prompt in filteredPrompts" 
          :key="prompt.id"
          class="bg-white rounded-xl p-6 shadow-sm border border-gray-100 hover:shadow-md transition-all duration-300 group"
        >
          <div class="flex items-start justify-between mb-4">
            <div class="p-2 bg-blue-50 text-primary rounded-lg">
              <component :is="prompt.icon" class="w-6 h-6" />
            </div>
            <button 
              @click="copyPrompt(prompt.content)"
              class="text-gray-400 hover:text-primary transition-colors"
              title="Copy Prompt"
            >
              <Copy class="w-5 h-5" />
            </button>
          </div>
          
          <h3 class="text-xl font-bold text-gray-900 mb-2 group-hover:text-primary transition-colors">
            {{ prompt.title }}
          </h3>
          <p class="text-gray-600 mb-4 line-clamp-3">
            {{ prompt.description }}
          </p>
          
          <div class="flex flex-wrap gap-2 mt-auto">
            <span 
              v-for="tag in prompt.tags" 
              :key="tag"
              class="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-md font-medium"
            >
              {{ tag }}
            </span>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="filteredPrompts.length === 0" class="text-center py-12">
        <div class="inline-block p-4 bg-gray-100 rounded-full mb-4 text-gray-400">
          <Search class="w-8 h-8" />
        </div>
        <h3 class="text-lg font-semibold text-gray-900">No prompts found</h3>
        <p class="text-gray-500">Try adjusting your search terms.</p>
      </div>
    </section>
  </div>
</template>

<script>
import { Search, Copy, CodeXml, Bug, Zap, Layers, Rocket, BookOpen, Code } from 'lucide-vue-next'

export default {
  name: 'Prompts',
  components: {
    Search,
    Copy,
    CodeXml,
    Bug,
    Zap,
    Layers,
    Rocket,
    BookOpen,
    Code
  },
  data() {
    return {
      searchQuery: '',
      prompts: [
        {
          id: 0,
          title: 'Project Initiation Expert',
          description: 'A ruthless, plan-first meta-prompt that forces the AI to act as an elite expert, critique your ideas, and generate a todo list before working.',
          content: "You are now operating as an elite, top-tier expert in [INSERT ROLE/DOMAIN]. Your directive is to assist me with: '[INSERT PROJECT DETAILS]'.\n\n**Operating Rules:**\n1. **Zero Tolerance for Mediocrity:** You are forbidden from sugarcoating. If any part of my idea, logic, or approach is amateurish, inefficient, or technically flawed, you must label it as 'trash' and provide a brutal, evidence-based critique. Then, dictate the correct, professional course of action.\n2. **Plan-First Architecture:** You will NEVER generate final output (code, design, text) without a blueprint. Your first response must always be a detailed, hypothetical 'Todo List' that breaks the project down into granular, logical steps.\n3. **Maximum Compute:** Utilize your full training and reasoning capabilities. Do not simplify complex topics. Assume I am a peer who demands the highest standard of work.\n\n**Your First Task:**\nAnalyze the project details provided above. Critique them ruthlessly. Then, generate the 'Imaginary Todo List' that we will follow to execute this project perfectly. Await my approval of the plan before generating any deliverables.",
          icon: 'Rocket',
          tags: ['Meta Prompt', 'Planning', 'Project Initiation']
        },
        {
          id: 1,
          title: 'Code Refactoring Expert',
          description: 'Act as a senior software engineer. Review the following code for readability, performance, and adherence to SOLID principles. Suggest improvements and explain why.',
          content: 'Act as a senior software engineer. Review the following code for readability, performance, and adherence to SOLID principles. Suggest improvements and explain why:\n\n[INSERT CODE HERE]',
          icon: 'CodeXml',
          tags: ['Refactoring', 'Clean Code', 'Best Practices']
        },
        {
          id: 2,
          title: 'Bug Hunter',
          description: 'Analyze the provided error log and code snippet. Identify the root cause of the bug and propose a fix with explanation.',
          content: 'Analyze the provided error log and code snippet. Identify the root cause of the bug and propose a fix with explanation.\n\nError Log:\n[INSERT LOG]\n\nCode:\n[INSERT CODE]',
          icon: 'Bug',
          tags: ['Debugging', 'Troubleshooting']
        },
        {
          id: 3,
          title: 'Unit Test Generator',
          description: 'Generate comprehensive unit tests for the following function using [Framework Name]. Include edge cases and happy paths.',
          content: 'Generate comprehensive unit tests for the following function using [Framework Name]. Include edge cases and happy paths:\n\n[INSERT FUNCTION]',
          icon: 'Zap',
          tags: ['Testing', 'QA', 'Automation']
        },
        {
          id: 4,
          title: 'System Architecture Designer',
          description: 'Design a scalable architecture for a [System Type] that handles [Load Requirement]. Outline the key components, database schema, and technologies.',
          content: 'Design a scalable architecture for a [System Type] that handles [Load Requirement]. Outline the key components, database schema, and technologies.',
          icon: 'Layers',
          tags: ['Architecture', 'System Design', 'Scalability']
        },
        {
          id: 5,
          title: 'Documentation Writer',
          description: 'Write clear and concise documentation for the following API endpoint, including request parameters, response format, and example usage.',
          content: 'Write clear and concise documentation for the following API endpoint, including request parameters, response format, and example usage:\n\n[INSERT API DETAILS]',
          icon: 'BookOpen',
          tags: ['Documentation', 'API', 'Technical Writing']
        },
        {
          id: 6,
          title: 'Regex Master',
          description: 'Create a regular expression to match [Pattern Description]. Explain how the regex works step-by-step.',
          content: 'Create a regular expression to match [Pattern Description]. Explain how the regex works step-by-step.',
          icon: 'Code',
          tags: ['Regex', 'Utilities']
        }
      ]
    }
  },
  computed: {
    filteredPrompts() {
      if (!this.searchQuery) return this.prompts
      const query = this.searchQuery.toLowerCase()
      return this.prompts.filter(prompt => 
        prompt.title.toLowerCase().includes(query) || 
        prompt.description.toLowerCase().includes(query) ||
        prompt.tags.some(tag => tag.toLowerCase().includes(query))
      )
    }
  },
  methods: {
    async copyPrompt(content) {
      try {
        await navigator.clipboard.writeText(content)
      } catch (err) {
        console.error('Failed to copy:', err)
      }
    }
  }
}
</script>
