<script setup lang="ts">
import sideBar from './side-bar.vue';


import { ref } from 'vue';
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'
import * as yup from 'yup'
import OrgAwait from './OrgAwait.vue'

const router = useRouter()



const showOrgAwait = ref(false);
const loading = ref(false)


const schema = yup.object({
  orgID: yup.string().max(36).required('Organization ID is required').label('Organization ID').matches(/^[a-z0-9-]{1,36}$/, {message: 'ID must contain no spaces and only lowercase letters, numbers, or dashes (-)'})  ,
  email: yup.string().max(320).required('Organization Leader Email is required').label('Organization Leader Email').email(),
  message: yup.string().max(2000).label('Organization message')
});


const { errors, validate, defineField, handleSubmit  } = useForm({
  validationSchema: schema
});


const [orgID] = defineField('orgID')
const [email] = defineField('email')
const [message] = defineField('message')


const onSubmit = handleSubmit(async () => {
  await validate();
  if (!Object.keys(errors.value).length) {
    loading.value = true;
    setTimeout(() => {
      loading.value = false;
      requestOrganization();
      showOrgAwait.value = true; // Show OrgAwait component
    }, 2000);
  } else {
    console.log('Validation failed:', errors.value);
  }
});


const requestOrganization = async () => {
    console.log('Form submitted with:', {
        id: orgID.value,
        email: email.value,
        message: message.value,
  });
}




</script>


<template>
<div class="container">
    <sideBar></sideBar>
 <RouterView />


 <div class="card width p-4 shadow-3 border-round" v-if="!showOrgAwait">
    <form @submit.prevent="onSubmit ">    
  <div class="text-center mb-5">
  <h2 >Organization Required</h2>
  <p class="text-500 line-height-2 ">You are currently not a part of an organization. To proceed, you can either join a pre-existing organization or <RouterLink to="createorg" class="no-underline " ><a class="font-semibold no-underline text-blue-400 cursor-pointer" >create your own</a></RouterLink>.</p>
  <Divider/>
      </div>
      <div class="text-center  mb-3 text-xl font-semibold">Request To Join Organization</div>             
      <p class="text-500 mx-auto text-sm text-center  "style="max-width: 35rem;"> Must provide Organization ID and Email of Organization Leader. Message is an optional field that will be sent directly to Organization Leader.</p>
      <div class="flex flex-column gap-1 mx-auto " style="min-height: 16rem; max-width: 20rem; ">
                 
                         <div class="field p-fluid mt-5">
                            <label class="text-900 font-medium mb-2">
                            Organization ID <span class="required-asterisk">*</span>
                            </label>
                            <InputText id="input" v-model="orgID" type="text" :class="{ 'p-invalid': errors.orgID}" placeholder="Enter ID" />
                            <small id="id-help" class="p-error">{{ errors.orgID }}</small>
                        </div>
                        <div class="field p-fluid ">
                            <label class="text-900 font-medium mb-2">Organization Leader's Email<span class="required-asterisk"> *</span>
                            </label>
                            <InputText id="input" v-model="email" type="email" :class="{ 'p-invalid': errors.email}" placeholder="Enter Email" />
                          <small id="email-help" class="p-error">{{ errors.email}}</small>
                        </div>
                        <div class="field p-fluid">
                            <label class="text-900 font-medium mb-2">Join Message</label>
                                <Textarea v-model="message" autoResize  rows="5" cols="30" :class="{ 'p-invalid': errors.message}" placeholder="Enter Join Message" />
                                <small id="message-help" class="p-error">{{ errors.message}}</small>
                        </div>
                    </div>
                    <div class="flex pb-5 mr-5 justify-content-end">
                        <Button label="Request to Join" raised type="submit" :loading="loading" iconPos="right"  />
                    </div>
                </form> 



  </div>
  <OrgAwait v-if="showOrgAwait" />

  </div>


</template>
 


 
<style scoped>


.width{
  width: 80%;
}


.container {
  display: flex;
  justify-content: center; /* Centers the child div horizontally */
  align-items: center; /* Centers the child div vertically */
  height: 100vh; /* Makes the container take the full viewport height */
}



.required-asterisk {
  color: rgb(253, 87, 87); /* Makes the asterisk red */
}
</style>
