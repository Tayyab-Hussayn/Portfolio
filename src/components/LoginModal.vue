<template>
  <!-- Modal Overlay -->
  <div v-if="isVisible" class="modal-overlay" @click="closeModal">
    <!-- Modal Content -->
    <div class="modal-content" @click.stop>
      <!-- Modal Header -->
      <div class="modal-header">
        <h2 class="text-2xl font-bold text-gray-900">
          Welcome Back
        </h2>
        <button @click="closeModal" class="close-button">
          <i class="fas fa-times"></i>
        </button>
      </div>

      <!-- Modal Body -->
      <div class="modal-body">
        <!-- Success Message -->
        <div v-if="showSuccess" class="success-message">
          <i class="fas fa-check-circle mr-2"></i>
          Login successful! Welcome back.
        </div>

        <!-- Login Form -->
        <form @submit.prevent="submitLogin" class="space-y-6">
          <!-- Email Field -->
          <div>
            <label for="loginEmail" class="form-label">
              Email Address
            </label>
            <div class="relative">
              <input
                id="loginEmail"
                v-model="loginForm.email"
                type="email"
                class="form-input pl-12"
                :class="{ 'border-red-500': errors.email }"
                placeholder="Enter your email"
              >
              <div class="input-icon">
                <i class="fas fa-envelope text-gray-400"></i>
              </div>
            </div>
            <p v-if="errors.email" class="error-message">{{ errors.email }}</p>
          </div>

          <!-- Password Field -->
          <div>
            <label for="loginPassword" class="form-label">
              Password
            </label>
            <div class="relative">
              <input
                id="loginPassword"
                v-model="loginForm.password"
                :type="showPassword ? 'text' : 'password'"
                class="form-input pl-12 pr-12"
                :class="{ 'border-red-500': errors.password }"
                placeholder="Enter your password"
              >
              <div class="input-icon">
                <i class="fas fa-lock text-gray-400"></i>
              </div>
              <button
                type="button"
                @click="togglePassword"
                class="password-toggle"
              >
                <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'" class="text-gray-400"></i>
              </button>
            </div>
            <p v-if="errors.password" class="error-message">{{ errors.password }}</p>
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <label class="flex items-center">
              <input
                v-model="loginForm.rememberMe"
                type="checkbox"
                class="checkbox"
              >
              <span class="ml-2 text-sm text-gray-600">Remember me</span>
            </label>
            <a href="#" class="text-sm text-primary hover:text-secondary">
              Forgot password?
            </a>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="isSubmitting"
            class="btn-primary w-full"
            :class="{ 'opacity-50 cursor-not-allowed': isSubmitting }"
          >
            <i v-if="isSubmitting" class="fas fa-spinner fa-spin mr-2"></i>
            <i v-else class="fas fa-sign-in-alt mr-2"></i>
            {{ isSubmitting ? 'Signing In...' : 'Sign In' }}
          </button>
        </form>

        <!-- Divider -->
        <div class="divider">
          <span class="divider-text">Or continue with</span>
        </div>

        <!-- Social Login Buttons -->
        <div class="space-y-3">
          <button class="social-login-btn">
            <i class="fab fa-google mr-3 text-red-500"></i>
            Continue with Google
          </button>
          <button class="social-login-btn">
            <i class="fab fa-github mr-3 text-gray-700"></i>
            Continue with GitHub
          </button>
        </div>

        <!-- Sign Up Link -->
        <div class="text-center mt-6">
          <p class="text-gray-600">
            Don't have an account?
            <a href="#" class="text-primary hover:text-secondary font-medium">
              Sign up here
            </a>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginModal',
  props: {
    isVisible: {
      type: Boolean,
      default: false
    }
  },
  emits: ['close'],
  data() {
    return {
      loginForm: {
        email: '',
        password: '',
        rememberMe: false
      },
      errors: {},
      isSubmitting: false,
      showSuccess: false,
      showPassword: false
    }
  },
  methods: {
    closeModal() {
      this.$emit('close')
      this.resetForm()
    },

    togglePassword() {
      this.showPassword = !this.showPassword
    },

    validateForm() {
      this.errors = {}

      // Email validation
      if (!this.loginForm.email.trim()) {
        this.errors.email = 'Email is required'
      } else if (!this.isValidEmail(this.loginForm.email)) {
        this.errors.email = 'Please enter a valid email address'
      }

      // Password validation
      if (!this.loginForm.password) {
        this.errors.password = 'Password is required'
      } else if (this.loginForm.password.length < 6) {
        this.errors.password = 'Password must be at least 6 characters'
      }

      return Object.keys(this.errors).length === 0
    },

    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    },

    async submitLogin() {
      if (!this.validateForm()) {
        return
      }

      this.isSubmitting = true

      try {
        // Simulate API call
        await new Promise(resolve => setTimeout(resolve, 2000))
        
        // Show success message
        this.showSuccess = true
        
        // Close modal after success
        setTimeout(() => {
          this.closeModal()
        }, 1500)

      } catch (error) {
        console.error('Login error:', error)
        // Handle login error
      } finally {
        this.isSubmitting = false
      }
    },

    resetForm() {
      this.loginForm = {
        email: '',
        password: '',
        rememberMe: false
      }
      this.errors = {}
      this.showSuccess = false
      this.showPassword = false
    }
  },
  mounted() {
    // Close modal on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && this.isVisible) {
        this.closeModal()
      }
    })
  }
}
</script>

<style scoped>
.modal-overlay {
  @apply fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4;
}

.modal-content {
  @apply bg-white rounded-2xl shadow-2xl max-w-md w-full max-h-screen overflow-y-auto;
}

.modal-header {
  @apply flex items-center justify-between p-6 border-b border-gray-200;
}

.close-button {
  @apply text-gray-400 hover:text-gray-600 text-xl p-1 rounded-full hover:bg-gray-100 transition-colors duration-200;
}

.modal-body {
  @apply p-6;
}

.form-label {
  @apply block text-sm font-medium text-gray-700 mb-2;
}

.form-input {
  @apply w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-primary focus:border-transparent transition-all duration-200;
}

.input-icon {
  @apply absolute left-4 top-1/2 transform -translate-y-1/2;
}

.password-toggle {
  @apply absolute right-4 top-1/2 transform -translate-y-1/2 p-1;
}

.checkbox {
  @apply h-4 w-4 text-primary focus:ring-primary border-gray-300 rounded;
}

.error-message {
  @apply text-red-500 text-sm mt-1;
}

.success-message {
  @apply bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg flex items-center mb-6;
}

.divider {
  @apply relative my-6;
}

.divider::before {
  content: '';
  @apply absolute inset-0 flex items-center;
  border-top: 1px solid theme('colors.gray.300');
}

.divider-text {
  @apply relative bg-white px-4 text-sm text-gray-500;
}

.social-login-btn {
  @apply w-full flex items-center justify-center px-4 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 transition-colors duration-200;
}
</style>

