<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted } from 'vue';
import { OrganizationList } from '@/store';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const organization = ref();
const selectedUser = ref();
const visible = ref();
const op = ref();
const router = useRouter()


const filters3 = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
});

const filters = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    name: { operator: FilterOperator.AND, constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }] },
    owner: { value: null, matchMode: FilterMatchMode.IN },
});

const filters2 = ref({
    global: { value: null, matchMode: FilterMatchMode.CONTAINS },
    owner: { value: null, matchMode: FilterMatchMode.IN },
    role: { value: null, matchMode: FilterMatchMode.IN},
});



const owners = ref([
    { name: 'Ioni Bowcher' },
    { name: 'Anna Figueroa' },
    { name: 'Crystal Mint' },
    { name: 'Ashley Carter' },
    { name: 'Kaden Nesch' },
    { name: 'Michael Rapaport' }
]);


const roles = ref([
    { name: 'Admin' },
    { name: 'Member' },

]);



const member = ref(false);

const members = ref([
    { name: 'Kaden Nesch', image: 'amyelsner.png', email: 'kadennesch@gmail.com', role: 'Admin' },
]);

const toggle = (event: any) => {
    op.value.toggle(event);
}

onMounted(() => {
    OrganizationList.getOrganizationSmall().then((data) => (organization.value = data));
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
                  ? 'This is the member dashboard. You will be able to see all of the collaborated applications here.'
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
            <DataTable
                  v-model:filters="filters3"
                  :value="organization"
                  v-if="member"
                  paginator
                  :rows="5"
                  filterDisplay="menu"
                  selectionMode="single"
                  dataKey="application"
                  :globalFilterFields="['name']"
                  class="mt-5"
              >
                  <template #header>
                      <IconField class="-ml-3" iconPosition="left">
                          <InputIcon>
                              <i class="pi pi-search" />
                          </InputIcon>
                          <InputText v-model="filters3['global'].value" placeholder="Application Search" />
                      </IconField>
                  </template>
                  <Column field="name" header=" Name" sortable style="width: 25%">
                      <template #filter="{ filterModel }">
                          <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
                      </template>
                  </Column>
                  <Column
                      v-if="!member"
                      header="Owner"
                      sortable
                      sortField="owner.name"
                      filterField="owner"
                      :showFilterMatchModes="false"
                      :filterMenuStyle="{ width: '14rem' }"
                      style="width: 25%"
                  >
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

                  <template #empty>No applications found </template>
              </DataTable>
          <div class="card">
            <Accordion :multiple="true" :activeIndex="0" expandIcon="pi pi-plus" collapseIcon="pi pi-minus">
                <AccordionTab v-if="!member" headerClass="text-xl" header="List of Collaborated Applications">
              <DataTable
                  v-model:filters="filters"
                  :value="organization"
                  paginator
                  :rows="5"
                  filterDisplay="menu"
                  selectionMode="single"
                  dataKey="member"
                  :globalFilterFields="['name', 'owner.name']"
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
                      sortField="owner.name"
                      filterField="owner"
                      :showFilterMatchModes="false"
                      :filterMenuStyle="{ width: '14rem' }"
                      style="width: 25%"
                  >
                      <template #body="{ data }">
                          <div class="flex align-items-center gap-2">
                              <span>{{ data.owner.name }}</span>
                          </div>
                      </template>
                      <template #filter="{ filterModel }">
                          <MultiSelect v-model="filterModel.value" :options="owners" optionLabel="name" placeholder="Any" class="p-column-filter">
                              <template #option="slotProps">
                                  <div class="flex align-items-center gap-2">                                      <span>{{ slotProps.option.name }}</span>
                                  </div>
                              </template>
                          </MultiSelect>
                      </template>
                  </Column>

                  <template #empty>No applications found</template>
              </DataTable>
            </AccordionTab>
            <AccordionTab  v-if="!member" headerClass="text-xl red" header="List of Organization Members and their Roles">
                <DataTable
                  v-model:filters="filters2"
                  v-model:selection="selectedUser"
                  :value="organization"
                  paginator
                  :rows="5"
                  filterDisplay="menu"
                  selectionMode="single"
                  dataKey="member"
                  :globalFilterFields="['owner.name', 'role.name']"
              >
                  <template #header>
                      <IconField class="-ml-3" iconPosition="left">
                          <InputIcon>
                              <i class="pi pi-search" />
                          </InputIcon>
                          <InputText v-model="filters2['global'].value" placeholder="Member Search" />
                      </IconField>
                  </template>
                  <Column field="owner.name" header="Member Name" sortable style="width: 25%">
                      <template #filter="{ filterModel }">
                          <InputText v-model="filterModel.value" type="text" class="p-column-filter" placeholder="Search by name" />
                      </template>
                  </Column>
                  <Column
                      v-if="!member"
                      header="Role"
                      sortable
                      sortField="role.name"
                      filterField="role"
                      :showFilterMatchModes="false"
                      :filterMenuStyle="{ width: '14rem' }"
                      style="width: 25%"
                  >
                      <template #body="{ data }">
                          <div class="flex align-items-center gap-2">
                              <span>{{ data.role.name }}</span>
                          </div>
                      </template>
                      <template #filter="{ filterModel }">
                          <MultiSelect v-model="filterModel.value" :options="roles" optionLabel="name" placeholder="Any" class="p-column-filter">
                              <template #option="slotProps">
                                  <div class="flex align-items-center gap-2">                                      <span>{{ slotProps.option.name }}</span>
                                  </div>
                              </template>
                          </MultiSelect>
                      </template>
                  </Column>

                  <template #empty>No members found</template>
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