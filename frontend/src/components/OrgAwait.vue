<script setup lang="ts">
import sideBar from './side-bar.vue';


import { ref } from 'vue';
import { useForm } from 'vee-validate'
import { useRouter } from 'vue-router'
import * as yup from 'yup'

const router = useRouter()


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
        router.push('/')
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


 <div class="card width p-4 shadow-3 border-round">

  <div class="text-center mb-5">
  <h2 > Join Request Pending</h2>
  <Divider/>
      </div>         
      <p class="text-600 mx-auto pb-3 text-center  "style="max-width: 35rem;">You have sent out your request to join the organization *Enter ID Here*. Please wait patiently for the leader to respond to your request. If accepted, you will be taken to dashboard page.</p>



  </div>

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
  height: 80vh; /* Makes the container take the full viewport height */
}



.required-asterisk {
  color: rgb(253, 87, 87); /* Makes the asterisk red */
}
</style>