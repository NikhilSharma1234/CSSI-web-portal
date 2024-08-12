<script setup lang="ts">
import { auth } from '@/firebaseAuth'
import router from '@/router'
import Sidebar from './side-bar.vue'
import store from '@/store';

auth.onAuthStateChanged(function (user) {
  if (!user) {
    // not logged in
    alert('Logged out. Returning to login.')
    router.push('/login')
  }
  else {
    store.commit('SET_USER', user)
  }
})
</script>

<template>
  <div class="center-content">
    <Sidebar />
    <RouterLink to="createorg"><Button label="Join/Create Organization"></Button></RouterLink>
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
  