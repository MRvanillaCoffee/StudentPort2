import type { LoginResponse } from '~/types/auth'

export const useAuth = () => {

  const token = useState<string | null>('auth_token', () => null)
  const user = useState<any>('auth_user', () => null)

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

  return {
    login,
    token,
    user
  }
}