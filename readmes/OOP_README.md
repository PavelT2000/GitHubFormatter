# OOP Lab 1: Space Vessel Management System

## 📖 Overview
A C# Windows Forms application designed to demonstrate core Object-Oriented Programming (OOP) principles through a space fleet management simulation. The project models a hierarchical spacecraft architecture, showcasing inheritance, polymorphism, abstraction, and encapsulation within a desktop UI environment.

## 🧠 OOP Concepts Demonstrated
| Concept | Implementation |
|---------|----------------|
| **Abstraction** | `SpaceVessel` abstract base class enforces a contract via `abstract void ExecuteMission()` and defines shared state (`ModelName`, `Fuel`). |
| **Inheritance** | Multi-level hierarchy: `SpaceVessel` → `CombatShip`/`TransportShip` → `Destroyer`/`CargoFreighter`. |
| **Polymorphism** | Runtime method resolution using `virtual`/`override` for `GetStatus()` and `ExecuteMission()`. Fleet management utilizes `List<SpaceVessel>` to handle heterogeneous types uniformly. |
| **Encapsulation** | Private backing fields with validated public properties (e.g., `Fuel` setter throws on negative values). Protected constructor restricts direct instantiation. |
| **Sealed Classes** | `Destroyer` and `CargoFreighter` are marked `sealed` to terminate the inheritance chain. |
| **Indexers** | `CargoFreighter` implements a custom indexer (`this[int index]`) for array-based cargo log management. |
| **Object Lifecycle** | Demonstrates finalizers (`~SpaceVessel()`) for cleanup notifications. |

## 🏗️ Architecture & Class Hierarchy
```
SpaceVessel (Abstract Base)
├── CombatShip
│   └── Destroyer (Sealed)
└── TransportShip
    └── CargoFreighter (Sealed)
```
**UI Layer:** `Form1` acts as the controller, managing fleet state and dynamically hosting input panels (`CombatInputControl`, `TransportInputControl`) based on user selection.

## 🛠️ Prerequisites
- **.NET SDK:** 6.0 or higher
- **IDE:** Visual Studio 2022, JetBrains Rider, or VS Code with C# Dev Kit
- **OS:** Windows (required for WinForms runtime)

## 🚀 Getting Started
1. **Clone & Navigate:**
   ```bash
   git clone <repository-url>
   cd OOP/Lab1
   ```
2. **Open & Build:**
   - Open `Lab1.csproj` in your IDE.
   - Restore dependencies and build:
     ```bash
     dotnet restore
     dotnet build
     ```
3. **Run:**
   ```bash
   dotnet run
   ```
   *(Or press `F5` in Visual Studio)*

## 🖥️ Usage
- **Initialize Fleet:** Click the `AddShip` button to instantiate and register default vessels (`Destroyer` and `CargoFreighter`) into the internal fleet list.
- **Dynamic UI Switching:** Use the ship type dropdown (`cmbShipType`) to dynamically load and display the corresponding input control (`CombatInputControl` or `TransportInputControl`) within the container panel.
- **Status Monitoring:** The main `ListBox` renders real-time status strings generated via polymorphic `GetStatus()` calls, displaying UID, model name, fuel percentage, and type-specific attributes.

## 📁 Project Structure
```
Lab1/
├── SpaceVessel.cs           # Abstract base class & core vessel logic
├── CombatShip.cs            # Combat-specific vessel implementation
├── TransportShip.cs         # Transport-specific vessel implementation
├── Destroyer.cs             # Sealed combat subclass with special abilities
├── CargoFreighter.cs        # Sealed transport subclass with cargo indexing
├── Form1.cs                 # Main application window & fleet controller
├── CombatInputControl.cs    # UI component for combat ship input
├── TransportInputControl.cs # UI component for transport ship input
├── Program.cs               # Application entry point
└── Lab1.csproj              # Project configuration
```

## 🔮 Future Enhancements
- **Dynamic Instantiation:** Wire `CombatInputControl` and `TransportInputControl` properties into `Form1.AddShip_Click` to create ships from user input.
- **Resource Management:** Replace finalizers with the `IDisposable` pattern for deterministic cleanup.
- **Architecture:** Migrate to MVVM or MVP for stricter separation of UI and business logic.
- **Persistence:** Add JSON/XML serialization to save and load fleet state.
- **Validation:** Centralize input validation and implement user-friendly error feedback.

## 📄 License
This project is developed for educational purposes. Refer to the repository root for licensing terms.