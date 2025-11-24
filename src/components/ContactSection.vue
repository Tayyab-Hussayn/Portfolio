<template>
  <section class="section-padding bg-gray-50">
    <div class="container-custom">
      <!-- Section Header -->
      <div class="text-center mb-16">
        <h2 class="text-4xl md:text-5xl font-bold text-gray-900 mb-6">
          Contact Us
        </h2>
        <p class="text-xl text-gray-600 max-w-3xl mx-auto">
          Ready to start your project? Get in touch and let's discuss how we can bring your ideas to life.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
        <!-- Contact Information -->
        <div class="space-y-8">
          <div>
            <h3 class="text-2xl font-semibold text-gray-900 mb-6">
              Let's Connect
            </h3>
            <p class="text-gray-600 mb-8">
              I'm always excited to work on new projects and collaborate with amazing people. 
              Whether you have a question, a project idea, or just want to say hello, feel free to reach out!
            </p>
          </div>

          <!-- Contact Details -->
          <div class="space-y-6">
            <div class="flex items-center space-x-4">
              <div class="w-12 h-12 rounded-full flex items-center justify-center text-xl bg-blue-100 text-blue-600">
                <i class="fas fa-envelope"></i>
              </div>
              <div>
                <h4 class="font-medium text-gray-900">Email</h4>
                <p class="text-gray-600">tayyabhussayn@gmail.com</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <div class="w-12 h-12 rounded-full flex items-center justify-center text-xl bg-green-100 text-green-600">
                <i class="fas fa-phone"></i>
              </div>
              <div>
                <h4 class="font-medium text-gray-900">Phone</h4>
		<p class="text-gray-600">+92 321 3875210</p>
              </div>
            </div>

            <div class="flex items-center space-x-4">
              <div class="w-12 h-12 rounded-full flex items-center justify-center text-xl bg-purple-100 text-purple-600">
                <i class="fas fa-map-marker-alt"></i>
              </div>
              <div>
                <h4 class="font-medium text-gray-900">Location</h4>
                <p class="text-gray-600">Johar Town, Lahore</p>
              </div>
            </div>
          </div>

          <!-- Social Links -->
          <div>
            <h4 class="font-medium text-gray-900 mb-4">Follow Me</h4>
            <div class="flex space-x-4">
              <a href="https://github.com/tayyab-hussayn" target="_blank" class="w-10 h-10 bg-gray-100 hover:bg-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-110">
                <i class="fab fa-github"></i>
              </a>
              <a href="https://linkedin.com" target="_blank" class="w-10 h-10 bg-gray-100 hover:bg-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-110">
                <i class="fab fa-linkedin"></i>
              </a>
              <a href="https://twitter.com" target="_blank" class="w-10 h-10 bg-gray-100 hover:bg-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-110">
                <i class="fab fa-twitter"></i>
              </a>
              <a href="https://dribbble.com" target="_blank" class="w-10 h-10 bg-gray-100 hover:bg-primary text-gray-600 hover:text-white rounded-full flex items-center justify-center transition-all duration-300 transform hover:scale-110">
                <i class="fab fa-dribbble"></i>
              </a>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="bg-white rounded-2xl shadow-xl p-8">
          <form @submit.prevent="submitForm" class="space-y-6">
            <!-- Success Message -->
            <div v-if="showSuccess" class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg flex items-center">
              <i class="fas fa-check-circle mr-2"></i>
              Thank you! Your message has been sent successfully.
            </div>

            <!-- Name Field -->
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                Full Name *
              </label>
              <input
                id="name"
                v-model="form.name"
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition-all duration-200"
                :class="{ 'border-red-500': errors.name }"
                placeholder="Enter your full name"
              >
              <p v-if="errors.name" class="text-red-500 text-sm mt-1">{{ errors.name }}</p>
            </div>

            <!-- Email Field -->
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                Email Address *
              </label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition-all duration-200"
                :class="{ 'border-red-500': errors.email }"
                placeholder="Enter your email address"
              >
              <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
            </div>

            <!-- Subject Field -->
            <div>
              <label for="subject" class="block text-sm font-medium text-gray-700 mb-2">
                Subject
              </label>
              <input
                id="subject"
                v-model="form.subject"
                type="text"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition-all duration-200"
                placeholder="What's this about?"
              >
            </div>

            <!-- Message Field -->
            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 mb-2">
                Message *
              </label>
              <textarea
                id="message"
                v-model="form.message"
                rows="5"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition-all duration-200 resize-none"
                :class="{ 'border-red-500': errors.message }"
                placeholder="Tell me about your project..."
              ></textarea>
              <p v-if="errors.message" class="text-red-500 text-sm mt-1">{{ errors.message }}</p>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              :disabled="isSubmitting"
              class="btn-primary w-full"
              :class="{ 'opacity-50 cursor-not-allowed': isSubmitting }"
            >
              <i v-if="isSubmitting" class="fas fa-spinner fa-spin mr-2"></i>
              <i v-else class="fas fa-paper-plane mr-2"></i>
              {{ isSubmitting ? 'Sending...' : 'Send Message' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ContactSection',
  data() {
    return {
      form: {
        name: '',
        email: '',
        subject: '',
        message: ''
      },
      errors: {},
      isSubmitting: false,
      showSuccess: false
    }
  },
  methods: {
    validateForm() {
      this.errors = {}

      // Name validation
      if (!this.form.name.trim()) {
        this.errors.name = 'Name is required'
      } else if (this.form.name.trim().length < 2) {
        this.errors.name = 'Name must be at least 2 characters'
      }

      // Email validation
      if (!this.form.email.trim()) {
        this.errors.email = 'Email is required'
      } else if (!this.isValidEmail(this.form.email)) {
        this.errors.email = 'Please enter a valid email address'
      }

      // Message validation
      if (!this.form.message.trim()) {
        this.errors.message = 'Message is required'
      } else if (this.form.message.trim().length < 10) {
        this.errors.message = 'Message must be at least 10 characters'
      }

      return Object.keys(this.errors).length === 0
    },

    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    },

    async submitForm() {
      if (!this.validateForm()) {
        return
      }

      this.isSubmitting = true

      try {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        // Show success message
        this.showSuccess = true
        
        // Reset form
        this.form = {
          name: '',
          email: '',
          subject: '',
          message: ''
        }

        // Hide success message after 5 seconds
        setTimeout(() => {
          this.showSuccess = false
        }, 5000)

      } catch (error) {
        console.error('Error submitting form:', error)
        // Handle error (you could show an error message here)
      } finally {
        this.isSubmitting = false
      }
    }
  }
}
</script>

<style scoped>
/* Styles removed and moved to template to fix @apply linting issues */
</style>
