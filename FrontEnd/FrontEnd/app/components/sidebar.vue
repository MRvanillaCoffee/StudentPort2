<template>
  <div class="h-screen w-3xs border-r-6 border-orange-500 bg-[#222263] flex flex-col items-center py-6">
    <img src="~/assets/LOGO-CIT.png" alt="Logo" class="w-28 mb-4" />

    <h1 class="text-white text-2xl font-semibold text-center mb-6">
      Student Portfolio
    </h1>

    <ul class="w-full px-4 space-y-4">
      <li v-if="!isLoggedIn" class="flex items-center space-x-3 text-white text-xl hover:bg-white/10 p-2 rounded-lg transition">
        <Icon name="ic:baseline-login" class="text-3xl" />
        <a href="/login">เข้าสู่ระบบ</a>
      </li>

      <li v-else class="flex items-center space-x-3 text-white text-xl hover:bg-white/10 p-2 rounded-lg transition">
        <Icon name="ic:baseline-login" class="text-3xl" />
        <a href="/score">คะแนนนักศึกษา</a>
      </li>

      <li class="flex items-center space-x-3 text-white text-xl hover:bg-white/10 p-2 rounded-lg transition">
        <Icon name="ic:baseline-school" class="text-3xl" />
        <a href="/">สาขาวิชาที่เปิดสอน</a>
      </li>

      <li class="flex items-center space-x-3 text-white text-xl hover:bg-white/10 p-2 rounded-lg transition">
        <Icon name="ic:baseline-menu-book" class="text-3xl" />
        <a href="/">หลักสูตร</a>
      </li>
    </ul>

  </div>
</template>

<script setup lang="ts">
  const isLoggedIn = false;
</script>