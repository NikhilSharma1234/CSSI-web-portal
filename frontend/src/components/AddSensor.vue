<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, watch } from 'vue';
import { useForm, useField } from 'vee-validate'
import * as yup from 'yup'

const schema = yup.object({
    selectedBrand: yup.string().required('Sensor Brand is required').label('Sensor Brand'),
    selectedModel: yup.string().required('Sensor Model is required').label('Sensor Model'),
    selectedHardware: yup.string().required('Hardware Version is required').label('Hardware Version'),
    selectedFirmware: yup.string().required('Firmware Version is required').label('Firmware Version'),
    selectedFrequency: yup.string().required('This field is required').label('Frequency'),
    joinEUI: yup.string().required('JoinEUI is required').label('JoinEUI'),
    devEUI: yup.string().required('DevEUI is required').label('DevEUI'),
    appKey: yup.string().required('App Key is required').label('App Key'),
    deviceID: yup.string().required('Device ID is required').label('Device ID'),
});

const { errors, validate, defineField, handleSubmit } = useForm({
    validationSchema: schema,
    validateOnMount: false
});

const { errorMessage: joinEUIError, validate: validateJoinEUI } = useField('joinEUI', {
    initialValue: '',
    rules: schema.fields.joinEUI
});

const [selectedBrand] = defineField('selectedBrand')
const [selectedModel] = defineField('selectedModel')
const [selectedHardware] = defineField('selectedHardware')
const [selectedFirmware] = defineField('selectedFirmware')
const [selectedFrequency] = defineField('selectedFrequency')
const [joinEUI] = defineField('joinEUI')
const [devEUI] = defineField('devEUI')
const [appKey] = defineField('appKey')
const [deviceID] = defineField('deviceID')






const brand = ref(['Dragino Technology', 'Xignal', 'Cital']);
const model = ref(['Temperature', 'Humidity', 'Temperature & Humidity']);
const hardware = ref(['1.0.0']);
const firmware = ref(['p1.0.0', 'q1.0.1', 'r1.0.2']);
const frequency = ref(['FSB1', 'FSB2', 'FSB3', 'FSB4', 'FSB5'])

const showModelDropdown = ref(false);
const showHardwareDropdown = ref(false);
const showFirmwareDropdown = ref(false);
const showAdditionalField1 = ref(false);
const showAdditionalField2 = ref(false);
const showAdditionalFields = ref(false);
const loading = ref(false);
const isFieldDisabled = ref(false);

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
        showAdditionalField2.value = true;
    }
});



const createOrganization = async () => {
    console.log('Form submitted with:', {
        selectedBrand: selectedBrand.value,
        selectedModel: selectedModel.value,
        selectedHardware: selectedHardware.value,
        selectedFirmware: selectedFirmware.value,
        selectedFrequency: selectedFrequency.value,
        joinEUI: joinEUI.value,
        devEUI: devEUI.value,
        appKey: appKey.value,
        deviceID: deviceID.value,
    });
}

const validateForm = handleSubmit (async () => {
    await validate();
    if (Object.keys(errors.value).length) {
        return console.log('Validation failed:', errors.value);
    }
    loading.value = true;
    setTimeout(() => {
        loading.value = false;
        createOrganization();
    }, 2000);
});

const generateAppKey = () => {
  const characters = '0123456789ABCDEF';
  let result = '';
  for (let i = 0; i < 32; i++) {
    result += characters.charAt(Math.floor(Math.random() * characters.length));
  }
  appKey.value = result;
};

const restrictInput = (e: KeyboardEvent) => {
    const char = e.key.toUpperCase(); 
    if (!/[0-9A-F]/.test(char)) {
        e.preventDefault(); 
    }
};

const validateJoinEUIField = async () => {
    await validateJoinEUI();
    if (joinEUIError.value) {
        console.log('JoinEUI validation failed:', joinEUIError.value);
        return false; 
    }
    return true; 
};

const showFields = async () => {
    const isValidJoinEUI = await validateJoinEUIField();
    if (isValidJoinEUI) {
        showAdditionalFields.value = true;
        isFieldDisabled.value = true;
    }
};

const resetForm = () => {
    isFieldDisabled.value = false;

    joinEUI.value = '';
    appKey.value ='';
    devEUI.value ='';
    deviceID.value='';

    // Hide additional fields
    showAdditionalFields.value = false;
};

const deviceValue = () => {
  deviceID.value = devEUI.value;
}


</script>

<template>
  <sideBar></sideBar>
  <RouterView />
  <div class="container">
    <div class="card width shadow-2">
      <div class="text-center">
        <h2>Register New Sensor</h2>
        <h5 class="-mt-3">To Application-ID</h5>
      </div>
      <TabView>
        <TabPanel header="QR Scanning Registration (Camera)">
          <div class="p-3">
            <div class="text-center text-600 text-sm">
              Register new device using the QR code on the back of your sensor
            </div>
            <Divider class="mt-4"/>
            <div class="text-center mt-4">
              <Button size="large">Use QR Code</Button>
            </div>
          </div>
        </TabPanel>
        <TabPanel header="Manual Registration (Default) ">
          <div class="text-center text-600 text-sm mt-3">
            Register new device using the default setup provided by LoRaWan repository
          </div>
          <Divider class="mt-4"/>
          <form @submit.prevent="validateForm()">
          <div class="grid">
            <div class="col-12 md:col-6">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mrgnB">
                  Sensor Brand<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedBrand" class="w-full md:w-12rem" :options="brand" placeholder="Select Brand" :class="{ 'p-invalid': errors.selectedBrand }"></Dropdown>
                <small id="selectedPurpose-help" class="p-error">{{ errors.selectedBrand }}</small>
              </div>
            </div>

            <div class="col-12 md:col-6" v-if="showModelDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mrgnM">
                  Sensor Model<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedModel" class="w-full md:w-12rem" :options="model" placeholder="Select Model" :class="{ 'p-invalid': errors.selectedModel }"></Dropdown>
                <small id="selectedPurpose-help" class="p-error">{{ errors.selectedModel }}</small>
              </div>
            </div>

            <div class="col-12 md:col-6" v-if="showHardwareDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mrgnH">
                 Hardware Version<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedHardware" class="w-full md:w-12rem" :options="hardware" placeholder="Select Version" :class="{ 'p-invalid': errors.selectedHardware }"></Dropdown>
                <small id="selectedPurpose-help" class="p-error">{{ errors.selectedHardware }}</small>
              </div>
            </div>
            <div class="col-12 md:col-6" v-if="showFirmwareDropdown">
              <div class="flex flex-column align-items-center mt-4">
                <label class="text-600 font-medium mb-2 mrgnF">
                  Firmware Version<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedFirmware" class="w-full md:w-12rem" :options="firmware" placeholder="Select Version" :class="{ 'p-invalid': errors.selectedFirmware }"></Dropdown>
                <small id="selectedPurpose-help" class="p-error">{{ errors.selectedFirmware }}</small>
              </div>
            </div>
          </div>

          <div v-if="showAdditionalField1" class="grid">
            <div class="col-12">
              <div class="flex flex-column mt-4">
                <label class="text-600 font-medium mb-2 ">
                  Frequency Plan<span class="required-asterisk"> *</span>
                </label>
                <Dropdown v-model="selectedFrequency" class="w-full " :options="frequency" placeholder="Select Option" :class="{ 'p-invalid': errors.selectedFrequency }"></Dropdown>
                <small id="selectedPurpose-help" class="p-error">{{ errors.selectedFrequency }}</small>
              </div>
            </div>
          </div>

          <div v-if="showAdditionalField2" class="grid">
            <div class="col-12">
              <div class="flex flex-column  mt-4">
                <label class="text-600 font-medium mb-2 ">
                  Join-EUI<span class="required-asterisk"> *</span>
                </label>
                <div >
                  <InputGroup>
                    <InputMask :disabled="isFieldDisabled" @keydown="restrictInput($event as KeyboardEvent)" v-model="joinEUI" mask="** ** ** ** ** ** ** **" placeholder="•• •• •• •• •• •• •• ••" :class="{ 'p-invalid': errors.joinEUI }"/>
                    <Button v-if="!isFieldDisabled" class="button-group" type="button" @click="showFields">Confirm</Button>
                    <Button v-else type="button" class="button-group" @click="resetForm">Reset</Button>
                </InputGroup>
                <small class="p-error">{{ errors.joinEUI }}</small>
                <div>
                
              </div>
              </div>
                
              </div>
            </div>
          </div>
          <div v-if="showAdditionalFields" class="grid">
            <div class="col-12">
              <div class="flex flex-column mt-2">
                <label class="text-600 font-medium mb-2 ">
                  Dev-EUI<span class="required-asterisk"> *</span>
                </label>
                <InputMask @keydown="restrictInput($event as KeyboardEvent)"  v-model="devEUI"  mask="** ** ** ** ** ** ** **" placeholder="•• •• •• •• •• •• •• ••" :class="{ 'p-invalid': errors.devEUI }"/>
                <small id="selectedPurpose-help" class="p-error">{{ errors.devEUI }}</small>
              </div>
            </div>

            <div class="col-12">
              <div class="flex flex-column ">
                <label class="text-600 font-medium mb-2 ">
                  App-Key<span class="required-asterisk"> *</span>
                </label>
                  <InputGroup>
                  <InputMask @keydown="restrictInput($event as KeyboardEvent)" v-model="appKey" mask="** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **" placeholder="•• •• •• •• •• •• •• •• •• •• •• •• •• •• •• ••"/>
                  <Button class="button-group " type="button" @click="generateAppKey">Generate</Button>
                </InputGroup>
                  <small id="selectedPurpose-help" class="p-error">{{ errors.appKey }}</small>
              </div>
            </div>

            <div class="col-12 mt-3">
              <div class="flex flex-column ">
                <label class="text-600 font-medium mb-2 ">
                 End-Device ID<span class="required-asterisk"> *</span>
                </label>
                <InputGroup>
                <InputMask id="basic" @keydown="restrictInput($event as KeyboardEvent)"  v-model="deviceID"  mask="** ** ** ** ** ** ** **" placeholder="•• •• •• •• •• •• •• ••" :class="{ 'p-invalid': errors.deviceID }"/>
                <Button class="button-group" type="button" @click="deviceValue">Use DevEUI</Button>
              </InputGroup>
                <small id="selectedPurpose-help" class="p-error">{{ errors.deviceID }}</small>
              </div>
            </div> 
          </div>
          <div class="flex pt-4 justify-content-center mt-5">
                <Button label="Add Sensor" size="large" :loading="loading"  type="submit"  />
            </div>
        </form>
        </TabPanel>
      
      </TabView>
    </div>
  </div>
</template>


<style scoped>


.container {
  display: flex;
  justify-content: center;
  margin-top: 5%;

}

.mrgnB {
  margin-right: 75px
}
.mrgnM {
  margin-right: 75px
}.mrgnH {
  margin-right: 40px
}.mrgnF {
  margin-right: 45px
}

.button-group{
justify-content: center;
width:124px;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 5px; /* Space between input mask and button */
}

.width{
  width: 640px;
}



.required-asterisk {
  color: rgb(253, 87, 87);
  /* Makes the asterisk red */
}



</style>
