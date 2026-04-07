<template>
    {{ profileid }}
</template>

<script lang="ts" setup>
    const profileid = useRoute().params.profileid;
</script>