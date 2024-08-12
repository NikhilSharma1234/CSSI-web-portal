import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateOrgView from '../views/CreateOrgView.vue'
import LoginView from '@/views/LoginView.vue'
import SignupView from '@/views/SignupView.vue'
import ForgotPasswordView from '@/views/ForgotPasswordView.vue'
import JoinOrgView from '@/views/JoinOrgView.vue'
import OrgDashView from '@/views/OrgDashView.vue'
import SensorView from '@/views/SensorView.vue'
import AddSensorView from '@/views/AddSensorView.vue'
import CreateAppView from '@/views/CreateAppView.vue'
import SensorDetailsView from '@/views/SensorDetailsView.vue'

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
      path: '/createApp',
      name: 'Create Application',
      component: CreateAppView
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
    {
      path: '/sensor',
      name: 'Application Sensor Dashboard',
      component: SensorView
    },
    {
      path: '/addsensor',
      name: 'Add Sensor',
      component: AddSensorView
    },
    {
      path: '/sensordetails',
      name: 'Sensor Details',
      component: SensorDetailsView
    },


  ]
})

export default router
