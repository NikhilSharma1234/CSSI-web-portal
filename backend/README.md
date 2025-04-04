# Getting Started
1. install requirements.txt with ```bash pip install -r requirements.txt ```
2. Run the backend with python app.py

# Build with docker
1. Install docker
2. A docker container container can be built with the following command ```bash docker build -t flaskbackend . ```  


# Current End Points
# API Endpoints Documentation

## 1. `/dataButton` – **Method: `POST`**
Used for data visualization based on predefined time periods and aggregation intervals.

### **Request Format**
**Content-Type:** `application/json`

#### **Body Parameters**
| Parameter    | Type   | Required | Description |
|-------------|--------|----------|-------------|
| `data`      | `dict` | ✅       | Dictionary mapping sensor IDs to lists of payload types. |
| `period`    | `string` | ✅     | Time period for data retrieval. Supported values: `1H`, `24H`, `7D`, `14D`, `30D`, `6M`, `1Y`, `ALL`. |
| `aggregation` | `string` | ❌   | Time interval for aggregation (optional). Supported values: `1 Hour`, `1 Day`, `7 Days`, `1 Month`, `6 Months`. |

### **Response Format**
**Content-Type:** `application/json`

#### **Response Fields**
| Field         | Type    | Description |
|--------------|---------|-------------|
| `dev_eui`    | `string` | Unique identifier of the device. |
| `timestamp`  | `string` | ISO 8601 formatted timestamp. |
| `payload_type` | `string` | Type of payload returned. |
| `value`      | `float`  | Aggregated or raw value of the payload. |

---

## 2. `/data` – **Method: `POST`**
Retrieves time-series sensor data within a user-specified time range.

### **Request Format**
**Content-Type:** `application/json`

#### **Body Parameters**
| Parameter    | Type   | Required | Description |
|-------------|--------|----------|-------------|
| `data`      | `dict` | ✅       | Dictionary mapping sensor IDs to lists of payload types. |
| `start_time` | `string` | ✅     | Start time in ISO 8601 format. |
| `end_time` | `string` | ✅       | End time in ISO 8601 format. |

### **Response Format**
**Content-Type:** `application/json`

#### **Response Fields**
| Field         | Type    | Description |
|--------------|---------|-------------|
| `dev_eui`    | `string` | Unique identifier of the device. |
| `timestamp`  | `string` | ISO 8601 formatted timestamp. |
| `payload_type` | `string` | Type of payload returned. |
| `value`      | `float`  | Recorded value for the specified payload type. |

---

## 3. `/devices` – **Method: `POST`**
Returns the device type and its latest sensor readings.

### **Request Format**
**Content-Type:** `application/json`

#### **Body Parameters**
| Parameter   | Type   | Required | Description |
|------------|--------|----------|-------------|
| `sensor_ids` | `list` | ✅     | List of sensor IDs to query. |

### **Response Format**
**Content-Type:** `application/json`

#### **Response Fields**
| Field         | Type    | Description |
|--------------|---------|-------------|
| `dev_eui`    | `string` | Unique identifier of the device. |
| `type`       | `string` | Type of the device. |
| `lastReading` | `dict`  | Contains the most recent timestamp and recorded values. |
| `readings`   | `list`  | List of available sensor readings. Each entry contains: |
  - **`payload_value`** (`string`): Internal identifier of the payload.
  - **`display_name`** (`string`): Human-readable name of the data field.

---

## 4. `/export` – **Method: `POST`**
Exports historical sensor data for specified devices within a given time range.

### **Request Format**
**Content-Type:** `application/json`

#### **Body Parameters**
| Parameter   | Type   | Required | Description |
|------------|--------|----------|-------------|
| `devices`  | `list` | ✅       | List of device IDs to export data for. |
| `startTime` | `string` | ✅     | Start time in ISO 8601 format. |
| `endTime`   | `string` | ✅     | End time in ISO 8601 format. |

### **Response Format**
**Content-Type:** `application/json`

#### **Response Fields**
| Field       | Type   | Description |
|------------|--------|-------------|
| `data`     | `list` | List of recorded sensor values. Each entry contains: |
  - **`dev_eui`** (`string`): Device identifier.
  - **`timestamp`** (`string`): ISO 8601 formatted timestamp.
  - **`item_number`** (`integer`): Entry index.
  - Additional fields corresponding to sensor payloads.
| `mapping`  | `dict` | Metadata mapping for data fields, including: |
  - **`display_name`** (`string`): Human-readable label.
  - **`unit`** (`string`): Measurement unit.
  - **`description`** (`string`): Explanation of the data field.
  - **`sortable`** (`boolean`): Indicates if sorting is supported.
  - **`width`** (`integer`): Suggested column width for display.

---


# Setting Database Connections
This backend has a number of different environment variables that can be set by a .env file.

Example .env file:
``` 
CSSI_DATABASE_USERNAME=username
CSSI_DATABASE_PASSWORD=password
CSSI_DATABASE_HOST=tts.rd.unr.edu
CSSI_DATABASE_TABLE=postgres
```


