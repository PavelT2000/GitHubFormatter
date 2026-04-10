# OOPLab1: Space Fleet Management System

## 📖 Overview
**OOPLab1** is a C# Windows Forms application designed to demonstrate core Object-Oriented Programming (OOP) principles through a simulated space fleet management system. The project models a hierarchy of spacecraft, manages their operational states, and provides an interactive UI for dynamic ship creation, status monitoring, and mission execution.

Built as an educational laboratory project, it bridges theoretical OOP concepts with practical WinForms UI development.

---

## ✨ Key Features
- **Dynamic Ship Creation**: Instantiate combat or transport vessels at runtime via modular input controls.
- **Polymorphic Mission Execution**: Execute missions with behavior defined per vessel type.
- **Real-Time Status Tracking**: Monitor fuel levels, unique identifiers, and specialized attributes.
- **Input Validation & Error Handling**: Robust parsing and exception handling for user inputs.
- **Modular UI Architecture**: Swappable `UserControl` panels for different ship categories.

---

## 🏗️ Architecture & OOP Principles

| Concept | Implementation |
|---------|----------------|
| **Abstraction** | `SpaceVessel` abstract base class defines common state (`Fuel`, `ModelName`, `_uid`) and enforces `ExecuteMission()`. |
| **Inheritance** | `CombatShip` & `TransportShip` extend `SpaceVessel`. `Destroyer` & `CargoFreighter` further specialize behavior. |
| **Polymorphism** | `virtual`/`override` methods for `GetStatus()` and `ExecuteMission()`. Runtime dispatch via `List<SpaceVessel>`. |
| **Encapsulation** | Private backing fields, validated properties (`Fuel`), and protected constructors control state mutation. |
| **Sealed Classes** | `Destroyer` and `CargoFreighter` are marked `sealed` to prevent unintended inheritance. |
| **Indexers** | `CargoFreighter` implements a custom indexer `this[int index]` for cargo log management. |
| **Resource Management** | Finalizer (`~SpaceVessel`) demonstrates object lifecycle tracking (noted for educational purposes). |

---

## 📁 Project Structure
```
OOPLab1/
├── SpaceFlot/
│   ├── Core Models/
│   │   ├── SpaceVessel.cs          # Abstract base class
│   │   ├── CombatShip.cs           # Combat vessel base
│   │   ├── TransportShip.cs        # Transport vessel base
│   │   ├── Destroyer.cs            # Sealed combat specialization
│   │   └── CargoFreighter.cs       # Sealed transport specialization + indexer
│   ├── UI Components/
│   │   ├── Form1.cs                # Main application window & fleet logic
│   │   ├── CombatInputControl.cs   # Input panel for combat ships
│   │   └── TransportInputControl.cs# Input panel for transport ships
│   └── Program.cs                  # Application entry point
├── .gitignore
└── .aiignore
```

---

## 🚀 Getting Started

### Prerequisites
- **.NET SDK 6.0+** (Windows Desktop Runtime)
- **IDE**: Visual Studio 2022 (recommended) or VS Code with C# Dev Kit

### Build & Run
```bash
# Clone the repository
git clone <repository-url>
cd OOPLab1

# Restore dependencies & build
dotnet restore
dotnet build

# Run the application
dotnet run --project SpaceFlot/SpaceFlot.csproj
```
*Alternatively, open `SpaceFlot.sln` in Visual Studio and press `F5`.*

---

## 🖥️ Usage Guide
1. **Select Vessel Type**: Use the dropdown menu to choose between `Combat` or `Transport`.
2. **Configure Parameters**: Fill in the model name and specialized attributes (Fire Power or Capacity).
3. **Add to Fleet**: Click `Add Ship` to instantiate and register the vessel.
4. **Execute Mission**: Select a ship from the list and click `Execute Mission` to trigger polymorphic behavior and update fuel/status.
5. **Quick Add**: Use the shortcut buttons to instantly add default `Destroyer` or `CargoFreighter` instances.

---

## 📝 Technical Notes & Recommendations
- **Localization**: UI strings and exception messages are currently in Russian. Consider extracting to `.resx` resource files for multi-language support.
- **Finalizer Usage**: `~SpaceVessel()` is included for demonstration. In production C#, finalizers should only be used for unmanaged resource cleanup. Prefer `IDisposable` if needed.
- **UI/Logic Coupling**: `Form1.cs` directly instantiates concrete types. Future iterations could benefit from a Factory pattern or dependency injection to improve testability.
- **State Management**: `UpdateUI()` rebuilds the list on every change. For larger fleets, consider `INotifyPropertyChanged` or data binding.

---

## 📄 License
This project is intended for educational and laboratory purposes. See repository root for licensing details.