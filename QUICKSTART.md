# Quick Start Guide - Water Twin

## 🚀 Quick Setup (3 Steps)

### Step 1: Install UV (if not already installed)

**Windows (PowerShell):**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or using pip:

```bash
pip install uv
```

### Step 2: Create Virtual Environment and Install Dependencies

**Option A: Using UV (Recommended - Faster)**

```bash
# Create virtual environment and install dependencies in one command
uv venv

# Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install dependencies using UV
uv pip install -r requirements.txt
```

**Option B: Using UV with pyproject.toml (Alternative)**

```bash
# Create virtual environment
uv venv

# Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install dependencies from pyproject.toml
uv pip install -e .
```

**Option C: Traditional pip (Fallback)**

```bash
# Create virtual environment
python -m venv .venv

# Activate the virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Verify Structure

Make sure these directories exist:

- ✅ `application/` - Main GUI
- ✅ `model/` - Simulation models  
- ✅ `visualisation/` - 3D visualization
- ✅ `communication/` - IPC files (should have `command.txt` and `capture.txt`)

### Step 4: Run the Application

```bash
python main.py
```

> **Note:** For future runs, remember to activate your virtual environment first:
>
> - **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
> - **Windows (CMD):** `.venv\Scripts\activate.bat`
> - **macOS/Linux:** `source .venv/bin/activate`

## 📱 What You'll See

1. **Splash Screen** (3-4 seconds)
   - Shows "WATER TWIN v1.0" with loading bar

2. **Main Application Window**
   - Menu bar with 5 sections:
     - **Twin model** - Real-time monitoring (default view)
     - **Scenarios** - Scenario management
     - **Training** - Training mode
     - **Profiles** - User profiles
     - **Settings** - Configuration

3. **Twin Model Interface**
   - Start/Stop button to control simulation
   - Real-time monitoring panels
   - Graphs showing flow rates, pressures, tank levels
   - Button to launch 3D visualization

## 🎮 Basic Usage

### Starting the Simulation

1. Click **"Twin model"** in the menu (if not already selected)
2. Click the **Start** button (green play button)
3. Watch real-time data update in the monitoring panels
4. The 3D visualization window will open automatically

### Controlling the System

#### From Command Monitoring Tab

1. Click on **"command monitoring"** tab in the Twin Model interface
2. **Valves**: Click directly on any valve indicator (VLVC01-VLVC10) to toggle open/closed
   - Green = Open, Red = Closed
   - Changes are immediately applied to the simulation
3. **Pumps**: Use the "Toggle PMP01" and "Toggle PMP02" buttons
   - Confirmation messages will appear
4. **Data Capture**: Click "Capture Data" to save current sensor readings
   - Files saved to `data_captures/` directory with timestamps
5. **Scenario Capture**: Click "Capture Scenario" to save current system state
   - Enter a scenario name when prompted
   - Files saved to `application/scenario_folder/` directory

#### From 3D Visualization

- Click on valves in the 3D scene to toggle them
- Watch water levels in tanks change in real-time
- See water flow through conduits when valves are open
- Interactive tooltips show component information

### Using Scenarios

1. Click **"Scenarios"** in the main menu
2. **Test a Scenario**:
   - Select a scenario from the list
   - Click "Tester un scenario" (Test a scenario)
   - Configure simulation parameters (time step, margin, iterations)
   - View results in plots
   - Use "3D inspection" to visualize in 3D
3. **Create New Scenario**:
   - Use Command Monitoring tab to set desired state
   - Click "Capture Scenario" to save

## 🔧 Troubleshooting

### "Module not found" error

**If using UV:**

```bash
# Make sure virtual environment is activated, then:
uv pip install ttkbootstrap pillow numpy matplotlib ursina psutil
```

**If using pip:**

```bash
# Make sure virtual environment is activated, then:
pip install ttkbootstrap pillow numpy matplotlib ursina psutil
```

### "File not found" error for communication files

The `communication/` folder should exist at the root. If missing:

```bash
mkdir communication
touch communication/command.txt
touch communication/capture.txt
```

### 3D models not loading

- Check that `visualisation/objet/` contains `.obj` files
- Check that `visualisation/texture/` contains `.png` files
- **Note**: If textures are corrupted or missing, models will display with gray fallback colors - this is normal and the application will continue to work

### Texture loading warnings

- If you see warnings about textures not loading, this is expected if textures are corrupted
- The application handles this gracefully by using fallback colors
- The 3D visualization will still work, just without textures

### Application won't start

- Make sure you're running from the project root directory
- Check Python version: `python --version` (should be 3.7+)
- Ensure virtual environment is activated (you should see `(.venv)` in your terminal prompt)
- If using UV, verify installation: `uv --version`

## 📊 Understanding the System

### Components

- **2 Pumps** (PMP01, PMP02): Supply water to the system
- **10 Valves** (VLV01-VLV10): Control water flow
- **2 Tanks**: Store water (Tank 1, Tank 2)
- **Multiple Conduits**: Transport water between components

### Sensor Data

- **CADC##**: Flow rate in conduit ##
- **CAPC##**: Pressure in conduit ##
- **CANTK#**: Water level in tank #
- **CANTK#RATE**: Rate of change of tank # level

### Commands

- **PMP##**: 0 = off, 1 = on
- **VLV##**: 0 = closed, 1 = open

## 🎯 Next Steps

1. **Explore Scenarios**: Click "Scenarios" to create and test different configurations
2. **Monitor Performance**: Watch CPU and RAM usage in the monitoring panel
3. **Experiment**: Try different valve combinations and observe system behavior
4. **3D Interaction**: Use the 3D view to visually understand system topology

## 💡 Tips

- **Start with both pumps ON and all valves OPEN** to see maximum flow
- **Close valves gradually** to see pressure changes in real-time graphs
- **Monitor tank levels** - they fill when inflow > outflow
- **Use Command Monitoring tab** for quick valve/pump control
- **Capture data** during interesting system states for later analysis
- **Create scenarios** for common operational configurations
- **Use 3D inspection** to visually understand system topology
- **Watch the graphs** - they update in real-time showing system dynamics

## 🆕 What's New

### Latest Updates (v1.1)

- ✅ **Clickable Valve Controls**: Click directly on valve indicators to toggle them
- ✅ **Data Capture**: Save sensor readings with timestamps
- ✅ **Scenario Capture**: Save system states for later replay
- ✅ **Improved Error Handling**: Application handles missing/corrupted files gracefully
- ✅ **English UI**: All text converted to English
- ✅ **Better Feedback**: Informative error messages and confirmations
- ✅ **Robust 3D Visualization**: Handles corrupted textures without crashing

### Key Features

- **Real-time Monitoring**: 8 different graphs showing various system parameters
- **Interactive Controls**: Direct manipulation of valves and pumps
- **3D Visualization**: Interactive 3D scene with clickable components
- **Scenario Management**: Save, load, and test different configurations
- **Data Export**: Capture sensor readings for analysis
