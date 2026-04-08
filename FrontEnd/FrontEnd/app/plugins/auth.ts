export default defineNuxtPlugin(() => {
  if (import.meta.client) {
    const { token, user } = useAuth()

    const savedToken = localStorage.getItem('token')
    const savedUser = localStorage.getItem('user')

    if (savedToken) token.value = savedToken
    if (savedUser) user.value = JSON.parse(savedUser)
  }
})