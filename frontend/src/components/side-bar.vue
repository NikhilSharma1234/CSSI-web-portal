<script setup lang="ts">
import { usePrimeVue } from 'primevue/config';
import { useThemeStore } from '../stores/themeStore';
import { ref, onMounted, watch } from 'vue';
import Button from 'primevue/button';
import Sidebar from 'primevue/sidebar';
import store from '../store';
import { ListApplications } from '@/helpers';

const PrimeVue = usePrimeVue();
const themeStore = useThemeStore();
const themes = ref(['aura-light-cyan', 'aura-dark-cyan']);
const visible = ref(false);
const checked = ref(false);
let applicationsFromAPI = ref();


const organizations = ref([
  {
    name: 'Tech Solutions Inc.',
    items: [
      { name: 'Dashboard' },

    ],
  },
  {
    name: 'Innovative Minds LLC',
    items: [
      { name: 'Dashboard' },
    ],
  },
  {
    name: 'Global Enterprises Ltd.',
    items: [
      { name: 'Dashboard' },
    ],
  },
  {
    name: 'Future Vision Corp.',
    items: [
      { name: 'Dashboard' },
    ],
  },
]);

const applications = ref([
  {
    name: 'Tech Solutions Inc.',
    items: [
      { name: 'Dashboard' },
      {
        name: 'Sensors',
        items: [
          { name: 'Home-Temp1' },
          { name: 'Office-Temp2' }
        ]
      }
    ]
  },
  {
    name: 'Innovative Minds LLC',
    items: [
      { name: 'Dashboard' },
      {
        name: 'Sensors',
        items: [
          { name: 'Lab-Temp1' },
          { name: 'Field-Temp2' }
        ]
      }
    ]
  },
  {
    name: 'Global Enterprises Ltd.',
    items: [
      { name: 'Dashboard' },
      {
        name: 'Sensors',
        items: [
          { name: 'Warehouse-Temp1' },
          { name: 'Shipping-Temp2' }
        ]
      }
    ]
  },
  {
    name: 'Future Vision Corp.',
    items: [
      { name: 'Dashboard' },
      {
        name: 'Sensors',
        items: [
          { name: 'Factory-Temp1' },
          { name: 'Office-Temp2' }
        ]
      }
    ]
  }
]);

function toggleTheme() {
  const newTheme = themeStore.currentTheme === themes.value[0] ? themes.value[1] : themes.value[0];
  PrimeVue.changeTheme(themeStore.currentTheme, newTheme, 'theme-link', () => {
    themeStore.setTheme(newTheme);
    checked.value = newTheme === themes.value[0]; // Update the checked state
  });
}

const logout = async () => {
  await store.dispatch('logOut')
}

onMounted(async () => {
  checked.value = themeStore.currentTheme === themes.value[0];
  applicationsFromAPI = await ListApplications('admin')

});

watch(() => themeStore.currentTheme, (newTheme) => {
  checked.value = newTheme === themes.value[0];
});

</script>

<template>
  <Sidebar v-model:visible="visible">
    <template #container="{ closeCallback }">
      <div class="flex flex-column h-full py-2">
        <div class="flex align-items-center px-6">
          <RouterLink to="/" @click="closeCallback" class="ml-7 ">
            <span class="p-ripple " v-ripple><img src="../assets/unr2.png" alt="Image" height="70" /></span>
          </RouterLink>
          <span class="ml-8">
            <Button type="button" @click="closeCallback" icon="pi pi-angle-double-left" rounded
              class=" p-button-lg  mb-2 ml-3"></Button>
          </span>
        </div>
        <div class="overflow-y-auto">
          <ul class="list-none p-3 m-0">
            <li>
              <div v-ripple v-styleclass="{
                selector: '@next',
                enterClass: 'hidden',
                enterActiveClass: 'slidedown',
                leaveToClass: 'hidden',
                leaveActiveClass: 'slideup'
              }" class="p-3 flex align-items-center justify-content-between text-600 cursor-pointer p-ripple">
                <span class="font-medium">ORGANIZATIONS</span>
                <i class="pi pi-chevron-down"></i>
              </div>
              <ul class="list-none p-0 m-0 overflow-hidden">
                <li v-for="org in organizations" :key="org.name">
                  <a v-ripple v-styleclass="{
                    selector: '@next',
                    enterClass: 'hidden',
                    enterActiveClass: 'slidedown',
                    leaveToClass: 'hidden',
                    leaveActiveClass: 'slideup'
                  }"
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                    <i class="pi pi-folder mr-2"></i>
                    <span class="font-medium">{{ org.name }}</span>
                    <i class="pi pi-chevron-down ml-auto"></i>
                  </a>
                  <ul
                    class="list-none py-0 pl-3 pr-0 m-0 hidden overflow-y-hidden transition-all transition-duration-400 transition-ease-in-out">
                    <li v-for="item in org.items" :key="item.name">
                      <a v-ripple v-styleclass="{
                        selector: '@next',
                        enterClass: 'hidden',
                        enterActiveClass: 'slidedown',
                        leaveToClass: 'hidden',
                        leaveActiveClass: 'slideup'
                      }"
                        class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                        <i
                          :class="item.name === 'Dashboard' ? 'pi pi-chart-bar' + ' mr-2' : 'pi pi-folder-open' + ' mr-2'"></i>
                        <span class="font-medium">{{ item.name }}</span>
                      </a>
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>
          <ul class="list-none p-3 m-0">
            <li>
              <div v-ripple v-styleclass="{
                selector: '@next',
                enterClass: 'hidden',
                enterActiveClass: 'slidedown',
                leaveToClass: 'hidden',
                leaveActiveClass: 'slideup'
              }" class="p-3 flex align-items-center justify-content-between text-600 cursor-pointer p-ripple">
                <span class="font-medium">APPLICATIONS</span>
                <i class="pi pi-chevron-down"></i>
              </div>
              <ul class="list-none p-0 m-0 overflow-hidden">
                <li v-for="org in applications" :key="org.name">
                  <a v-ripple v-styleclass="{
                    selector: '@next',
                    enterClass: 'hidden',
                    enterActiveClass: 'slidedown',
                    leaveToClass: 'hidden',
                    leaveActiveClass: 'slideup'
                  }"
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                    <i class="pi pi-folder mr-2"></i>
                    <span class="font-medium">{{ org.name }}</span>
                    <i class="pi pi-chevron-down ml-auto"></i>
                  </a>
                  <ul
                    class="list-none py-0 pl-3 pr-0 m-0 hidden overflow-y-hidden transition-all transition-duration-400 transition-ease-in-out">
                    <li v-for="item in org.items" :key="item.name">
                      <a v-ripple v-styleclass="{
                        selector: '@next',
                        enterClass: 'hidden',
                        enterActiveClass: 'slidedown',
                        leaveToClass: 'hidden',
                        leaveActiveClass: 'slideup'
                      }"
                        class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                        <i
                          :class="item.name === 'Dashboard' ? 'pi pi-chart-bar' + ' mr-2' : 'pi pi-th-large' + ' mr-2'"></i>
                        <span class="font-medium">{{ item.name }}</span>
                        <i v-if="item.items && item.name !== 'Dashboard'" class="pi pi-chevron-down ml-auto"></i>
                      </a>
                      <ul v-if="item.items"
                        class="list-none py-0 pl-3 pr-0 m-0 hidden overflow-y-hidden transition-all transition-duration-400 transition-ease-in-out">
                        <li v-for="subItem in item.items" :key="subItem.name">
                          <a v-ripple v-styleclass="{
                            selector: '@next',
                            enterClass: 'hidden',
                            enterActiveClass: 'slidedown',
                            leaveToClass: 'hidden',
                            leaveActiveClass: 'slideup'
                          }"
                            class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                            <i
                              :class="subItem.name === 'Dashboard' ? 'pi pi-chart-bar' + ' mr-2' : 'pi pi-wave-pulse' + ' mr-2'"></i>
                            <span class="font-medium">{{ subItem.name }}</span>
                          </a>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </li>
              </ul>
            </li>
          </ul>

          <ul class="list-none p-3 m-0">
            <li>
              <div v-ripple v-styleclass="{
                selector: '@next',
                enterClass: 'hidden',
                enterActiveClass: 'slidedown',
                leaveToClass: 'hidden',
                leaveActiveClass: 'slideup'
              }" class="p-3 flex align-items-center justify-content-between text-600 cursor-pointer p-ripple">
                <span class="font-medium">ACCOUNT</span>
                <i class="pi pi-chevron-down"></i>
              </div>
              <ul class="list-none p-0 m-0 overflow-hidden">
                <li>
                  <a v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                    <i class="pi pi-cog mr-2"></i>
                    <span class="font-medium">Settings</span>
                  </a>
                </li>
                <li>
                  <a v-ripple
                    class="flex align-items-center cursor-pointer p-3 border-round text-700 hover:surface-100 transition-duration-150 transition-colors p-ripple">
                    <i class="pi pi-question-circle mr-2"></i>
                    <span class="font-medium">Help</span>
                    <p></p>
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
        <div class="mt-auto">
          <hr class="mb-3 mx-3 border-top-3 border-none surface-border" />
          <a class="m-2 flex align-items-center p-3 gap-2 border-round text-700">
            <Avatar image="https://primefaces.org/cdn/primevue/images/avatar/amyelsner.png" shape="circle" />
            <span class="font-bold mr-4">{{ store.state.user ? store.state.user['displayName'] : '' }}</span>
            <span class="pi pi-moon" style="font-size: 1.2rem"></span>
            <InputSwitch v-model="checked" @change="toggleTheme">Switch Theme</InputSwitch>
            <span class="pi pi-sun" style="font-size: 1.3rem"></span>
          </a>
        </div>
        <div class="d-grid mx-2">
          <Button class="w-full flex" severity="danger" type="button" @click="logout()" label="Log Out"></Button>
        </div>
      </div>
    </template>
  </Sidebar>
  <Button v-if="!visible" icon="pi pi-bars" @click="visible = true" class="toggle-btn" />
</template>


<style scoped>.toggle-btn {
  position: fixed;
  top: 30px;
  /* Adjust as needed */
  left: 30px;
  /* Adjust as needed */
  scale: 1.6;
}</style>