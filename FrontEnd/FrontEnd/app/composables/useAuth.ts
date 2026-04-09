import type { LoginResponse } from '~/types/auth'

export const useAuth = () => {

  const token = useState<string | null>('auth_token', () => {
    if (import.meta.client) {
      return localStorage.getItem('token')
    }
    return null
  })
  const user = useState<any>('auth_user', () => {
    if (import.meta.client) {
      const savedUser = localStorage.getItem('user')
      if (savedUser) {
        try {
          return JSON.parse(savedUser)
        } catch {
          return null
        }
      }
    }
    return null
  })

  const config = useRuntimeConfig()

  const login = async (username: string, password: string) => {
    const res = await $fetch<LoginResponse>(
      `${config.public.apiBase}/api/login`,
      {
        method: 'POST',
        body: {
          username,
          password
        }
      }
    )

    token.value = res.access_token
    user.value = res.user

    if (import.meta.client) {
      localStorage.setItem('token', res.access_token)
      localStorage.setItem('user', JSON.stringify(res.user))
    }

    return res
  }

  const logout = () => {
    token.value = null
    user.value = null
    if (import.meta.client) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
    }
  }

  return {
    login,
    logout,
    token,
    user
  }
}