<script setup lang="ts">
import sideBar from './side-bar.vue';


import { ref } from 'vue';
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const router = useRouter()

const loading = ref(false)
const active = ref(0);
const op = ref();
const purpose = ref(['Personal', 'Academic', 'Professional']);


const members = ref([
    { name: 'Kaden Nesch', image: 'amyelsner.png', email: 'kadennesch@gmail.com', role: 'Admin' },
]);


const toggle = (event: any) => {
    op.value.toggle(event);
}


const schema = yup.object({
    orgID: yup.string().max(36).required('Organization ID is required').label('Organization ID').matches(/^[a-z0-9-]{1,36}$/, { message: 'ID must contain no spaces and only lowercase letters, numbers, or dashes (-)' }),
    selectedPurpose: yup.string().required('Organization Purpose is required').label('Purpose Of Use'),
    orgName: yup.string().max(50).label('Organization Name'),
    description: yup.string().max(2000).label('Organization Description')
});






const { errors, validate, defineField } = useForm({
    validationSchema: schema
});


const [orgID] = defineField('orgID')
const [selectedPurpose] = defineField('selectedPurpose')
const [orgName] = defineField('orgName')
const [description] = defineField('description')


const validateStep1 = async (nextCallback: any) => {
    await validate();
    if (!Object.keys(errors.value).length) {
        nextCallback();
    } else {
        console.log('Validation failed:', errors.value);
    }
};


const validateStep2 = async (nextCallback: any) => {
    await validate();
    if (!Object.keys(errors.value).length) {
        loading.value = true;
        setTimeout(() => {
            loading.value = false;
            createOrganization();
            nextCallback();
        }, 2000);
    } else {
        console.log('Validation failed:', errors.value);
    }
};


const createOrganization = async () => {
    console.log('Form submitted with:', {
        id: orgID.value,
        selectedPurpose: selectedPurpose.value,
        orgName: orgName.value,
        description: description.value,
    });
}


const routePage = async () => {
    router.push('/')
}


</script>


<template>
    <div class="container">
        <sideBar></sideBar>
        <RouterView />


        <div class="card width p-4 shadow-3 border-round">
            <div class="text-center mb-6">
                <h2>Create Organization</h2>
                <p label="dan" class="text-500 line-height-2">Create your own organization or <RouterLink to="joinorg"
                        class="no-underline "><a class="font-semibold no-underline text-blue-400 cursor-pointer">join a
                            pre-existing one</a></RouterLink>.</p>
                <Divider />
            </div>


            <div class="card flex justify-content-center">
                <Stepper linear v-model:activeStep="active">
                    <StepperPanel>
                        <template #header="{ index, clickCallback }">
                            <button class="bg-transparent border-none inline-flex flex-column gap-2" @click="clickCallback">
                                <span
                                    :class="['border-round border-2 w-3rem h-3rem inline-flex align-items-center justify-content-center', { 'bg-primary border-primary': index <= active, 'surface-border': index > active }]">
                                    <i class="pi pi-folder" />
                                </span>
                            </button>
                        </template>
                        <template #content="{ nextCallback }">
                            <form @submit.prevent="validateStep1(nextCallback)">
                                <div class="flex flex-column gap-2 mx-auto" style="min-height: 16rem; max-width: 20rem">
                                    <div class="text-center mt-3 mb-3 text-xl font-semibold">Enter Organization Details
                                    </div>
                                    <div class="field p-fluid mt-3">
                                        <label class="text-900 font-medium mb-2">
                                            Organization ID <span class="required-asterisk">*</span>
                                        </label>
                                        <InputText id="input" v-model="orgID" type="text"
                                            :class="{ 'p-invalid': errors.orgID }" placeholder="Enter ID" />
                                        <small id="id-help" class="p-error">{{ errors.orgID }}</small>
                                    </div>
                                    <div class="field p-fluid ">
                                        <label class="text-900 font-medium mb-2">Organization
                                            Purpose<span class="required-asterisk"> *</span>
                                        </label>
                                        <Dropdown v-model="selectedPurpose" :options="purpose"
                                            :class="{ 'p-invalid': errors.selectedPurpose }" placeholder="Select Purpose"
                                            class="w-full md:w-14rem" />
                                        <small id="selectedPurpose-help" class="p-error">{{ errors.selectedPurpose }}</small>
                                    </div>
                                </div>
                                <div class="flex pt-4 justify-content-end">
                                    <Button label="Next" :loading="loading" icon="pi pi-arrow-right" type="submit"
                                        iconPos="right" />
                                </div>
                            </form>
                        </template>
                    </StepperPanel>
                    <StepperPanel>
                        <template #header="{ index, clickCallback }">
                            <button class="bg-transparent border-none inline-flex flex-column gap-2" @click="clickCallback">
                                <span
                                    :class="['border-round border-2 w-3rem h-3rem inline-flex align-items-center justify-content-center', { 'bg-primary border-primary': index <= active, 'surface-border': index > active }]">
                                    <i class="pi pi-cog" />
                                </span>
                            </button>
                        </template>
                        <template #content="{ prevCallback, nextCallback }">



                            <div class="flex flex-column gap-2 mx-auto" style="min-height: 16rem; max-width: 20rem">
                                <div class="text-center mt-3 mb-3 text-xl font-semibold">Customize Organization (Optional)
                                </div>
                                <div class="field p-fluid mt-3">
                                    <label class="text-900 font-medium mb-2">Organization Name </label>
                                    <InputText id="input" v-model="orgName" type="text"
                                        :class="{ 'p-invalid': errors.orgName }" placeholder="Enter Name " />
                                    <small id="orgName-help" class="p-error">{{ errors.orgName }}</small>
                                </div>


                                <div class="field p-fluid">
                                    <label class="text-900 font-medium mb-2">Organization Description </label>
                                    <Textarea v-model="description" autoResize rows="5" cols="30"
                                        :class="{ 'p-invalid': errors.description }" placeholder="Enter Description" />
                                    <small id="description-help" class="p-error">{{ errors.description }}</small>
                                </div>



                            </div>
                            <div class="flex pt-4 justify-content-between">
                                <Button label="Back" raised severity="secondary" icon="pi pi-arrow-left"
                                    @click="prevCallback" />
                                <Button label="Create Organization" raised :loading="loading" iconPos="right"
                                    @click="validateStep2(nextCallback)" />
                            </div>
                        </template>
                    </StepperPanel>
                    <StepperPanel>
                        <template #header="{ index, clickCallback }">
                            <button class="bg-transparent border-none inline-flex flex-column gap-2" @click="clickCallback">
                                <span
                                    :class="['border-round border-2 w-3rem h-3rem inline-flex align-items-center justify-content-center', { 'bg-primary border-primary': index <= active, 'surface-border': index > active }]">
                                    <i class="pi pi-user-plus" />
                                </span>
                            </button>
                        </template>
                        <template #content="{ prevCallback }">
                            <div class="flex flex-column gap-2 mx-auto" style="min-height: 16rem; max-width: 24rem">
                                <div class="text-center mt-3 text-xl font-semibold">Invite Others To Organization (Optional)
                                </div>
                                <div class="text-center mt-5">
                                    <Button type="button" outlined icon="pi pi-image" label="Invite Others via Email"
                                        @click="toggle" />
                                    <OverlayPanel ref="op">
                                        <div class="flex flex-column gap-3 w-25rem">
                                            <div>
                                                <span class="font-medium text-900 block mb-2">Invite Member</span>
                                                <InputGroup>
                                                    <InputText placeholder="Enter Email" />
                                                    <Button label="Invite" icon="pi pi-users"></Button>
                                                </InputGroup>
                                            </div>
                                            <div>
                                                <span class="font-medium text-900 block mb-2">Team Members</span>
                                                <ul class="list-none p-0 m-0 flex flex-column gap-3">
                                                    <li v-for="member in members" :key="member.name"
                                                        class="flex align-items-center gap-2">
                                                        <img :src="`https://primefaces.org/cdn/primevue/images/avatar/${member.image}`"
                                                            style="width: 32px" />
                                                        <div>
                                                            <span class="font-medium">{{ member.name }}</span>
                                                            <div class="text-sm text-color-secondary">{{ member.email }}
                                                            </div>
                                                        </div>
                                                        <div
                                                            class="flex align-items-center gap-2 text-color-secondary ml-auto text-sm">
                                                            <span>{{ member.role }}</span>

                                                        </div>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </OverlayPanel>
                                </div>
                            </div>
                            <div class="flex pt-4 justify-content-end">
                                <Button label="To Dashboard" raised @click="routePage" iconPos="right"></Button>
                            </div>

                        </template>
                    </StepperPanel>
                </Stepper>
            </div>


        </div>


    </div>
</template>
 


 
<style scoped>
.container {
    display: flex;
    justify-content: center;
    /* Centers the child div horizontally */
    align-items: center;
    /* Centers the child div vertically */
}

.width {
    width: 80%;
}

.p-stepper {
    flex-basis: 50rem;
}


.required-asterisk {
    color: rgb(253, 87, 87);
    /* Makes the asterisk red */
}</style>
