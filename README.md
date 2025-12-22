# Water Twin - Digital Twin of Water Supply System

A digital twin application for simulating and monitoring a water supply system **without physical sensors**. This project creates a virtual representation of a hydraulic water distribution network with real-time monitoring, 3D visualization, and scenario management capabilities.

## 📋 Overview

This application simulates a complete water supply system including:

- **2 Pumps** (PMP01, PMP02)
- **10 Valves** (VLV01-VLV10)
- **2 Water Tanks** (Tank 1, Tank 2)
- **Multiple Conduits** with flow monitoring
- **Pressure sensors** and **flow meters**

The system uses a mathematical hydraulic model based on Euler Forward integration to simulate water flow, pressure, and tank levels in real-time.

## 🏗️ Architecture

The codebase is organized into four main modules:

1. **`application/`** - Main GUI application with monitoring and control panels
   - `app.py` - Main application window with navigation
   - `twin_app.py` - Real-time monitoring interface
   - `scenario_app.py` - Scenario management and testing
   - `HydraulicModel.py` - Hydraulic simulation model
   - `communication.py` - Inter-process communication

2. **`model/`** - Mathematical models and equations
   - `HydraulicModel.py` - Core hydraulic simulation engine
   - `Model_math.py` - Mathematical equations

3. **`visualisation/`** - 3D visualization
   - `visualisation3D.py` - 3D scene with interactive valves and pumps
   - `virtual3D.py` - Alternative 3D view
   - `objet/` - 3D models (OBJ files)
   - `texture/` - Textures for 3D models

4. **`communication/`** - File-based IPC
   - `command.txt` - Commands from GUI to model
   - `capture.txt` - Sensor values from model to visualization

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Windows/Linux/macOS

### Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd watertwin-main
   ```

2. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify the communication directory exists:**
   The `communication/` folder should contain `command.txt` and `capture.txt` files.

### Running the Application

**Option 1: Run from main entry point (with splash screen):**

```bash
python main.py
```

**Option 2: Run directly (without splash screen):**

```bash
cd application
python app.py
```

**Option 3: Run 3D visualization separately:**

```bash
cd visualisation
python visualisation3D.py
```

## 🎮 Usage

### Main Application Features

1. **Twin Model (Real-time Monitoring)**
   - Start/Stop simulation
   - Monitor pump status, valve positions, tank levels
   - View flow rates and pressures
   - Real-time graphs and gauges (8 different monitoring graphs)
   - Launch 3D visualization window
   - **Command Monitoring Tab**:
     - Clickable valve controls (VLVC01-VLVC10) - click to toggle open/closed
     - Pump control buttons (Toggle PMP01/PMP02)
     - Data capture functionality - save current sensor readings
     - Scenario capture functionality - save current system state

2. **Scenarios**
   - Create and save operational scenarios
   - Test different valve/pump configurations
   - Replay recorded scenarios
   - 3D inspection mode - view scenarios in 3D visualization
   - Plot simulation results with customizable parameters

3. **Training Mode**
   - Interactive learning interface
   - System operation tutorials (coming soon)

4. **Profiles**
   - User profile management
   - Session preferences (coming soon)

5. **Settings**
   - Application configuration
   - Display preferences (coming soon)

### Controls

- **Pumps**: Toggle PMP01 and PMP02 on/off from Command Monitoring tab
- **Valves**:
  - Click directly on valve indicators in Command Monitoring tab to toggle
  - Control VLV01-VLV10 (open/closed) with visual feedback
- **3D View**: Click on valves in 3D to toggle them
- **Monitoring**: View real-time sensor data and system status
- **Data Capture**: Save sensor readings to `data_captures/` directory
- **Scenario Capture**: Save system state to `scenario_folder/` directory

## 🔧 Technical Details

### Hydraulic Model

The simulation uses a physics-based model with:

- **Euler Forward integration** for time-stepping
- **Resistance calculations** for pipes and valves
- **Pressure dynamics** based on flow rates
- **Tank capacity** and level tracking
- **Junction flow** calculations

Key parameters:

- Time step: 0.1 seconds (configurable)
- Tank areas: 54 m² each
- Multiple pipe resistances and inertias
- Valve resistance: 13,985,716.43 when closed

### Communication System

The application uses file-based inter-process communication:

- `communication/command.txt` - Commands (valve/pump states)
- `communication/capture.txt` - Sensor readings (flows, pressures, levels)

### 3D Visualization

Built with **Ursina Engine**:

- Interactive 3D models
- Real-time water level visualization
- Clickable valves and equipment
- Visual flow indicators

## 📁 Project Structure

```
watertwin-main/
├── main.py                 # Entry point with splash screen
├── application/             # Main GUI application
│   ├── app.py             # Main window
│   ├── twin_app.py        # Monitoring interface
│   ├── scenario_app.py    # Scenario management
│   ├── HydraulicModel.py  # Simulation model
│   ├── communication.py   # IPC module
│   └── assets/            # Icons and images
├── model/                  # Mathematical models
│   └── HydraulicModel.py  # Core simulation engine
├── visualisation/         # 3D visualization
│   ├── visualisation3D.py # Main 3D scene
│   ├── objet/             # 3D models (OBJ/MTL)
│   └── texture/           # Textures
└── communication/         # IPC files
    ├── command.txt        # Commands
    └── capture.txt        # Sensor data
```

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed

   ```bash
   pip install -r requirements.txt
   ```

2. **File not found errors**: Check that `communication/` directory exists
   - The application will create it automatically if missing
   - Ensure `command.txt` and `capture.txt` files are present

3. **3D models not loading**:
   - Verify `visualisation/objet/` and `visualisation/texture/` paths exist
   - **Note**: Corrupted or missing textures are handled gracefully - models will display with gray fallback colors

4. **Splash screen/image loading errors**:
   - Missing or corrupted images are handled gracefully
   - Application will continue with text-only buttons if icons are missing
   - Check `application/assets/` directory for icon files

5. **Tkinter callback errors after closing windows**:
   - Fixed in latest version - callbacks are properly cleaned up when windows close
   - If you see these errors, ensure you're using the latest code

6. **Scenario file errors**:
   - Invalid scenario files show helpful error messages
   - Empty or invalid parameter inputs use default values
   - Scenario files are saved to `application/scenario_folder/`

### Error Handling Improvements

The application now includes robust error handling for:

- ✅ Missing or corrupted image files (icons, splash screen)
- ✅ Corrupted 3D model textures (automatic fallback to gray)
- ✅ Invalid user inputs (default values applied)
- ✅ Missing scenario files (helpful error messages)
- ✅ Widget destruction callbacks (proper cleanup)
- ✅ Empty command dictionaries (graceful handling)

## 👤 Author

**MEME ANDERMON JUNIOR**

## 📝 License

This project appears to be a research/educational project. Please check with the author for licensing information.

## ✨ Recent Updates & Fixes

### Version 1.1 (Latest)

**New Features:**

- ✅ **Command Monitoring Tab**: Fully functional with clickable valve controls
- ✅ **Data Capture**: Save sensor readings with timestamps to `data_captures/` directory
- ✅ **Scenario Capture**: Save current system state as scenarios with user-defined names
- ✅ **3D Inspection**: Launch 3D visualization from scenario testing interface
- ✅ **Pump Controls**: Dedicated buttons for toggling PMP01 and PMP02
- ✅ **English Translation**: All UI text converted from French to English

**Bug Fixes:**

- ✅ Fixed image loading errors (missing/corrupted icons handled gracefully)
- ✅ Fixed texture loading in 3D visualization (fallback to gray when textures fail)
- ✅ Fixed Tkinter callback errors when windows are closed
- ✅ Fixed scenario file handling (proper error messages, filename sanitization)
- ✅ Fixed input validation (default values for empty fields)
- ✅ Fixed deprecation warnings (updated ttkbootstrap imports)
- ✅ Fixed path handling (using pathlib for portability)

**Improvements:**

- ✅ Robust error handling throughout the application
- ✅ Better user feedback with informative error messages
- ✅ Graceful degradation when assets are missing
- ✅ Improved code organization and maintainability

### Technical Improvements

- **Error Handling**: All image/texture loading wrapped in try-except blocks
- **Path Management**: Standardized on `pathlib` for cross-platform compatibility
- **Callback Management**: Proper cleanup of Tkinter callbacks to prevent errors
- **Input Validation**: Comprehensive validation for user inputs with sensible defaults
- **File I/O**: Robust file handling with proper error messages

## 🔮 Future Enhancements

- Machine learning integration for predictive maintenance
- Cloud connectivity for remote monitoring
- Advanced scenario analysis and comparison
- Export/import configurations
- Real-time data export (CSV, JSON)
- Historical data analysis and trending
- Multi-user support with profile management
