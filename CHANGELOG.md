# Changelog

All notable changes to the Water Twin project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-12-22

### Added

- **Command Monitoring Tab Functionality**
  - Clickable valve controls (VLVC01-VLVC10) - click to toggle open/closed state
  - Visual feedback: Green for open, Red for closed
  - Real-time valve state monitoring and updates
  
- **Pump Control Buttons**
  - Dedicated "Toggle PMP01" and "Toggle PMP02" buttons
  - Confirmation messages when pumps are toggled
  - Commands written to communication files
  
- **Data Capture Feature**
  - "Capture Data" button saves current sensor readings
  - Files saved to `data_captures/` directory with timestamps
  - Includes all sensor values (flows, pressures, tank levels)
  
- **Scenario Capture Feature**
  - "Capture Scenario" button saves current system state
  - User-friendly dialog for scenario naming
  - Files saved to `application/scenario_folder/` directory
  - Includes pump states, valve states, and sensor values
  
- **3D Inspection Integration**
  - "3D inspection" button in scenario testing interface
  - Launches 3D visualization in separate thread
  - Allows visual inspection of scenario configurations

- **Content for Empty Tabs**
  - Added placeholder content to Training tab
  - Added placeholder content to Profiles tab
  - Added placeholder content to Settings tab

### Changed

- **UI Language**: All French text converted to English throughout the application
- **Path Handling**: Replaced hardcoded paths with `pathlib` for cross-platform compatibility
- **Error Handling**: Comprehensive error handling added throughout the application
- **Image Loading**: Robust image loading with fallback to text-only buttons
- **Texture Loading**: Safe texture loading in 3D visualization with fallback colors

### Fixed

- **Image Loading Errors**
  - Fixed crashes when splash screen image is missing or corrupted
  - Fixed crashes when icon files are missing or corrupted
  - Added graceful fallback to colored backgrounds and text-only buttons
  
- **3D Visualization Crashes**
  - Fixed `AttributeError: 'NoneType' object has no attribute 'setMagfilter'` errors
  - Added `safe_entity()` and `safe_button()` helper functions
  - Models display with gray fallback colors when textures fail
  - Fixed "multiple values for keyword argument 'color'" errors
  
- **Tkinter Callback Errors**
  - Fixed callback errors when windows are closed
  - Added proper widget existence checks before scheduling callbacks
  - Wrapped `after()` calls in try-except blocks
  - Fixed errors in `OnRunning()`, `commandListinning()`, and `monitorVannes()` methods
  
- **Scenario File Handling**
  - Fixed `FileNotFoundError` for missing scenario files
  - Added helpful error messages instead of crashes
  - Fixed scenario filename generation (now uses scenario name, not date)
  - Added filename sanitization (replaces spaces and special characters)
  
- **Input Validation**
  - Fixed `ValueError` when empty fields are submitted
  - Added default values for `pas`, `marge`, and `k` parameters
  - Added validation for plotting parameters
  - Skip invalid entries with user feedback
  
- **Deprecation Warnings**
  - Fixed `ttkbootstrap.scrolled` deprecation warning
  - Updated imports to use `ttkbootstrap.widgets.scrolled`
  
- **Communication Module**
  - Fixed typo: `readCommnand()` → `readCommand()`
  - Added file existence checks before reading
  - Improved error handling for empty command dictionaries

### Technical Improvements

- **Code Organization**
  - Improved error handling patterns
  - Better separation of concerns
  - More maintainable code structure
  
- **Robustness**
  - Application continues to function even with missing assets
  - Graceful degradation when files are corrupted
  - Better user feedback for errors
  
- **Cross-Platform Compatibility**
  - Using `pathlib` instead of hardcoded paths
  - Relative path handling throughout
  - Better Windows/Linux/macOS compatibility

## [1.0.0] - Initial Release

### Features

- Digital twin simulation of water supply system
- Real-time hydraulic modeling with Euler Forward integration
- 2D GUI with real-time monitoring graphs
- 3D visualization with Ursina Engine
- Scenario management system
- File-based inter-process communication
- Support for 2 pumps, 10 valves, 2 tanks
- Multiple conduit monitoring

### Components

- Main GUI application (`application/app.py`)
- Hydraulic simulation model (`application/HydraulicModel.py`)
- 3D visualization (`visualisation/visualisation3D.py`)
- Communication system (`application/communication.py`)

---

## Notes

- Version numbers follow Semantic Versioning (MAJOR.MINOR.PATCH)
- Breaking changes will increment MAJOR version
- New features increment MINOR version
- Bug fixes increment PATCH version
