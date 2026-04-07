<template>
    <div class="bg-white m-5 rounded-lg shadow-md p-4 flex items-center justify-between">
        <h1 class="text-2xl font-bold">{{title}}</h1>
        <div class="flex items-center space-x-4">
            <a v-if="isLogedin" href="/login"><Icon name="ic:baseline-account-circle" class="text-gray-600 text-3xl" /></a>
            <a v-else href="/login" class="bg-[#222263] text-white px-4 py-2 rounded-lg">Login</a>
        </div>

    </div>
</template>

<script lang="ts" setup>
    const isLogedin = false;
    defineProps({
        title: {
            type: String,
            default: 'Student Portfolio'
        }
    });
</script>