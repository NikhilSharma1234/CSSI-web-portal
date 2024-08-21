<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { OrganizationNames } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';


const organization = ref();



const filters3 = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    ID: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    description: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    collaborators: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
});


onMounted(() => {
    OrganizationNames.getOrganizationNamesSmall().then((data) => (organization.value = data));
});





</script>


<template>
  <div class="container">
      <sideBar></sideBar>
      <RouterView />
      <div class="card p-4 shadow-1 border-round">
          <div class="text-center">
              <h2>Collaborated Organizations</h2>
              <Divider />
              <DataTable
          v-model:filters="filters3"
          :value="organization"
          paginator
          :rows="5"
          filterDisplay="menu"
          selectionMode="single"
          dataKey="ID"
          :globalFilterFields="['ID', 'name', 'description', 'collaborators']"
          class="mt-5"
        >
          <template #header>
            <IconField class="margin" icon-position="left" >
              <InputIcon>
                <i class="pi pi-search" />
              </InputIcon>
              <InputText  v-model="filters3['global'].value" placeholder="Organization Search" />
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
          <Column field="description" header="Description" sortable style="width: 30%">
            <template #filter="{ filterModel }">
              <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by description" />
            </template>
          </Column>
          <Column field="collaborators" header="Collaborators" sortable style="width: 20%">
            <template #filter="{ filterModel }">
              <InputNumber v-model="filterModel.value" class="p-column-filter" placeholder="Min Collaborators" />
            </template>
          </Column>

          <template #empty>No organizations found</template>
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