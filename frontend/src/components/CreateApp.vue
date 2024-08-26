<script setup lang="ts">
import sideBar from './side-bar.vue';


import { ref } from 'vue';
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'
import axios from 'axios';
import { CreateApplication } from '@/helpers';

const router = useRouter()
const loading = ref(false)

const schema = yup.object({
    user_id: yup.string().max(36).required('user_id is required').label('user_id'),
    app_id: yup.string().required('Application ID is required').label('Application ID').matches(/^[a-z0-9-]{1,36}$/, { message: 'ID must contain no spaces and only lowercase letters, numbers, or dashes (-)' }),
    app_name: yup.string().max(50).required('Application Name is required').label('Application Name'),
    description: yup.string().max(2000).label('Application Description')
});

const { errors, validate, defineField } = useForm({
    validationSchema: schema
});


const [user_id] = defineField('user_id')
const [app_id] = defineField('app_id')
const [app_name] = defineField('app_name')
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
    }, 1000);
};


const createApplication = async () => {
    try {
        const response = await CreateApplication(
            user_id.value,
            app_id.value,
            app_name.value,
            description.value
        );

        console.log('Application created successfully:', response.data);
        router.push('/');  // Redirect to a success page or wherever you want

    } finally {
        loading.value = false;
    }
};

</script>


<template>
    <sideBar></sideBar>
    <RouterView />

    <div class="container">



        <div class="card width p-4 shadow-1 border-round">
            <div class="text-center mb-6">
                <h2>Create Application</h2>
                <p class="text-500 line-height-2">Create an individual application or add your application to an organization.</p>
                <Divider />
            </div>

            <div class="card flex justify-content-center">
                <form @submit.prevent="validateForm()">
                    <div class="flex flex-column -mt-4 mx-auto" style="min-height: 16rem; max-width: 20rem">
                        <div class="text-center mb-5 text-xl font-semibold">Enter Application Details
                        </div>
                        <div class="field p-fluid ">
                            <label class="text-900 font-medium mb-2">
                                user_id ID<span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="user_id" type="text" :class="{ 'p-invalid': errors.app_id }"
                            placeholder="Enter User/Organization-ID" />
                            <small id="id-help" class="p-error">{{ errors.user_id }}</small>
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Application-ID <span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="app_id" type="text" :class="{ 'p-invalid': errors.app_id }"
                                placeholder="Enter Application-ID" />
                            <small id="id-help" class="p-error">{{ errors.app_id }}</small>
                        </div>
                        <div class="field p-fluid mt-3">
                            <label class="text-900 font-medium mb-2">
                                Application Name
                            </label>
                            <InputText id="input" v-model="app_name" type="text" :class="{ 'p-invalid': errors.app_name }"
                                placeholder="Enter Application Name" />
                            <small id="id-help" class="p-error">{{ errors.app_name }}</small>
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
    align-items: center;
    min-height: 90vh;  
}

.width {
    width: 50%;
}

.p-stepper {
    flex-basis: 50rem;
}


.required-asterisk {
    color: rgb(253, 87, 87);
}
</style>
