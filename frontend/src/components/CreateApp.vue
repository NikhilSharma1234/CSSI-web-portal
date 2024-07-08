<script setup lang="ts">
import sideBar from './side-bar.vue';


import { ref } from 'vue';
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const router = useRouter()

const loading = ref(false)

const schema = yup.object({
    ownerId: yup.string().max(36).required('Owner ID is required').label('Owner ID').matches(/^[a-z0-9-]{1,36}$/, { message: 'ID must contain no spaces and only lowercase letters, numbers, or dashes (-)' }),
    appId: yup.string().required('Application ID is required').label('Application ID').matches(/^[a-z0-9-]{1,36}$/, { message: 'ID must contain no spaces and only lowercase letters, numbers, or dashes (-)' }),
    appName: yup.string().max(50).required('Application Name is required').label('Application Name'),
    description: yup.string().max(2000).label('Application Description')
});






const { errors, validate, defineField } = useForm({
    validationSchema: schema
});


const [ownerId] = defineField('ownerId')
const [appId] = defineField('appId')
const [appName] = defineField('appName')
const [description] = defineField('description')


const validateForm = async () => {
    await validate();
    if (Object.keys(errors.value).length) {
        return console.log('Validation failed:', errors.value);
    }
    loading.value = true;
    setTimeout(() => {
        loading.value = false;
        createApplication();
    }, 2000);
};


const createApplication = async () => {
    console.log('Form submitted with:', {
        id: ownerId.value,
        appId: appId.value,
        appName: appName.value,
        description: description.value,
    });
}

</script>


<template>
    <div class="container">
        <sideBar></sideBar>
        <RouterView />


        <div class="card width p-4 shadow-3 border-round">
            <div class="text-center mb-6">
                <h2>Create Application</h2>
                <Divider />
            </div>


            <div class="card flex justify-content-center">
                <form @submit.prevent="validateForm()">
                    <div class="flex flex-column gap-2 mx-auto" style="min-height: 16rem; max-width: 20rem">
                        <div class="text-center mt-3 mb-3 text-xl font-semibold">Enter Application Details
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Owner ID<span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="ownerId" type="text" :class="{ 'p-invalid': errors.ownerId }"
                                placeholder="Enter owner ID" />
                            <small id="id-help" class="p-error">{{ errors.ownerId }}</small>
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Application ID <span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="appId" type="text" :class="{ 'p-invalid': errors.appId }"
                                placeholder="Enter Application Id" />
                            <small id="id-help" class="p-error">{{ errors.appId }}</small>
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Application Name <span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="appName" type="text" :class="{ 'p-invalid': errors.appName }"
                                placeholder="Enter Application Name" />
                            <small id="id-help" class="p-error">{{ errors.appName }}</small>
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Application Description
                            </label>
                            <Textarea id="input" v-model="description" type="text"
                                :class="{ 'p-invalid': errors.description }" placeholder="Enter Application Description" />
                            <small id="id-help" class="p-error">{{ errors.description }}</small>
                        </div>
                    </div>
                    <div class="flex pt-4 justify-content-end">
                        <Button label="Next" :loading="loading" icon="pi pi-arrow-right" type="submit" iconPos="right" />
                    </div>
                </form>
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
}
</style>
