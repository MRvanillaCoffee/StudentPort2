<template>
  <div class="flex h-screen">
    <sidebar/>
    <div class="flex flex-col flex-1">
      <topbar/>
      <div class="scrollable flex-1 flex-col flex-1 p-4 overflow-y-auto">
        <div class="bg-white rounded-lg p-4">
          News
          <div class="bg-gray-300 m-2 p-4 h-100">
            <br>
          </div>

          <div class="bg-gray-300 m-2 p-4 h-100">
            <br>
          </div>

          <div class="bg-gray-300 m-2 p-4 h-100">
            <br>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
  import sidebar from '~/components/sidebar.vue';
  import topbar from '~/components/topbar.vue';
  useHead({
    title: 'Student Portfolio',
  });
</script>
