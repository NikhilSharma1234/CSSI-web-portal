<script setup lang="ts">
</script>

<template>
    <div class="center-content">
      <RouterLink to="about"><Button label="To About"></Button></RouterLink>
      <RouterLink to="login"><Button label="To Login"></Button></RouterLink>
      <RouterView />
      <h1>Hello, this is our home page!</h1>
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
  