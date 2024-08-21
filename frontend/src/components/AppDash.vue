<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { SensorList } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import { useRouter } from 'vue-router'

const sensors = ref();
const router = useRouter();


const owners = ref([
    { name: 'Kaden Nesch' },
    { name: 'Michael George' },
    { name: 'George Nesch' },
    { name: 'Michael Nesch' },
])

const route = async () => {
  router.push('/addsensor')
}


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
    <div class="card p-4 shadow-1 border-round">
      <div class="text-center">
        <h2>Application Name</h2>
        <h5 class="-mt-3">Application-ID</h5>
        <Divider />
      
      </div>
      <div class="text-center text-500 text-sm ml-8 mr-8">
        All sensors that belong to this application will be displayed here.
      </div>
      <div class="flex mt-5 justify-content-center">
      <Button @click="route">Add New Sensor</Button>
    </div>
  
      <DataTable
        v-model:filters="filters"
        :value="sensors"
        paginator
        :rows="5"
        filterDisplay="menu"
        selectionMode="single"
        dataKey="sensor"
        :globalFilterFields="['name', 'owner.name']"
        class="mt-3"
      >
        <template #header>
          <IconField class="-ml-3" iconPosition="left">
            <InputIcon>
              <i class="pi pi-search" />
            </InputIcon>
            <InputText v-model="filters['global'].value" placeholder="Sensor Search" />
          </IconField>
        </template>
        <Column field="name" header="Name" sortable style="width: 25%">
                <template #filter="{ filterModel }">
                    <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
                </template>
            </Column>
        <template #empty>No sensors found.</template>
        <Column header="Owner" sortable sortField="owner.name" filterField="owner" :showFilterMatchModes="false" :filterMenuStyle="{ width: '14rem' }" style="width: 25%">
                <template #body="{ data }">
                    <div class="flex align-items-center gap-2">
                        <span>{{ data.owner.name }}</span>
                    </div>
                </template>
                <template #filter="{ filterModel }">
                    <MultiSelect v-model="filterModel.value" :options="owners" optionLabel="name" placeholder="Any" class="p-column-filter">
                        <template #option="slotProps">
                            <div class="flex align-items-center gap-2">
                                <span>{{ slotProps.option.name }}</span>
                            </div>
                        </template>
                    </MultiSelect>
                </template>
            </Column>
      </DataTable>
    </div>
  </div>
</template>

 

 
<style scoped>


.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}



</style>