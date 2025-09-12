/*import { ref, computed } from 'vue'
import { useQuasar } from 'quasar'

interface User {
  email: string
  name: string
}

interface LoginCredentials {
  email: string
  password: string
}

export function useAuth() {
  const $q = useQuasar()
  const user = ref<User | null>(null)
  const isLoading = ref(false)
  const error = ref<string | null>(null)

  const isAuthenticated = computed(() => user.value !== null)

  const login = async (credentials: LoginCredentials): Promise<boolean> => {
    isLoading.value = true
    error.value = null
    
    try {
      // Simulate API call
      await new Promise(resolve => setTimeout(resolve, 1000))
      
      if (credentials.email === 'admin@example.com' && credentials.password === 'password') {
        user.value = {
          email: credentials.email,
          name: 'Admin User'
        }
        $q.notify({
          type: 'positive',
          message: 'Login successful!',
          position: 'top'
        })
        return true
      } else {
        throw new Error('Invalid credentials')
      }
    } catch (err) {
      error.value = err instanceof Error ? err.message : 'Login failed'
      $q.notify({
        type: 'negative',
        message: error.value,
        position: 'top'
      })
      return false
    } finally {
      isLoading.value = false
    }
  }

  const logout = (): void => {
    user.value = null
    $q.notify({
      type: 'info',
      message: 'Logged out successfully',
      position: 'top'
    })
  }

  return {
    user,
    isLoading,
    error,
    isAuthenticated,
    login,
    logout
  }
}*/