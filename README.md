A Wear OS app that authenticates users, collects sensor data (heart rate, steps, GPS), and sends it via MQTT to a broker. Telegraf listens on the broker, then forwards the data to InfluxDB for storage. 
The goal is to track worker activity and movement(??) patterns for machine learning-based behavior analysis and pattern recognition.
(??)
```mermaid
graph TD
    A[Wear OS App] -->|Sensor Data via MQTT| B[MQTT Broker]
    B -->|Subscribes & Forwards| C[Telegraf]
    C -->|Writes Data| D[InfluxDB]
```


## 🏗️ Architecture

### Core Components

1. **MainActivity**
   - Entry point of the application
   - Manages screen navigation
   - Handles permission requests
   - Coordinates background services

2. **Services**
   - `WifiService`: Manages Wi-Fi connectivity
   - `SensorLoggingService`: Collects sensor data
   - `TouchAccessibilityService`: Handles touch events(used to keep screen alive,dont need anymore)

3. **Data Management**
   - `LoginCache`: Secure storage for user credentials
   - Encrypted SharedPreferences for sensitive data

## 📊 Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant A as MainActivity.kt
    participant S as SensorLoggingService.kt
    participant W as WiFi
    participant TW as ThingWorx API(Authentication)
    participant DB as Influx DB (MQTT/InfluxDB)

    U->>A: Login
    A->>TW: Authenticate User
    TW-->>A: Authentication Success
    A->>S: Start Monitoring
    S->>S: Handle & Buffer Sensor Data
    A->>W: Check Wi-Fi Connection
    S->>DB: Transmit Data via MQTT
    DB->>DB: Store Data in InfluxDB
```


## 🛠️ Technical Implementation

### Login Process

1. User enters credentials
2. App checks Wi-Fi connectivity
3. Credentials are validated
4. Session is encrypted and stored
5. Background services are initialized

### Background Services

#### WifiService
- Manages Wi-Fi connections
- Handles silent reconnection
- Monitors connection status

#### SensorLoggingService
- Collects heart rate data
- Tracks GPS location
- Monitors step count(not working need activity recognition permission..)
- Transmits data to server

## 📱 UI Components

### Screens

1. **Login Screen**
   - Employee ID input
   - PIN input
   - Login button
   - Status messages

2. **Home Screen**
   - User information
   - Real-time sensor data
   - Wi-Fi status
   - Logout button

3. **Wifi Logs**
   to check if the wifi reconnection logics are running

5. **Voice Notes**
   currently sent to a flask server(ran locally for now)

## 🔧 Setup and Configuration

### Prerequisites
- Android Wear OS device
- Android Studio
- Minimum SDK version: 30
- Target SDK version: 30(need to be this or older because Eclipse Paho MQTT doesnt work for newer android api yet)

### Required Permissions(theres a whole lot of them,look at AndoridManifest.xml for them)
```xml
<uses-permission android:name="android.permission.BODY_SENSORS" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACTIVITY_RECOGNITION" />
```

## 🚀 Deployment

...

## 🔍 Troubleshooting

### Common Issues

1. **Wi-Fi Connection Issues(Home Screen Circle is Red)**
   - tap screen to keep the watch alive(somehow turns back on the servcies??)

2. **Sensor Data Not Updating**
   -Verify permissions,go to **apps->permission manager.**
   ensure health data sensors and accessibilty permissions on.Most often these are the ones that get reset.
   Location servcies needed for wifi reconnection(no idea why)
   **IMPT**Sometimes when reinstalling app through ADB the permissions may be reset.
   - Check sensor availability maybe watch dont have that sensor hardware


## 🤝 Support

For technical support or feature requests, please contact:
- Email: [Support Email]
- Issue Tracker: [Repository URL]

## 📄 License

[License Information]

---

*Documentation last updated: [Current Date]* 
