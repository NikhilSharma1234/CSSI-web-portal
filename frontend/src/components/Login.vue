<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const checked = ref(false)
const loading = ref(false)
const store = useStore()
const router = useRouter()
const error = ref<string | null>(null)

const schema = yup.object({
  email: yup.string().required().label('Email address'),
  password: yup.string().required().label('Password')
})

const { defineField, validate, handleSubmit, errors } = useForm({
  validationSchema: schema
})

const [email] = defineField('email')
const [password] = defineField('password')

const login = async () => {
  try {
    await store.dispatch('logIn', {
      email: email.value,
      password: password.value
    })
    router.push('/')
  } catch (err: any) {
    console.error(err)
    error.value = 'Login failed. Please check your email and password'
  }
}

const signInWithGoogle = async () => {
  try {
    await store.dispatch('signInWithGoogle')
    router.push('/')
  } catch (err: any) {
    console.error('Google sign-in failed:', err.message)
    error.value = 'Google sign-in failed'
  }
}

const onSubmit = handleSubmit(async () => {
  await validate()
  if (!Object.keys(errors.value).length) {
    loading.value = true
    setTimeout(() => {
      loading.value = false
      login()
    }, 2000)
  }
})

const routeToForgotPassword = () => {
  router.push('/forgotpassword')
}
</script>

<template>
  <div class="center-content">
    <div class="surface-card p-8 shadow-3 border-round w-full lg:w-4">
      <div class="text-center mb-6">
        <img src="../assets/unr2.png" alt="Image" height="50" class="mb-3" />
        <div class="text-900 text-3xl font-medium mb-3">Welcome Back!</div>
        <span class="text-600 font-medium line-height-4">Don't have an account?</span>
        <RouterLink to="signup" class="no-underline"><a
            class="font-semibold no-underline ml-2 text-blue-400 cursor-pointer p-ripple" v-ripple>Signup</a>
        </RouterLink>
        <div class="text-600 font-medium mb-3 mt-3">Or</div>
        <Button @click="signInWithGoogle()" label="Sign up with Google" severity="secondary" raised>
          <img src="../assets/google.png" alt="Google Logo" style="width: 24px; height: 24px; margin-right: 8px" />
          Sign in with Google
        </Button>
      </div>

      <form @submit.prevent="onSubmit">
        <div class="field">
          <label class="text-900 font-medium mb-2">Email</label>
          <IconField iconPosition="left">
            <InputIcon class="pi pi-envelope"></InputIcon>
            <InputText class="w-full weight" type="email" v-model="email" :class="{ 'p-invalid': errors.email }"
              placeholder="Enter Your Email" />
          </IconField>
          <small id="email-help" class="p-error">{{ errors.email }}</small>
        </div>

        <div class="field">
          <label class="text-900 font-medium mb-2">Password</label>
          <IconField iconPosition="left">
            <InputIcon class="pi pi-key"></InputIcon>
            <InputText class="w-full weight" v-model="password" :class="{ 'p-invalid': errors.password }" type="password"
              placeholder="Enter Your Password" />
          </IconField>
          <small id="fullName-help" class="p-error">{{ errors.password }}</small>
        </div>
        <div class="flex align-items-center justify-content-between mb-3">
          <div class="flex align-items-center mt-2">
            <Checkbox id="rememberme1" :binary="true" v-model="checked" class="mr-2"></Checkbox>
            <label for="rememberme1">Remember me</label>
          </div>
          <a @click="routeToForgotPassword"
            class="font-semibold no-underline ml-2 text-blue-400 cursor-pointer p-ripple">Forgot password?</a>
        </div>
        <div class="text-center mb-2">
          <small id="fullName-help" class="p-error">{{ error }}</small>
        </div>
        <Button :loading="loading" label="Sign in " icon="pi pi-user" class="w-full height" type="submit"></Button>
      </form>
    </div>
  </div>
</template>



<style scoped>
.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}
.height{
    height: 5vh;
    font-size: 18px;
}

.weight{
    height: 4vh;
    font-size: 14px;
}
</style>