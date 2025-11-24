<template>
  <div class="min-h-screen pt-16 bg-gray-50/50">
    <!-- Hero Section -->
    <section class="bg-white border-b border-gray-100 relative overflow-hidden">
      <!-- Decorative Background Elements -->
      <div class="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
        <div class="absolute -top-24 -right-24 w-96 h-96 bg-blue-50 rounded-full blur-3xl opacity-50"></div>
        <div class="absolute top-1/2 -left-24 w-72 h-72 bg-purple-50 rounded-full blur-3xl opacity-50"></div>
      </div>

      <div class="container-custom py-20 md:py-32 text-center relative z-10">
        <div class="inline-flex items-center px-3 py-1 rounded-full bg-blue-50 text-primary text-xs font-medium mb-6 border border-blue-100">
          <span class="flex h-2 w-2 rounded-full bg-primary mr-2"></span>
          Studio Resources
        </div>
        
        <h1 class="text-4xl md:text-6xl font-bold text-gray-900 mb-6 tracking-tight leading-tight">
          AI Prompts for <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-600 to-purple-600">Developers</span>
        </h1>
        
        <p class="text-xl text-gray-500 max-w-2xl mx-auto mb-12 leading-relaxed font-light">
          A curated collection of high-quality prompts to boost your coding productivity, debugging, and system design. I actively used these prompts in my daily life coding and other tasks.
        </p>
        
        <!-- Search Bar -->
        <div class="max-w-2xl mx-auto">
          <SearchInput 
            v-model="searchQuery" 
            placeholder="Search prompts (e.g., 'React', 'Debug', 'Refactor')..." 
          />
        </div>
      </div>
    </section>

    <!-- Prompts Grid -->
    <section class="container-custom py-16 md:py-24">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <PromptCard 
          v-for="prompt in filteredPrompts" 
          :key="prompt.id" 
          :prompt="prompt" 
        />
      </div>

      <!-- Empty State -->
      <div v-if="filteredPrompts.length === 0" class="text-center py-24">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gray-100 rounded-full mb-6 text-gray-400">
          <Search class="w-8 h-8" />
        </div>
        <h3 class="text-xl font-bold text-gray-900 mb-2">No prompts found</h3>
        <p class="text-gray-500 max-w-md mx-auto">
          We couldn't find any prompts matching your search. Try using different keywords or browse the collection.
        </p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { Search } from 'lucide-vue-next'
import SearchInput from '../../components/studio/SearchInput.vue'
import PromptCard from '../../components/studio/PromptCard.vue'

defineOptions({
  name: 'Prompts'
})

const searchQuery = ref('')

const prompts = ref([
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
])

const filteredPrompts = computed(() => {
  if (!searchQuery.value) return prompts.value
  const query = searchQuery.value.toLowerCase()
  return prompts.value.filter(prompt => 
    prompt.title.toLowerCase().includes(query) || 
    prompt.description.toLowerCase().includes(query) ||
    prompt.tags.some(tag => tag.toLowerCase().includes(query))
  )
})
</script>
