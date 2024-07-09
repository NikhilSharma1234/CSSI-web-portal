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
    additionalField1: yup.string().required('This field is required').label('Additional Field 1'),
    additionalField2: yup.string().required('This field is required').label('Additional Field 2'),
    additionalField3: yup.string().required('This field is required').label('Additional Field 3'),
    additionalField4: yup.string().required('This field is required').label('Additional Field 4'),
    additionalField5: yup.string().required('This field is required').label('Additional Field 5'),
});

const { errors, validate, defineField, setFieldValue } = useForm({
    validationSchema: schema
});

const [selectedBrand] = defineField('selectedBrand')
const [selectedModel] = defineField('selectedModel')
const [selectedHardware] = defineField('selectedHardware')
const [selectedFirmware] = defineField('selectedFirmware')
const [selectedFrequency] = defineField('selectedFrequency')
const [joinEUI] = defineField('joinEUI')
const [additionalField3] = defineField('additionalField3')
const [additionalField4] = defineField('additionalField4')
const [additionalField5] = defineField('additionalField5')

const createOrganization = async () => {
    console.log('Form submitted with:', {
        selectedBrand: selectedBrand.value,
        selectedModel: selectedModel.value,
        selectedHardware: selectedHardware.value,
        selectedFirmware: selectedFirmware.value,
        selectedFrequency: selectedFrequency.value,
        joinEUI: joinEUI.value,
        additionalField3: additionalField3.value,
        additionalField4: additionalField4.value,
        additionalField5: additionalField5.value,
    });
}

const brand = ref(['Dragino Technology', 'Xignal', 'Cital']);
const model = ref(['Temperature', 'Humidity', 'Temperature & Humidity']);
const hardware = ref(['1.0.0']);
const firmware = ref(['p1.0.0', 'q1.0.1', 'r1.0.2']);
const frequency = ref(['FSB1', 'FSB2', 'FSB3', 'FSB4', 'FSB5'])

const showModelDropdown = ref(false);
const showHardwareDropdown = ref(false);
const showFirmwareDropdown = ref(false);
const showAdditionalField1 = ref(false);
const showAdditionalFields = ref(false);

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

watch(selectedFirmware, (newVal) => {
    if (newVal) {
        showAdditionalField1.value = true;
    }
});

watch(selectedFrequency, (newVal) => {
    if (newVal) {
        showAdditionalFields.value = true;
    }
});


const handleInput = (event: InputEvent) => {
  const input = event.target as HTMLInputElement;
  let value = input.value.toUpperCase(); // Convert input to uppercase

  // Filter out non A-F and 0-9 characters
  value = value.replace(/[^A-F0-9\s]/g, '');

  setFieldValue('joinEUI', value); // Update the v-model value
};
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
            <div class="col-12 md:col-6">
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

          <div v-if="showAdditionalField1" class="grid">
            <div class="col-12">
              <div class="flex flex-column mt-4">
                <label class="text-600 font-medium mb-2 ml-2">
                  Frequency Plan<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedFrequency" class="w-full " :options="frequency" placeholder="Select Option"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>
          </div>

          <div v-if="showAdditionalFields" class="grid">
            <div class="col-12">
              <div class="flex flex-column  mt-4">
                <label class="text-600 font-medium mb-2 ml-2">
                  Join-EUI<span class="required-asterisk"> *</span>
                </label>
                <InputMask @input="handleInput" id="basic" v-model="joinEUI"  mask="** ** ** ** ** ** ** **" placeholder="•• •• •• •• •• •• •• ••" />
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>

            <div class="col-12">
              <div class="flex flex-column mt-4">
                <label class="text-600 font-medium mb-2 ml-2">
                  Dev-EUI<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="additionalField3" class="w-full" :options="firmware" placeholder="Select Option"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>

            <div class="col-12">
              <div class="flex flex-column mt-4">
                <label class="text-600 font-medium mb-2 ml-2">
                  App-Key<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="additionalField4" class="w-full" :options="firmware" placeholder="Select Option"></Dropdown>
                <small id="selectedPurpose-help" class="p-error"></small>
              </div>
            </div>

            <div class="col-12">
              <div class="flex flex-column mt-4">
                <label class="text-600 font-medium mb-2 ml-2">
                 End-Device ID<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="additionalField5" class="w-full" :options="firmware" placeholder="Select Option"></Dropdown>
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

}

.required-asterisk {
  color: rgb(253, 87, 87);
  /* Makes the asterisk red */
}
</style>
