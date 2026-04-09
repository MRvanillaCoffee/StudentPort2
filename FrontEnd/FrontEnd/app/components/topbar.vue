<template>
    <div class="bg-white m-5 rounded-lg shadow-md p-4 flex items-center justify-between">
        <h1 class="text-2xl font-bold">{{title}}</h1>
        <div class="flex items-center space-x-4">
            <div v-if="isLoggedIn" class="flex items-center space-x-4">
                <span class="text-gray-700 font-semibold">{{ user?.username || 'User' }}</span>
                <button @click="logout" class="text-red-500 hover:text-red-700 text-sm">ออกจากระบบ</button>
            </div>
            <a v-else href="/login" class="bg-[#222263] text-white px-4 py-2 rounded-lg hover:bg-[#1a1a4d] transition">เข้าสู่ระบบ</a>
        </div>

    </div>
</template>

<script lang="ts" setup>
import { useAuth } from '~/composables/useAuth'

const { token, user } = useAuth()
const isLoggedIn = computed(() => !!token.value)

const logout = () => {
  token.value = null
  user.value = null
  if (import.meta.client) {
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }
  navigateTo('/login')
}

defineProps({
    title: {
        type: String,
        default: 'Student Portfolio'
    }
});
</script>