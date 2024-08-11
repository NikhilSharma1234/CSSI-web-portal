<script setup lang="ts">
import { RouterView } from 'vue-router';
import Dialog from 'primevue/dialog';
import { onBeforeMount, ref } from "vue";
import { checkServerHealth } from './helpers';

let serverDown = ref(false);
onBeforeMount(async () => {
  serverDown.value = await checkServerHealth();
})
</script>

<template>
<img class="background" src="./assets/tahoe.jpg">
  <Dialog v-model:visible="serverDown" modal :closable="false" header="Server Down" :style="{ width: '25rem' }">
    <span class="text-surface-500 dark:text-surface-400 block mb-1">Server is down. Please connect to the server and
      refresh</span>
  </Dialog>
  <RouterView v-if="!serverDown" />
</template>

<style scoped>

.background{
    position: fixed;
    top: 0;
    bottom:0;
    left:0;
    width: 100%;
    height: 100%;
    z-index: -1;
}
</style>
