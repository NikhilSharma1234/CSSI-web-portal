<script setup lang="ts">

</script>

<template>
  <div class="center-content">
    <RouterLink to="/"><Button label="To Home"></Button></RouterLink>
    <RouterView />
    <h1>Hello, this is our About page!</h1>
  </div>
</template>
  
<style scoped>
.center-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}
</style>