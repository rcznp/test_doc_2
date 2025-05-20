# WatchApp - Code Flow Documentation

## 🔄 Application Flow Overview

```mermaid
graph TD
    A[App Launch] --> B[MainActivity.onCreate]
    B --> C{Check Login Status}
    C -->|Not Logged In| D[LoginScreen]
    C -->|Logged In| E[HomeScreen]
    D -->|Login Success| E
    E -->|Background| F[Start Services]
    F --> G[WifiService]
    F --> H[SensorLoggingService]
```

## 📱 Entry Point: MainActivity

### 1. Application Launch
```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Initialize login cache
        loginCache = LoginCache(applicationContext)
        
        // Check initial login state
        val initialScreen = if (checkIfUserIsLoggedIn() && cachedUserId != null) {
            userIdState.value = cachedUserId
            Screen.Home
        } else {
            Screen.Login
        }
        
        // Set up the UI
        setContent {
            AppContent(...)
        }
    }
}
```

### 2. Screen Navigation Flow
```mermaid
sequenceDiagram
    participant MA as MainActivity
    participant AC as AppContent
    participant LS as LoginScreen
    participant HS as HomeScreen

    MA->>AC: setContent
    AC->>AC: Check currentScreen
    alt Login Screen
        AC->>LS: Render LoginScreen
        LS->>MA: onLoginSuccess
        MA->>AC: Update currentScreen
    else Home Screen
        AC->>HS: Render HomeScreen
        HS->>MA: onLogout
        MA->>AC: Update currentScreen
    end
```

## 🔐 Authentication Flow

### 1. Login Process
```kotlin
// LoginScreen.kt
@Composable
fun LoginScreen(
    onLoginSuccess: (String, String) -> Unit,
    ...
) {
    // 1. User enters credentials
    var username by remember { mutableStateOf("") }
    var password by remember { mutableStateOf("") }

    // 2. Login button click
    Button(onClick = {
        // 3. Check Wi-Fi connection
        if (!isWifiConnected(context)) {
            Toast.makeText(context, "Wi-Fi not connected", Toast.LENGTH_SHORT).show()
            return@Button
        }

        // 4. Send login request
        sendLoginDataToApi(username, password, coroutineScope) { result ->
            if (result == "Login Success!") {
                // 5. Save login state
                loginCache.saveLoginStatus(true)
                loginCache.saveUserId(username)
                // 6. Navigate to home
                onLoginSuccess(username, password)
            }
        }
    })
}
```

## 🔄 Background Services Flow

### 1. Service Initialization
```mermaid
sequenceDiagram
    participant MA as MainActivity
    participant WS as WifiService
    participant SS as SensorLoggingService

    MA->>WS: startForegroundService
    MA->>SS: startForegroundService
    WS->>WS: onStartCommand
    SS->>SS: onStartCommand
    WS->>WS: Start WiFi Monitoring
    SS->>SS: Start Sensor Monitoring
```

### 2. WifiService Flow
```kotlin
class WifiService : Service() {
    override fun onStartCommand() {
        // 1. Create WiFi suggestion
        val suggestion = WifiNetworkSuggestion.Builder()
            .setSsid("w03test3")
            .setWpa2Passphrase("Hmgics2025!")
            .build()

        // 2. Add network suggestion
        wifiManager.addNetworkSuggestions(listOf(suggestion))

        // 3. Start monitoring connection
        startWifiMonitoring()
    }
}
```

### 3. SensorLoggingService Flow
```kotlin
class SensorLoggingService : Service() {
    override fun onStartCommand() {
        // 1. Initialize sensors
        initializeSensors()

        // 2. Start data collection
        startHeartRateMonitoring()
        startLocationTracking()
        startStepCounting()

        // 3. Start data transmission
        startDataTransmission()
    }
}
```

## 📊 Data Flow

### 1. Sensor Data Collection
```mermaid
sequenceDiagram
    participant SS as SensorService
    participant S as Sensors
    participant MA as MainActivity
    participant API as Server

    SS->>S: Request Data
    S->>SS: Send Data
    SS->>MA: Broadcast Data
    MA->>MA: Update UI
    SS->>API: Transmit Data
```

### 2. Data Storage Flow
```kotlin
class LoginCache(private val context: Context) {
    // 1. Initialize secure storage
    private val masterKey = MasterKey.Builder(context)
        .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
        .build()

    // 2. Create encrypted preferences
    private val sharedPreferences = EncryptedSharedPreferences.create(
        context,
        "login_cache",
        masterKey,
        ...
    )

    // 3. Save data
    fun saveLoginStatus(isLoggedIn: Boolean) {
        sharedPreferences.edit() { 
            putBoolean("isLoggedIn", isLoggedIn) 
        }
    }
}
```

## 🔄 State Management

### 1. UI State Flow
```mermaid
graph TD
    A[User Action] --> B[State Update]
    B --> C[UI Recomposition]
    C --> D[Screen Update]
    D --> E[User Sees Change]
```

### 2. State Variables
```kotlin
// MainActivity.kt
private val dataSendingStatus = mutableStateOf("Not sending data")
private val gpsDataState = mutableStateOf("No GPS data yet")
private val latitudeState = mutableStateOf("...")
private val longitudeState = mutableStateOf("...")
private val userIdState = mutableStateOf("")
private val heartRateState = mutableStateOf("...")
```

## 🔍 Error Handling Flow

### 1. Permission Handling
```mermaid
sequenceDiagram
    participant MA as MainActivity
    participant P as Permission
    participant S as Service

    MA->>P: Request Permission
    alt Granted
        P->>MA: Permission Granted
        MA->>S: Start Service
    else Denied
        P->>MA: Permission Denied
        MA->>MA: Show Error
    end
```

### 2. Service Error Handling
```kotlin
try {
    startForegroundService(serviceIntent)
} catch (securityException: SecurityException) {
    Log.e("MainActivity", "Security Exception: ${securityException.message}")
    Toast.makeText(this, "Permission denied", Toast.LENGTH_LONG).show()
} catch (e: Exception) {
    Log.e("MainActivity", "Error: ${e.message}")
    Toast.makeText(this, "Service start failed", Toast.LENGTH_LONG).show()
}
```

## 📱 Screen Lifecycle

### 1. Screen State Management
```mermaid
graph TD
    A[Screen Created] --> B[State Initialized]
    B --> C[UI Rendered]
    C --> D[User Interaction]
    D --> E[State Update]
    E --> C
```

### 2. Screen Navigation
```kotlin
enum class Screen {
    Login,
    Home,
    OptionsPage
}

@Composable
fun AppContent(
    currentScreen: Screen,
    onNavigate: (Screen) -> Unit,
    ...
) {
    when (currentScreen) {
        Screen.Login -> LoginScreen(...)
        Screen.Home -> HomeScreen(...)
        Screen.OptionsPage -> OptionsPage()
    }
}
```

---

*This documentation shows the main code execution paths in the application. Each component is designed to work independently while maintaining communication through well-defined interfaces and state management.*
