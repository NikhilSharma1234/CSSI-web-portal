<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, watch } from 'vue';
import { useForm } from 'vee-validate'
import * as yup from 'yup'

const schema = yup.object({
    selectedBrand: yup.string().required('Sensor Brand is required').label('Sensor Brand'),
    selectedModel: yup.string().required('Sensor Model is required').label('Sensor Model'),
    selectedHardware: yup.string().required('Hardware Version is required').label('Hardware Version'),
    selectedFirmware: yup.string().required('Firmware Version is required').label('Firmware Version'),
});

const { errors, validate, defineField } = useForm({
    validationSchema: schema
});

const [selectedBrand] = defineField('selectedBrand')
const [selectedModel] = defineField('selectedModel')
const [selectedHardware] = defineField('selectedHardware')
const [selectedFirmware] = defineField('selectedFirmware')

const createOrganization = async () => {
    console.log('Form submitted with:', {
        selectedBrand: selectedBrand.value,
        selectedModel: selectedModel.value,
        selectedHardware: selectedHardware.value,
        selectedFirmware: selectedFirmware.value,
    });
}

const brand = ref(['Dragino Technology', 'Xignal', 'Cital']);
const model = ref(['Temperature', 'Humidity', 'Temperature & Humidity']);
const hardware = ref(['1.0.0']);
const firmware = ref(['p1.0.0', 'q1.0.1', 'r1.0.2']);

const showModelDropdown = ref(false);
const showHardwareDropdown = ref(false);
const showFirmwareDropdown = ref(false);


watch(selectedBrand, (newVal) => {
    if (newVal) {
        showModelDropdown.value = true;
        if (model.value.length === 1) {
            selectedModel.value = model.value[0];
        }
    }
});

watch(selectedModel, (newVal) => {
    if (newVal) {
        showHardwareDropdown.value = true;
        if (hardware.value.length === 1) {
            selectedHardware.value = hardware.value[0];
        }
    }
});

watch(selectedHardware, (newVal) => {
    if (newVal) {
        showFirmwareDropdown.value = true;
        if (firmware.value.length === 1) {
            selectedFirmware.value = firmware.value[0];
        }
    }
});
</script>

<template>
      <sideBar></sideBar>
      <RouterView />
  <div class="container">
    <div class="card w-min shadow-2">
      <div class="text-center">
        <h2>Register New Sensor</h2>
        <h5 class="-mt-3">To Application-ID</h5>
      </div>
      <TabView>
        <TabPanel header="QR Code Registration">
          <div class="p-3">
            <div class="text-center text-600 text-sm">
              Register new device using the QR code on the back of your sensor
            </div>
            <Divider class="mt-4"/>
            <div class="text-center mt-4">
              <Button outlined>Use QR Code</Button>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Default Setup Registration">
          <div class="text-center text-600 text-sm mt-3">
            Register new device using the default setup provided by LoRaWan repository
          </div>
          <Divider class="mt-4"/>

          <div class="grid">
            <div class="col-12 md:col-6" v-if="true">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mr-7">
                  Sensor Brand<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedBrand" class="w-full md:w-12rem" :options="brand" placeholder="Select Brand"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>

            <div class="col-12 md:col-6" v-if="showModelDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mr-7">
                  Sensor Model<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedModel" class="w-full md:w-12rem" :options="model" placeholder="Select Model"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>

            <div class="col-12 md:col-6" v-if="showHardwareDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mr-5">
                  Hardware Version<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedHardware" class="w-full md:w-12rem" :options="hardware" placeholder="Select Version"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>
            <div class="col-12 md:col-6" v-if="showFirmwareDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mr-5">
                  Firmware Version<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedFirmware" class="w-full md:w-12rem" :options="firmware" placeholder="Select Version"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>
          </div>
        </TabPanel>
      </TabView>
    </div>
  </div>
</template>

 

 
<style scoped>



.container {
  display: flex;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.required-asterisk {
    color: rgb(253, 87, 87);
    /* Makes the asterisk red */
}

</style>