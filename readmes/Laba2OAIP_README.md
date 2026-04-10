# Laba2OAIP - Ski Jump Animation & Simulation

## 📖 Overview
**Laba2OAIP** is a Delphi VCL desktop application that renders a 2D animated ski jump sequence. Originally developed as a laboratory assignment for Object-Oriented Programming & Algorithms (OAiP), the project demonstrates procedural graphics, frame-based animation, coordinate normalization, and modular software architecture.

## ✨ Features
- **Frame-Based Animation Engine:** Driven by a `TTimer` (40ms interval, ~25 FPS) with sequential phase progression.
- **Procedural Snowfall:** 50 dynamically generated snowflakes with randomized size, speed, aspect ratio, and rotation.
- **Multi-Stage Ski Jump Sequence:** Automated camera/character movement across 5 phases (approach, acceleration, takeoff, flight, landing).
- **Normalized Coordinate System:** Decouples logical positions from screen resolution using a `0.0–1.0` mapping system.
- **Interactive Debug Mode:** Real-time coordinate measurement, frame counter, and clipboard export.
- **Modular Architecture:** Separated concerns across dedicated units for rendering, audio, location, and character/ski logic.

## 🛠️ Prerequisites
- **IDE:** Embarcadero Delphi (RAD Studio) with VCL framework support
- **OS:** Windows (VCL & WinAPI dependencies)
- **Version Control:** Git
- **Assets:** Background audio file (default: `calmMind.mp3`)

## 🚀 Getting Started
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Laba2OAIP
   ```
2. Open `Laba2Film.dproj` in Delphi.
3. Update the media player path in `Main.dfm` if the audio file is located elsewhere:
   ```delphi
   // Main.dfm -> MediaPlayer1.FileName
   FileName = 'path\to\your\calmMind.mp3'
   ```
4. Build and run the project (`Ctrl + F9`).

## 🎮 Controls & Debugging
| Key | Action |
|-----|--------|
| `i` | Toggle debug mode (shows UI hints, enables mouse panning) |
| `q` | Set start point for coordinate measurement |
| `e` | Set end point for coordinate measurement |
| `r` | Copy measured coordinates to clipboard |
| Mouse Drag | Pan the scene (only active in debug mode) |

## 🏗️ Architecture & Design
### Coordinate System
The application uses a **normalized coordinate system** (`0.0` to `1.0`) managed by `PointConverter.pas`. This ensures resolution-independent positioning:
- `Convert()`: Maps logical `(X, Y)` to screen pixels.
- `ConvertBack()`: Maps screen pixels back to logical coordinates.
- `GetPixels()`: Calculates a dynamic scaling factor based on canvas dimensions.

### Animation Pipeline
1. `FPSTimer` increments the global frame counter (`allCadrs`).
2. Phase-specific logic updates `PLocation` (camera/character offset).
3. `FormPaint` triggers `NextPaint()`, which:
   - Renders the background/location
   - Draws character & ski frames (if within valid frame ranges)
   - Updates snowflake positions & redraws them
   - Applies debug overlays (if enabled)
4. `Invalidate()` schedules the next render cycle.

### Module Breakdown
| Unit | Responsibility |
|------|----------------|
| `Main.pas` | Application entry, animation loop, input handling, debug UI |
| `drawSomeThing.pas` | Procedural snowflake generation & rendering |
| `PointConverter.pas` | Coordinate normalization & pixel conversion utilities |
| `Location.pas` | Background/terrain rendering |
| `NikManTest.pas` | Character animation frames & positioning |
| `SkisPoles.pas` | Ski & pole rendering logic |
| `Music.pas` | Audio playback control |

## 📁 Project Structure
```
Laba2OAIP/
├── FlowCharts/          # Visio diagrams (.vsd) for module logic
├── Laba2Film.dpr        # Project entry point
├── Main.pas / .dfm      # Main form & animation controller
├── drawSomeThing.pas    # Snowflake rendering
├── PointConverter.pas   # Coordinate system utilities
├── Location.pas         # Terrain/background logic
├── NikManTest.pas       # Character animation
├── SkisPoles.pas        # Ski equipment rendering
├── Music.pas            # Audio management
└── отчет лаба ОАиП2лаба2.doc # Project report (Russian)
```

## ⚠️ Notes & Limitations
- **Hardcoded Asset Path:** The default MP3 path in `Main.dfm` is absolute. Update it to a relative path or your local directory before deployment.
- **Frame-Dependent Timing:** Animation speed is tied to the timer interval. Adjust `FPS.Interval` in `Main.dfm` to change playback speed.
- **Debug Mode Requirement:** Mouse panning and coordinate tools are intentionally disabled in production mode (`CanDebug := False`).
- **Flowchart Files:** `.vsd` files require Microsoft Visio or a compatible viewer (e.g., LibreOffice Draw, Visio Viewer).

## 📄 License
This project was developed for academic purposes. Use, modification, and distribution are permitted for educational and non-commercial use.

---
*Developed with Embarcadero Delphi | Laboratory Assignment: OAiP 2*