<script lang="ts">
import { ref } from 'vue'
import { useStore } from 'vuex'
import { useRouter } from 'vue-router'
export default {
  name: "RegisterComponent",
 setup() {
    const name = ref('')
    const email = ref('')
    const password = ref('')
    const error = ref(null)

    const store = useStore()
    const router = useRouter()

    const Register = async () => {
      console.log(email.value)
        await store.dispatch('register', {
          email: email.value,
          password: password.value,
          name: name.value
        })
        router.push('/')
    }
    return { Register, name,email, password, error }
  }
};
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

    
    <form @submit.prevent="Register">
        <div class="field">
        <IconField iconPosition="left" class="mb-3">
            <InputIcon class="pi pi-envelope"></InputIcon>
            <InputText type="email" v-model="email" placeholder="Enter Your Email" />
        </IconField>
        </div>


        <IconField iconPosition="left" class="mb-3">
            <InputIcon class="pi pi-user"></InputIcon>
            <InputText type="text" v-model="name" placeholder="Enter Your Full Name" />
        </IconField>
        

        <IconField iconPosition="left" class="mb-5">
            <InputIcon class="pi pi-key"></InputIcon>
            <InputText id="email1" v-model="password" type="password" placeholder="Enter Your Password" />
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