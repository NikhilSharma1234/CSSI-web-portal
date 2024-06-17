<script setup lang="ts">
import store from '@/store';
import { useForm } from 'vee-validate';
import { ref } from 'vue';
import * as yup from 'yup'

const schema = yup.object({
  email: yup.string().required().label('Email address')
})

const { defineField, validate, handleSubmit, errors } = useForm({
  validationSchema: schema
})

const [email] = defineField('email')
const loading = ref(false)
const error = ref<string | null>(null)

const sendResetEmail = async () => {
  try {
    await store.dispatch('sendResetEmail', {
      email: email.value,
    })
  } catch (err: any) {
    console.log(err)
  }
  alert('If there is an account with that email, it has been sent a password reset link')
}

const onSubmit = handleSubmit(async () => {
  await validate()
  if (!Object.keys(errors.value).length) {
    loading.value = true
    setTimeout(() => {
      loading.value = false
      sendResetEmail()
    }, 2000)
  }
})
</script>

<template>
  <div class="center-content">
    <div class="surface-card p-4 shadow-3 border-round w-full lg:w-4">
      <div class="text-center mb-6">
        <img src="../assets/unr2.png" alt="Image" height="50" class="mb-3" />
        <div class="text-900 text-3xl font-medium mb-3">Forgot Password</div>
        <span class="text-600 font-medium line-height-4">Get here by accident?</span>
        <RouterLink to="login" class="no-underline"><a
            class="font-semibold no-underline ml-2 text-blue-400 cursor-pointer p-ripple" v-ripple>Login</a>
        </RouterLink>
        <div class="text-600 font-medium mb-3 mt-3">Or</div>
        <span class="text-600 font-medium line-height-4">Enter your email to reset password</span>
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
        <div class="text-center mb-2">
          <small id="fullName-help" class="p-error">{{ error }}</small>
        </div>
        <Button :loading="loading" label="Send Password Reset Email" icon="pi pi-user" class="w-full height"
          type="submit" />
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

.height {
  height: 7vh;
  font-size: 18px;
}
</style>