<template>
  <div class="flex h-screen">
    <sidebar/>
    <div class="flex flex-col flex-1">
      <topbar title="LOGIN"/>
      <div class="flex-1 flex items-center justify-center p-4">
        <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
          <h2 class="text-2xl font-bold mb-6 text-center">เข้าสู่ระบบ</h2>
          <form>
            <div class="mb-4">
              <label for="username" class="block text-gray-700 mb-2">ชื่อผู้ใช้</label>
              <input type="text" id="username" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" placeholder="กรอกชื่อผู้ใช้ของคุณ" />
            </div>
            <div class="mb-6">
              <label for="password" class="block text-gray-700 mb-2">รหัสผ่าน</label>
              <input type="password" id="password" class="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300" placeholder="กรอกรหัสผ่านของคุณ" />
            </div>
            <button type="submit" class="w-full bg-[#222263] text-white py-2 rounded-lg hover:bg-[#1a1a4d] transition">เข้าสู่ระบบ</button>
          </form>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script lang="ts" setup>
  useHead({
    title: 'Login'
  });
</script>

<style>
  
</style>