<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { SensorList } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';

const sensors = ref();


const owners = ref([
    { name: 'Kaden Nesch' },
    { name: 'Michael George' },
    { name: 'George Nesch' },
    { name: 'Michael Nesch' },
])


const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    owner: { value: null, matchMode: FilterMatchMode.IN },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
});


onMounted(() => {
    SensorList.getSensorSmall().then((data) => (sensors.value = data));
});


</script>

<template>
  <div class="container">
    <sideBar></sideBar>
    <RouterView />
    <div class="card p-4 shadow-3 border-round">
      <div class="text-center">
        <h2>Register New Sensor</h2>
        <h5 class="-mt-3">To Application-ID</h5>
        <Divider />
      
      </div>
      <div class="text-center text-500 text-sm ml-8 mr-8">
        Register new sensor using QR or defualt setup.
      </div>
      <div class="text-center mt-4">
      <Button outlined>Use QR Code </Button>
      <div class="text-600 font-medium mb-3 mt-3">Or</div>
      
    </div>
  
    </div>
  </div>
</template>

 

 
<style scoped>


.container {
  display: flex;
  justify-content: center; /* Centers the child div horizontally */
  align-items: center; /* Centers the child div vertically */
   /* Makes the container take the full viewport height */
}



</style>