<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { CustomerService } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';

const customers = ref();
const selectedCustomer = ref();
const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    'country.name': { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    representative: { value: null, matchMode: FilterMatchMode.IN },
    status: { operator: FilterOperator.OR, constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }] }
});
const representatives = ref([
    { name: 'Amy Elsner', image: 'amyelsner.png' },
    { name: 'Anna Fali', image: 'annafali.png' },
    { name: 'Asiya Javayant', image: 'asiyajavayant.png' },
    { name: 'Bernardo Dominic', image: 'bernardodominic.png' },
    { name: 'Elwin Sharvill', image: 'elwinsharvill.png' },
    { name: 'Ioni Bowcher', image: 'ionibowcher.png' },
    { name: 'Ivan Magalhaes', image: 'ivanmagalhaes.png' },
    { name: 'Onyama Limba', image: 'onyamalimba.png' },
    { name: 'Stephen Shaw', image: 'stephenshaw.png' },
    { name: 'XuXue Feng', image: 'xuxuefeng.png' }
]);

const member = ref(false);

onMounted(() => {
    CustomerService.getCustomersSmall().then((data) => (customers.value = data));
});

const toggleMember = () => {
    member.value = !member.value;
};
</script>


<template>
  <div class="container">
      <sideBar></sideBar>
      <RouterView />

      <div class="card width p-4 shadow-3 border-round">
          <div class="text-center mb-5">
              <h2>Organization Name</h2>
              <Button class="mb-4" @click="toggleMember">Switch to {{ member ? 'Leader' : 'Member' }}</Button>
              <Divider />
          </div>
          <div class="text-center text-500 text-sm mx-8 mb-2">
              {{ member
                  ? 'This is the member dashboard. You will be able to see all of your personal applications here.'
                  : 'This is the organization leader dashboard. You will be able to see all applications created in this organization and their respective owners.' }}
          </div>
          <div class="card">
              <DataTable
                  v-model:filters="filters"
                  v-model:selection="selectedCustomer"
                  :value="customers"
                  stateStorage="session"
                  stateKey="dt-state-demo-session"
                  paginator
                  :rows="5"
                  filterDisplay="menu"
                  selectionMode="single"
                  dataKey="id"
                  :globalFilterFields="['name', 'country.name', 'representative.name', 'status']"
              >
                  <template #header>
                      <IconField iconPosition="left">
                          <InputIcon>
                              <i class="pi pi-search" />
                          </InputIcon>
                          <InputText v-model="filters['global'].value" placeholder="Global Search" />
                      </IconField>
                  </template>
                  <Column field="name" header="Name" sortable style="width: 25%">
                      <template #filter="{ filterModel }">
                          <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
                      </template>
                  </Column>
                  <Column
                      v-if="!member"
                      header="Owner"
                      sortable
                      sortField="representative.name"
                      filterField="representative"
                      :showFilterMatchModes="false"
                      :filterMenuStyle="{ width: '14rem' }"
                      style="width: 25%"
                  >
                      <template #body="{ data }">
                          <div class="flex align-items-center gap-2">
                              <img :alt="data.representative.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${data.representative.image}`" style="width: 32px" />
                              <span>{{ data.representative.name }}</span>
                          </div>
                      </template>
                      <template #filter="{ filterModel }">
                          <MultiSelect v-model="filterModel.value" :options="representatives" optionLabel="name" placeholder="Any" class="p-column-filter">
                              <template #option="slotProps">
                                  <div class="flex align-items-center gap-2">
                                      <img :alt="slotProps.option.name" :src="`https://primefaces.org/cdn/primevue/images/avatar/${slotProps.option.image}`" style="width: 32px" />
                                      <span>{{ slotProps.option.name }}</span>
                                  </div>
                              </template>
                          </MultiSelect>
                      </template>
                  </Column>

                  <template #empty>No customers found.</template>
              </DataTable>
          </div>
      </div>
  </div>
</template>
 

 
<style scoped>


.width{
  width: 50%;
}


.container {
  display: flex;
  justify-content: center; /* Centers the child div horizontally */
  align-items: center; /* Centers the child div vertically */
   /* Makes the container take the full viewport height */
}



</style>