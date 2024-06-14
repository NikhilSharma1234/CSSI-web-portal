<script setup lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';
import { useRouter } from 'vue-router';
import { useForm } from 'vee-validate';
import * as yup from 'yup';

// Define the validation schema
const schema = yup.object({
  email: yup.string().required().email().label('Email address'),
  fullName: yup.string().required().max(40, 'Full name must be at most 40 characters long').label('Full Name').matches(/^(?=.*[a-zA-Z])[a-zA-Z-' ]{1,40}$/, {message: 'Full name must contain at least one letter and can only contain letters, spaces, hyphens, or apostrophes'}),
  password: yup.string().required().min(6).matches(/^\S*$/, 'Password must not contain spaces').max(25).label('Password'),
});

// Setup the form with VeeValidate
const { defineField, validate, handleSubmit, errors } = useForm({
  validationSchema: schema,
});
const [fullName] = defineField('fullName');
const [email] = defineField('email');
const [password]  = defineField('password');

// Firebase and Vuex setup
const store = useStore();
const router = useRouter();
const error = ref<string | null>(null);
const loading = ref(false)

// Register function
const register = async () => {
  try {
    await store.dispatch('register', {
      email: email.value,
      password: password.value,
      name: fullName.value
    });
    router.push('/');
  } catch (err: any) {
    console.error(err);
    error.value = err.message;
  }
};

const signInWithGoogle = async () => {
  try {
    await store.dispatch('signInWithGoogle');
    router.push('/');
  } catch (err: any) {
    console.error('Google sign-in failed:', err.message);
    error.value = err.message;
  }
};

// Handle form submission
const onSubmit = handleSubmit(async () => {
  await validate();
  if (!Object.keys(errors.value).length) {
  loading.value = true;
  setTimeout(() => {
        loading.value = false;
        register();
    }, 2000);
    
  
}

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
        <Button @click="signInWithGoogle()" label="Sign up with Google" severity="secondary" raised>
    <img src="../assets/google.png" alt="Google Logo" style="width: 24px; height: 24px; margin-right: 8px;" />
    Sign up with Google
  </Button>
    </div>

    
    <form @submit.prevent="onSubmit">
        <div class="field ">
        <label class="text-900 font-medium mb-2">Email</label>
        <IconField iconPosition="left">
            <InputIcon class="pi pi-envelope"></InputIcon>
            <InputText class="w-full weight" type="email" v-model="email" :class="{ 'p-invalid': errors.email}" placeholder="Enter Your Email" />
        </IconField>
        <small id="email-help" class="p-error">{{ errors.email }}</small>
        </div>

        <div class="field">
        <label class="text-900 font-medium mb-2">Full Name</label>
        <IconField iconPosition="left" class="">
            <InputIcon class="pi pi-user"></InputIcon>
            <InputText  class="w-full weight" type="text" v-model="fullName" :class="{ 'p-invalid': errors.fullName}" placeholder="Enter Your Full Name" />
        </IconField>
        <small id="fullName-help" class="p-error">{{ errors.fullName }}</small>
        </div>

        <div class="field">
        <label class="text-900 font-medium mb-2">Password</label>
        <IconField iconPosition="left">
            <InputIcon class="pi pi-key"></InputIcon>
            <InputText class="w-full weight" v-model="password" :class="{ 'p-invalid': errors.password}" type="password" placeholder="Enter Your Password" />
        </IconField>
        <small  id="fullName-help" class="p-error ">{{ errors.password }}</small>
        </div>


        <Button  :loading="loading" label="Sign up" icon="pi pi-user" class="w-full mt-3 height" type="submit"></Button>

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


.height{
    height: 7vh;
    font-size: 18px;
}

.weight{
    height: 6vh;
    font-size: 14px;
}

</style>