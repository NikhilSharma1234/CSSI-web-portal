import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateOrgView from '../views/CreateOrgView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ForgotPasswordView from '@/views/ForgotPasswordView.vue'
import JoinOrgView from '@/views/JoinOrgView.vue'
import OrgDashView from '@/views/OrgDashView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/createorg',
      name: 'CreateOrg',
      component: CreateOrgView
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'Signup',
      component: SignupView
    },
    {
      path: '/forgotpassword',
      name: 'Forgot Password',
      component: ForgotPasswordView
    },
    {
      path: '/joinorg',
      name: 'JoinOrg',
      component: JoinOrgView
    },
    {
      path: '/orgdash',
      name: 'Organization Dashboard',
      component: OrgDashView
    },
  ]
})

export default router
