<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { CustomerService } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const customers = ref();
const selectedCustomer = ref();
const visible = ref();
const op = ref();
const router = useRouter()

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

const members = ref([
    { name: 'Kaden Nesch', image: 'amyelsner.png', email: 'kadennesch@gmail.com', role: 'Admin' },
]);

const toggle = (event: any) => {
    op.value.toggle(event);
}

onMounted(() => {
    CustomerService.getCustomersSmall().then((data) => (customers.value = data));
});

const toggleMember = () => {
    member.value = !member.value;
};

const schema = yup.object({
  orgName: yup.string().max(50).label('Organization Name'),
  description: yup.string().max(2000).label('Organization Description')
});

const { errors, validate, defineField } = useForm({
  validationSchema: schema
});

const [orgName] = defineField('orgName')
const [description] = defineField('description')


</script>


<template>
  <div class="container">
      <sideBar></sideBar>
      <RouterView />

      <div class="card p-4 shadow-3 border-round">
          <div class="text-center">
              <h2>Organization Name</h2>
              <h5 class="-mt-3">Organization-ID</h5>
              <Button class="mb-2" @click="toggleMember">Switch to {{ member ? 'Leader' : 'Member' }}</Button>
              <Divider />
          </div>
          <div class="text-center text-500 text-sm mx-8 ">
              {{ member
                  ? 'This is the member dashboard. You will be able to see all of your personal applications here.'
                  : 'This is the organization leader dashboard. You will be able to see all applications created in this organization and their respective owners.' }}
          </div>
          <div v-if="!member" class="flex mt-5 justify-content-center">
        <Button label="Edit Organization & Invite Others" @click="visible = true" />
        <Dialog v-model:visible="visible" :draggable="false" closeOnEscape position="center" dismissableMask modal header="Edit Profile">
            <template #header>
                <div class="inline-flex align-items-center justify-content-center gap-2">
                    <span class="font-boldwhite-space-nowrap -mb-4 ">Organization-ID</span>
                </div>
            </template>
            <span class="p-text-secondary block mb-4">Edit Organization Information</span>
            <div class="flex flex-column gap-2 mx-auto" style="min-height: 16rem; max-width: 30rem">
                        <div class="field p-fluid mt-2">
                            <label class="text-900 font-medium mb-2">Name </label>
                                <InputText id="input" v-model="orgName" type="text" :class="{ 'p-invalid': errors.orgName}" placeholder="Organization Name " />
                                <small id="orgName-help" class="p-error">{{ errors.orgName}}</small>
                        </div>


                        <div class="field p-fluid">
                            <label class="text-900 font-medium mb-2">Description </label>
                                <Textarea v-model="description" autoResize  rows="5" cols="30" :class="{ 'p-invalid': errors.description}" placeholder="Description" />
                                <small id="description-help" class="p-error">{{ errors.description}}</small>
                        </div>


                       
                    </div>
            <div class="flex flex-column gap-2 mx-auto mb-2" >
                        <div class="text-center mt-3 text-lg font-semibold">Invite Others To Organization</div>
                        <div class="text-center mt-2">
                            <Button type="button" outlined icon="pi pi-image" label="Invite via Email" @click="toggle" />
                            <OverlayPanel ref="op">
            <div class="flex flex-column gap-3 w-25rem">
                <div>
                    <span class="font-medium text-900 block mb-2">Invite Member</span>
                    <InputGroup>
                        <InputText placeholder="Enter Email"/>
                        <Button label="Invite" icon="pi pi-users"></Button>
                    </InputGroup>
                </div>
                <div>
                    <span class="font-medium text-900 block mb-2">Team Members</span>
                    <ul class="list-none p-0 m-0 flex flex-column gap-3">
                        <li v-for="member in members" :key="member.name" class="flex align-items-center gap-2">
                            <img :src="`https://primefaces.org/cdn/primevue/images/avatar/${member.image}`" style="width: 32px" />
                            <div>
                                <span class="font-medium">{{ member.name }}</span>
                                <div class="text-sm text-color-secondary">{{ member.email }}</div>
                            </div>
                            <div class="flex align-items-center gap-2 text-color-secondary ml-auto text-sm">
                                <span>{{ member.role }}</span>
                       
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </OverlayPanel>
                        </div>
                    </div>
            <template #footer>
                <Button label="Cancel" text severity="secondary" @click="visible = false" autofocus />
                <Button label="Save" severity="primary" @click="visible = false" autofocus />
            </template>
        </Dialog>
    </div>
          <div class="card">
            <Accordion :multiple="true" :activeIndex="0" expandIcon="pi pi-plus" collapseIcon="pi pi-minus">
                <AccordionTab headerClass="text-xl" header="List of Applications and Owners">
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
                      <IconField class="-ml-3" iconPosition="left">
                          <InputIcon>
                              <i class="pi pi-search" />
                          </InputIcon>
                          <InputText v-model="filters['global'].value" placeholder="Application Search" />
                      </IconField>
                  </template>
                  <Column field="name" header="Application Name" sortable style="width: 25%">
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
            </AccordionTab>
            <AccordionTab headerClass="text-xl red" header="List of Organization Members and their Roles">
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
                      <IconField class="-ml-3" iconPosition="left">
                          <InputIcon>
                              <i class="pi pi-search" />
                          </InputIcon>
                          <InputText v-model="filters['global'].value" placeholder="Application Search" />
                      </IconField>
                  </template>
                  <Column field="name" header="Application Name" sortable style="width: 25%">
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
            </AccordionTab>
            </Accordion>
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