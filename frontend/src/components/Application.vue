<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { ApplicationNames } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';


const application = ref();



const filters3 = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    ID: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    devices: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },

  });


onMounted(() => {
    ApplicationNames.getApplicationNamesSmall().then((data) => (application.value = data));
});





</script>


<template>
  <div class="container">
      <sideBar></sideBar>
      <RouterView />
      <div class="card p-4 shadow-1 border-round">
          <div class="text-center">
              <h2>Collaborated Applications</h2>
              <Divider />
              <DataTable
          v-model:filters="filters3"
          :value="application"
          paginator
          :rows="5"
          filterDisplay="menu"
          selectionMode="single"
          dataKey="ID"
          :globalFilterFields="['ID', 'name', 'devices']"
          class="mt-5"
        >
          <template #header>
            <IconField class="margin" icon-position="left">
              <InputIcon>
                <i class="pi pi-search" />
              </InputIcon>
              <InputText v-model="filters3['global'].value" placeholder="Application Search" />
            </IconField>
          </template>
          <Column field="ID" header="ID" sortable style="width: 25%">
            <template #filter="{ filterModel }">
              <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by ID" />
            </template>
          </Column>
          <Column field="name" header="Name" sortable style="width: 25%">
            <template #filter="{ filterModel }">
              <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
            </template>
          </Column>
          <Column field="devices" header="End Devices" sortable style="width: 20%">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value" class="p-column-filter" placeholder="Min End Devices" />
            </template>
          </Column>

          <template #empty>No applications found</template>
        </DataTable>
    </div>
  </div>
</div>


</template>
 

 
<style scoped>


.container {
    display: flex;
  justify-content: center;
  align-items: center;
}

.margin{
    margin-right: 80%;
}


</style>