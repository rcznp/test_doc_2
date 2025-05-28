# 🪝 Log Tag Reference – WatchApp

This document summarizes all logging tags used across the app (especially in `SensorLoggingService` and `MainActivity`) and groups them by purpose. Each tag is followed by example messages and what they indicate.

---

## 📁 MQTT Connection & Publishing

| **Tag**              | **Description**                                                          |
| -------------------- | ------------------------------------------------------------------------ |
| `MQTT`               | General connection flow (attempt, success, failure)                      |
| `MQTT_Publish`       | When messages are successfully published to MQTT                         |
| `MQTT_Publish_Error` | When MQTT message publishing fails (retry logic included)                |
| `MQTT_NotConnected`  | When publish is attempted but client is disconnected                     |
| `AccelPublish`       | Used for aggressive accelerometer queue draining (high-volume condition) |
| `QueueSizes`         | Periodic size logging of all sensor queues before publishing             |

---

## 📲 Sensor Data Collection

| **Tag**              | **Description**                                                     |
| -------------------- | ------------------------------------------------------------------- |
| `AccelerometerData`  | Raw accelerometer values and timestamps                             |
| `AccelQueueSize`     | Size of the accelerometer queue before and after offering data      |
| `GyroscopeData`      | Raw gyroscope sensor values                                         |
| `HeartRateData`      | BPM values received from heart rate sensor                          |
| `LinearAccelData`    | Linear acceleration values (x/y/z)                                  |
| `RotationVectorData` | Orientation sensor output                                           |
| `StepDetectorData`   | Steps detected (typically 1.0 per step)                             |
| `AvailableSensor`    | All sensors printed during initialization                           |
| `SensorService`      | General logs for registration, permission issues, or fallback logic |

---

## 🌍 GPS & Location Updates

| **Tag**               | **Description**                                             |
| --------------------- | ----------------------------------------------------------- |
| `GPSData`             | InfluxDB-formatted GPS payload preview                      |
| `LocationCallback`    | Latitude/Longitude logs upon receiving new location updates |
| `GPSService`          | Location permission or update registration status           |
| `SensorService_check` | Check for permissions before proximity or GPS activation    |

---

## 🧠 Gesture & App Wake

| **Tag**        | **Description**                                                      |
| -------------- | -------------------------------------------------------------------- |
| `WristGesture` | Detects flicks, logs axis deltas, and whether a launch was triggered |
| `KeepAliveTap` | Logs periodic screen taps to keep app active in background           |
| `SimulateTap`  | Indicates when a simulated UI tap was made (for app wake or launch)  |

---

## 🔋 Power & Wake Lock

| **Tag**     | **Description**                                             |
| ----------- | ----------------------------------------------------------- |
| `PowerLock` | Logs when wake locks are acquired/released for GPS tracking |

---

## 📊 Queue Monitoring

| **Tag**        | **Description**                                         |
| -------------- | ------------------------------------------------------- |
| `QueueMonitor` | Logs snapshot sizes of each queue and total memory used |
| `QueueDump`    | Error logs in case of queue dump failures               |

---

## 🌐 Network / Wi-Fi

| **Tag**       | **Description**                                   |
| ------------- | ------------------------------------------------- |
| `WifiService` | Logs service startup and connection monitoring    |
| `MQTT`        | Logs Wi-Fi disconnection checks before publishing |

---

## 🛠️ Broadcasts to UI

| **Tag**         | **Description**                                              |
| --------------- | ------------------------------------------------------------ |
| `SensorService` | General logs for broadcasting data to the activity           |
| `Status`        | Broadcast status of whether MQTT publish succeeded or failed |

---

## 🧪 Testing & Receivers

| **Tag**        | **Description**                                                      |
| -------------- | -------------------------------------------------------------------- |
| `TestReceiver` | Logs whether the test broadcast receiver was registered or triggered |

---

## ⚙️ App Lifecycle & Navigation

| **Tag**            | **Description**                                                    |
| ------------------ | ------------------------------------------------------------------ |
| `MainActivity`     | Logs lifecycle events, service start, stop, and errors             |
| `ServiceLifecycle` | Logs when the OS might be killing the service (`onTaskRemoved`)    |
| `ForegroundCheck`  | Checks if the app is in the foreground before simulating a gesture |

---

## ❗ Error Handling

| **Tag**              | **Description**                                                         |
| -------------------- | ----------------------------------------------------------------------- |
| `MQTT_Publish_Error` | Catches publish errors, retries with exponential backoff                |
| `TestReceiver`       | Warns if trying to unregister a receiver that wasn't registered         |
| `GPSService`         | Logs missing permissions or SecurityExceptions from FusedLocationClient |

---
#REMINDER!!!
##need to do cache clearing for all the other queues too

