<script setup lang="ts">
import { useForm } from 'vee-validate';
import * as yup from 'yup';

const schema = yup.object({
  email: yup.string().required().email().label('Email address'),
  fullName: yup.string().required().label('Full name').matches(/^[a-zA-Z ]+$/),
  password: yup.string().required().min(6).label('Password').matches(/^.{6,20}$/),
  passwordConfirm: yup
    .string()
    .oneOf([yup.ref('password')], 'Passwords must match')
    .required()
    .label('Password confirmation'),
});

const { defineField, handleSubmit, resetForm, errors } = useForm({
  validationSchema: schema,
});

const [fullName] = defineField('fullName');
const [email] = defineField('email');
const [password] = defineField('password');
const [passwordConfirm] = defineField('passwordConfirm');


const onSubmit = handleSubmit((values) => {
  console.log('Submitted with', values);
});


</script>

<template>
<div class="center-content">
<div class="surface-card p-4 shadow-3 border-round w-full lg:w-4">
    <div class="text-center mb-6">
        <img src="../assets/unr2.png" alt="Image" height="50" class="mb-3" />
        <div class="text-900 text-3xl font-medium mb-3">Create your account</div>
        <span class="text-600 font-medium line-height-4">Already have an account?</span>
        <a class="font-medium no-underline ml-2 text-blue-500 cursor-pointer p-ripple" v-ripple>Login</a>
        <div class="text-600 font-medium mb-3 mt-3">Or</div>
        <Button label="Sign up with Google" severity="secondary" raised>
    <img src="../assets/google.png" alt="Google Logo" style="width: 24px; height: 24px; margin-right: 8px;" />
    Sign up with Google
  </Button>
    </div>

    
    <form @submit="onSubmit">
        <div class="field">
        <IconField iconPosition="left" class="mb-3">
            <InputIcon class="pi pi-envelope"></InputIcon>
            <InputText v-model="email" :class="{ 'p-invalid': errors.email}" type="email" placeholder="Enter Your Email" />
        </IconField>
        <small id="email-help" class="p-error">
            {{ errors.email }}
          </small>
        </div>


        <IconField iconPosition="left" class="mb-3">
            <InputIcon class="pi pi-user"></InputIcon>
            <InputText type="email" placeholder="Enter Your Full Name" />
        </IconField>
        

        <IconField iconPosition="left" class="mb-5">
            <InputIcon class="pi pi-key"></InputIcon>
            <InputText id="email1" type="text" placeholder="Enter Your Password" />
        </IconField>
   

        <Button label="Sign up" icon="pi pi-user" class="w-full" type="submit"></Button>
    </form>
</div>
</div>
</template>

<style scoped>
.center-content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

</style>