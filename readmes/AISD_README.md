# AISD

**Automated Interactive Spatial Discovery & Navigation System**

A lightweight, console-based application designed to identify a user's current location within a multi-story facility and provide deterministic, step-by-step navigation instructions to the nearest exit. Built with C# and .NET 8.0.

---

## 📋 Table of Contents
- [✨ Features](#-features)
- [🛠️ Prerequisites](#-prerequisites)
- [🚀 Getting Started](#-getting-started)
- [📖 Usage](#-usage)
- [🏗️ Architecture](#-architecture)
- [🔍 How It Works](#-how-it-works)
- [🔧 Customization](#-customization)
- [⚠️ Known Limitations & Future Improvements](#-known-limitations--future-improvements)
- [📄 License](#-license)

---

## ✨ Features
- **Interactive Location Identification**: Guided Q&A interface using wall color, room type, and lighting conditions to pinpoint the user's exact room.
- **Deterministic Path Navigation**: Graph-based routing that delivers sequential, human-readable instructions from the identified location to the facility exit.
- **State-Driven Logic**: Clean state-machine architecture for managing multi-step user input and decision branching.
- **Zero External Dependencies**: Pure .NET 8.0 console application with no third-party libraries.
- **Extensible Data Model**: Room metadata, navigation edges, and prompts are centralized for easy modification.

---

## 🛠️ Prerequisites
- [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later
- Terminal / Command Prompt / PowerShell
- Basic familiarity with console applications

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AISD
   ```

2. **Navigate to the project directory**
   ```bash
   cd Hz/Hz
   ```

3. **Restore dependencies & build**
   ```bash
   dotnet restore
   dotnet build
   ```

4. **Run the application**
   ```bash
   dotnet run
   ```

---

## 📖 Usage

Upon launch, the application enters an interactive loop:

1. **Location Identification Phase**
   - You will be prompted with questions about your surroundings (e.g., wall color, room description, lighting).
   - Respond by entering the corresponding number and pressing `Enter`.

2. **Navigation Phase**
   - Once your location is identified, the system switches to navigation mode.
   - Step-by-step instructions will be displayed. Press any key to advance to the next instruction.
   - The loop terminates when you reach the exit.

3. **Restart**
   - After reaching the exit, you can choose to restart the identification process.

> 💡 *Note: All prompts and navigation instructions are currently in Russian. Localization can be added by modifying the string resources in `AnswerSystem.cs`.*

---

## 🏗️ Architecture

```
Hz/
├── Hz.csproj          # .NET 8.0 project configuration
├── Program.cs         # Application entry point & main execution loop
├── AnswerSystem.cs    # State machine, Q&A logic, room identification
├── PathFinder.cs      # Directed graph structure & navigation iterator
└── AskAnsApi.cs       # (Not provided) Public facade/wrapper for AnswerSystem & PathFinder
```

### Core Components
| Component | Responsibility |
|-----------|----------------|
| `Program.cs` | Orchestrates the main loop, switches between identification and navigation phases, handles console I/O. |
| `AnswerSystem.cs` | Manages `AskState` enum, maps user inputs to room IDs using dictionaries, and generates contextual prompts. |
| `PathFinder.cs` | Stores a directed graph of room transitions (`Dictionary<int, Edge>`), iterates through navigation steps. |
| `AskAnsApi` | Acts as a public API layer (wrapper) exposing `FillDictionaries()`, `Start()`, `IsFound()`, `Get()`, `Set()`, and `GetNum()` to `Program.cs`. |

---

## 🔍 How It Works

### 1. Identification Phase
The system uses a **state machine** (`AskState.Color → description → additionalDesc → answering`) to progressively narrow down the user's location:
- **Color Selection**: Maps wall color to a subset of possible rooms.
- **Description Selection**: Filters rooms based on functional type (Lab, Gallery, Reactor, etc.).
- **Additional Context**: Uses lighting or secondary descriptors to finalize the room ID.
- Once identified, `numRoom` is set and the state transitions to `answering`.

### 2. Navigation Phase
The `PathFinder` class loads a **static directed graph** where each node (room) contains exactly one outgoing edge (next step). Calling `Next()`:
1. Retrieves the instruction for the current room.
2. Updates the internal cursor to the target room.
3. Returns the instruction string.
This creates a deterministic, linear path to the exit without requiring complex pathfinding algorithms.

---

## 🔧 Customization

### Adding New Rooms
1. Update `AnswerSystem.rooms` dictionary with the new room ID and description.
2. Add corresponding entries to `AnswerSystem.roomsDesc` if using a new `RoomState`.
3. Extend the `DescrPick[Color]()` methods to map new descriptions to the room ID.

### Modifying Navigation Routes
Edit `PathFinder.FillGraph()`:
```csharp
graph.Add(sourceRoomId, new Edge(targetRoomId, "Instruction text here"));
```
Ensure the graph remains acyclic and leads to room `0` (Exit).

### Changing Language
Replace hardcoded Russian strings in `AnswerSystem.cs` with your preferred language or implement a resource file (`.resx`) for localization.

---

## ⚠️ Known Limitations & Future Improvements

| Limitation | Suggested Improvement |
|------------|------------------------|
| No input validation (`int.Parse` throws on invalid input) | Wrap console reads in `int.TryParse()` with retry loops. |
| Hardcoded graph & decision tree | Externalize data to JSON/XML for runtime configuration. |
| Single-path navigation (no alternative routes) | Implement Dijkstra/A* for dynamic pathfinding. |
| Console-only UI | Migrate to a lightweight GUI (Avalonia, WPF) or web interface. |
| `AskAnsApi` wrapper not provided in snippet | Ensure public API matches internal `AnswerSystem`/`PathFinder` signatures. |

---

## 📄 License

This project is provided for educational and internal use. Modify and distribute as needed. For commercial deployment, ensure compliance with your organization's software licensing policies.

---

*Generated for technical documentation purposes. For questions or contributions, refer to the project maintainers or repository issue tracker.*