<template>
  <div class="flex h-screen">
    <sidebar/>
    <div class="flex flex-col flex-1">
      <topbar title="score"/>
      <div class="scrollable flex-1 flex-col flex-1 p-4 overflow-y-auto">
        <div class="bg-white rounded-lg p-4">
          
          
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
  // const config = useRuntimeConfig()

  // const {data:role} = useFetch(`${config.public.apiBase}/api/users/me`, {
  //   method: 'GET',
  //   headers: {
  //     'Authorization': `Bearer ${useAuth().token.value}`
  //   },
  //   transform: (response : { role: string}) => response.role
  // })

  // console.log(role.value)
</script>