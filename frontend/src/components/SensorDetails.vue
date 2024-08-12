<script setup lang="ts">
import sideBar from './side-bar.vue';
import { ref, onMounted, watch } from 'vue';

const frequency = ref('United States 902-928 MHz, FSB 1');
const deviceid = ref('kaden-device1');
const deveui = ref('0021BE4A00013D31');
const appeui = ref('D3A61ADCCC31B2FF');
const date = ref('June 18, 2024 13:05:30');
const brand = ref('laird');
const model = ref('rs1xx-ext-temp-1w-sensor');
const hardware = ref('rev 4');
const firmware = ref('6.1_20_6_16');
const owner = ref('Kaden Nesch');

const value = ref('Time-Series');
const options = ref(['Time-Series', 'Bar']);

const chartType = ref('line'); 
const selectedDataset = ref('temperature'); 

const timesOptions = ['1H', '24H', '7D', '14D', '1M', '6M', 'All'];
const selectedTime = ref('1H');

const times = ref();

const selectTime = (time: string) => {
  selectedTime.value = time;
  times.value = null; 
  updateChart(); 
};

onMounted(() => {
  updateChart();
});

watch([value, selectedDataset], () => {
  chartType.value = value.value === 'Time-Series' ? 'line' : 'bar';
  updateChart();
});

const chartData = ref();
const chartOptions = ref();

const dataMap: { [key: string]: number[] } = {
  temperature: [22, 29, 23, 19, 24, 23, 25, 30],
  battery: [98, 97, 95, 94, 93, 92, 85, 79],
  humidity: [45, 50, 48, 60, 47, 49, 50, 39],
  soilMoisture: [30, 31, 33, 32, 34, 33, 35, 39],
};

const labelMap: { [key: string]: string } = {
  temperature: 'Temperature (°C)',
  battery: 'Battery (%)',
  humidity: 'Humidity (%)',
  soilMoisture: 'Soil Moisture (%)',
};

const maxDate = new Date();

const confirmTimeSelection = () => {
  if (times.value) {
    selectedTime.value = 'customRange';
  }
  updateChart();
};

const generateTimeLabels = (range: string, customRange?: [Date, Date]) => {
  const labels = [];
  let intervals = 6; 

  if (customRange) {
    const [start, end] = customRange;
    const duration = (end.getTime() - start.getTime()) / 1000 / 60; 
    const intervalDuration = duration / intervals;
    const daysDifference = Math.floor(duration / 1440); 

    for (let i = 0; i <= intervals; i++) {
      const time = new Date(start.getTime() + i * intervalDuration * 60 * 1000);
      if (daysDifference >= 6) {
        labels.push(time.toLocaleDateString());
      } else {
        labels.push(time.toLocaleString([], { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }));
      }
    }
  } else {
    const now = new Date();
    switch (range) {
      case '1H':
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 10 * 60 * 1000)); // 10-minute intervals
          labels.push(time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        }
        break;
      case '24H':
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 4 * 60 * 60 * 1000)); // 4-hour intervals
          labels.push(time.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
        }
        break;
      case '7D':
        intervals = 7;
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 24 * 60 * 60 * 1000)); // 1-day intervals
          labels.push(time.toLocaleDateString());
        }
        break;
      case '14D':
        intervals = 7;
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 2 * 24 * 60 * 60 * 1000)); // 2-day intervals
          labels.push(time.toLocaleDateString());
        }
        break;
      case '1M':
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 5 * 24 * 60 * 60 * 1000)); // 5-day intervals
          labels.push(time.toLocaleDateString());
        }
        break;
      case '6M':
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 30 * 24 * 60 * 60 * 1000)); // 1-month intervals
          labels.push(time.toLocaleDateString());
        }
        break;
      case 'All':
        intervals = 8; // 8 x-axis points for all data
        for (let i = intervals - 1; i >= 0; i--) {
          const time = new Date(now.getTime() - (i * 90 * 24 * 60 * 60 * 1000)); // 3-month intervals
          labels.push(time.toLocaleDateString());
        }
        break;
    }
  }

  return labels;
};


const updateChart = () => {
  chartData.value = setChartData(selectedDataset.value);
  chartOptions.value = setChartOptions(selectedDataset.value);
};

const setChartData = (dataset: string) => {
  const customRange = times.value ? times.value : undefined;
  const labels = generateTimeLabels(selectedTime.value, customRange);
  const data = dataMap[dataset];
  
 
  return {
    labels,
    datasets: [
      {
        label: labelMap[dataset],
        data: data.slice(0, labels.length), // Ensure data length matches labels length
        backgroundColor: chartType.value === 'bar' ? 'rgba(75, 192, 192, 0.2)' : 'rgba(75, 192, 192, 0.2)',
        borderColor: chartType.value === 'bar' ? 'rgba(75, 192, 192, 1)' : 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }
    ]
  };
};

const calculateStepSize = (maxValue: number) => {
  const magnitude = Math.pow(10, Math.floor(Math.log10(maxValue)));
  const residual = maxValue / magnitude;

  if (residual <= 1) return 0.2 * magnitude;
  if (residual <= 2) return 0.5 * magnitude;
  if (residual <= 5) return magnitude;
  return 2 * magnitude;
};

const setChartOptions = (dataset: string) => {
  const documentStyle = getComputedStyle(document.documentElement);
  const textColor = documentStyle.getPropertyValue('--text-color');
  const textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
  const surfaceBorder = documentStyle.getPropertyValue('--surface-border');

  const maxValue = Math.max(...dataMap[dataset]);
  const yAxisMax = maxValue + maxValue * 0.15;
  const stepSize = calculateStepSize(yAxisMax);
  const roundedMax = Math.ceil(yAxisMax / stepSize) * stepSize;

  return {
    maintainAspectRatio: false,
    plugins: {
      title: {
        display: true,
        align: 'start',
        position: 'top',
        text: 'SENSOR DATA',
        font: {
          size: 16
        }
      },
      legend: {
        labels: {
          color: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      },
      y: {
        beginAtZero: true,
        max: roundedMax,
        ticks: {
          stepSize: stepSize,
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder
        }
      }
    }
  };
  
};


</script>

<template>
  <div class="container">
    <sideBar></sideBar>
    <RouterView />

    <div class="card p-4 shadow-1 border-round scaled">
      <div class="mt- justify-content-center">
        <div class="text-center h-5">
          <h2>Sensor Name</h2>
          <h5>Application-ID</h5>
        </div>

        <TabView :scrollable="true">
          <TabPanel header="Sensor Information">
            <div class="grid two-column-layout mt-2">
              <div class="left-column">
                <div class="col-12 mb-2">
                  <div class="flex flex-column mt-4">
                    <label class="text-600 font-bold mb-2 text-sm">End-Device ID</label>
                    <InputText size="small" readonly class="w-10" :model-value="deviceid" />
                  </div>
                </div>

                <div class="col-12 mb-2">
                  <div class="flex flex-column mt-2">
                    <label class="text-600 font-bold mb-2 text-sm">Frequency</label>
                    <InputText readonly size="small" class="w-10" :model-value="frequency" />
                  </div>
                </div>

                <div class="col-12">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Dev-EUI</label>
                    <InputMask readonly class="w-10" mask="** ** ** ** ** ** ** **" :model-value="deveui" />
                  </div>
                </div>

                <div class="col-12 mb-2">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">App-EUI</label>
                    <InputMask size="small" readonly class="w-10" mask="** ** ** ** ** ** ** **" :model-value="appeui" />
                  </div>
                </div>

                <div class="col-12 mb-2">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Created At</label>
                    <div>{{ date }}</div>
                  </div>
                </div>
              </div>

              <div class="right-column">
                <div class="col-12 mb-4">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Brand</label>
                    <div>{{ brand }}</div>
                  </div>
                </div>
                <div class="col-12 mb-4">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Model</label>
                    <div>{{ model }}</div>
                  </div>
                </div>

                <div class="col-12 mb-4">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Hardware Version</label>
                    <div>{{ hardware }}</div>
                  </div>
                </div>

                <div class="col-12 mb-4">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Firmware Version</label>
                    <div>{{ firmware }}</div>
                  </div>
                </div>

                <div class="col-12">
                  <div class="flex flex-column">
                    <label class="text-600 font-bold mb-2 text-sm">Owner</label>
                    <div>{{ owner }}</div>
                  </div>
                </div>
              </div>
            </div>
          </TabPanel>

          <TabPanel header="Data Visualization">
            <div class="chart-container card">
              <Chart :type="chartType" style="height: 45vh; width: 85%;" :data="chartData" :options="chartOptions" />
              <SelectButton class="top-right-button" v-model="value" :options="options" aria-labelledby="basic" />
            </div>
            <div class="flex-wrap p-fluid">
              <div class="flex-auto ml-6">
                <div class="button-container -mt-6 mb-3">
                  <Button v-for="time in timesOptions" :key="time" :label="time" class="small" :severity="selectedTime === time ? 'primary' : 'secondary'" :text="selectedTime !== time"  @click="selectTime(time)" />
                </div>
                <label for="calendar-12h">Time Picker Selection</label>
                <InputGroup class="w-6 mt-2">
                  <Calendar class="w-6" id="calendar-12h" selectionMode="range" v-model="times" showTime hourFormat="12" :maxDate="maxDate" />
                  <Button @click="confirmTimeSelection">Confirm</Button>
                </InputGroup>
              </div>
            </div>

            <div class="flex mt-3 ml-6 justify-content-center">
              <Button class="mr-4" @click="selectedDataset = 'temperature'">Temperature</Button>
              <Button class="mr-4" @click="selectedDataset = 'battery'">Battery</Button>
              <Button class="mr-4" @click="selectedDataset = 'humidity'">Humidity</Button>
              <Button class="mr-4" @click="selectedDataset = 'soilMoisture'">Soil Moisture</Button>
            </div>
          </TabPanel>
          <TabPanel header="Live Data"></TabPanel>
          <TabPanel header="Payload Settings"></TabPanel>
        </TabView>
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
}

.chart-container {
  position: relative;
}

.scaled {
  width: 60%;
}

.top-right-button {
  position: absolute;
  top: 10px;
  right: 10px;
}

.small {
  padding: 2px;
  width: 4%;
  margin-right: 8px; /* Add space between buttons */
}

.button-container {
  display: flex;
}

.two-column-layout {
  display: flex;
}

.left-column,
.right-column {
  flex: 1;
}

.right-column {
  margin-left: 6rem;
  margin-top: 1.3rem;
}

.flex-column {
  display: flex;
  flex-direction: column;
}
</style>

