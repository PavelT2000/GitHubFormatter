# C- Repository

> A comprehensive C#/.NET learning and experimentation workspace featuring web applications, desktop GUIs, custom graphics engines, object-oriented design patterns, and database integration.

## 📁 Project Structure

| Directory | Description |
|-----------|-------------|
| `ASP.net/` | Blazor Server web applications (`blazortest`, `MyFirstApp`) with interactive server-side rendering |
| `C#Tests/` | Test environment for Blazor components, routing, and layout validation |
| `GraphicsTest/` | WinForms-based 3D rendering engine with custom math, camera controls, and polygon projection |
| `MyAppWithOpenTK/` | OpenTK-powered 2D/3D graphics application with file-based polygon parsing |
| `OOP/` | Console application demonstrating OOP principles (inheritance, encapsulation, transaction management) |
| `GravityCheck/` | WinForms physics/gravity simulation prototype |
| `WindowsTry/` | Basic Windows Forms application template |
| `sqlLerning/` | Console-based SQL integration and database learning module |

## 🛠️ Technologies & Frameworks

- **Language:** C# 10+
- **Runtime:** .NET 8 / .NET 9 (verify via `.csproj` files)
- **Web:** ASP.NET Core, Blazor Server, Razor Components
- **Desktop:** Windows Forms (WinForms)
- **Graphics:** OpenTK, Custom 3D Math (`Vector3`, `Mat`, `Camera`), Immediate Mode Rendering
- **Database:** ADO.NET / SQL Client (depending on `sqlLerning` implementation)
- **Tooling:** Visual Studio 2022, JetBrains Rider, or VS Code with C# Dev Kit

## 🚀 Getting Started

### Prerequisites
- [.NET SDK 8.0+](https://dotnet.microsoft.com/download)
- An IDE: Visual Studio 2022, JetBrains Rider, or VS Code
- (Optional) SQL Server or SQLite for `sqlLerning`

### Installation & Setup
```bash
# Clone the repository
git clone <repository-url>
cd C-

# Restore dependencies across all projects
dotnet restore
```

### Running Individual Modules
Each module is a standalone project. Execute them using:
```bash
# Blazor Web App
dotnet run --project ASP.net/blazortest

# WinForms 3D Graphics Engine
dotnet run --project GraphicsTest/GraphicsTest

# OpenTK Graphics App
dotnet run --project MyAppWithOpenTK/MyAppWithOpenTK

# OOP Banking Console App
dotnet run --project OOP/classes

# SQL Learning Module
dotnet run --project sqlLerning
```

## 📦 Module Highlights

### 🌐 ASP.NET Blazor Server (`ASP.net/`)
- Interactive server-side rendering with Razor Components
- Standard layout, routing (`Routes.razor`), and error handling setup
- Configured for HTTPS redirection, static files, and antiforgery protection
- Follows modern minimal hosting patterns (`WebApplication.CreateBuilder`)

### 🎨 Custom 3D Graphics Engine (`GraphicsTest/`)
- **Math Library:** `Vector3` class with operator overloads (`+`, `-`, `*`), normalization, dot/cross products, and axis-aligned rotation matrices
- **Camera System:** Position, direction, up/right vectors, and keyboard-controlled movement (`WASD`, `Space`, `C`)
- **Rendering Pipeline:** WinForms `Paint` event-driven rendering with double buffering and aspect ratio calculation
- **Polygon Management:** 3D polygon storage, color assignment, and projection via `Drawer` class

### 🖼️ OpenTK Integration (`MyAppWithOpenTK/`)
- Game loop architecture using `GameWindow` with fixed timestep (`60.0` FPS)
- File-based 2D polygon parsing (`_2DParser`, `_2DPolygon`, `Vertex2D`)
- Immediate mode OpenGL rendering (`GL.Begin`/`GL.End`)
- Vertex iteration with console debugging output

### 🏦 Object-Oriented Design (`OOP/`)
- `BankAccount` base class with transaction history, computed balance, and minimum balance enforcement
- `Transaction` immutable data model
- Inheritance-ready architecture (`GiftCardAccount`, `InterestEarningAccount`, `LineOfCreditAccount`)
- Extensible month-end processing hook (`virtual PerformMonthEndTransactions()`)

## ⚙️ Architecture Notes
- **Graphics Pipeline:** The `GraphicsTest` module implements a foundational software-style 3D pipeline on WinForms GDI+. It demonstrates core concepts like vector algebra, camera transforms, and polygon rasterization without hardware acceleration.
- **OpenTK Legacy Patterns:** `MyAppWithOpenTK` utilizes immediate mode rendering. This is pedagogically valuable but should be migrated to VBOs/VAOs and shader programs for production-grade performance.
- **Blazor Configuration:** ASP.NET projects follow .NET 8+ conventions with component-based routing, interactive server render mode, and environment-aware exception handling.

## 📝 Future Improvements
- [ ] Migrate OpenTK rendering to modern OpenGL core profile (VAOs, VBOs, GLSL shaders)
- [ ] Implement hardware-accelerated 3D rendering in `GraphicsTest` using DirectX, Vulkan, or Silk.NET
- [ ] Add unit tests for `Vector3` math operations and `BankAccount` transaction logic
- [ ] Standardize target framework across all modules to a single .NET LTS version
- [ ] Implement dependency injection and configuration management in desktop applications

## 📄 License
This repository is intended for educational and experimental purposes. See the `LICENSE` file for details.

## 🤝 Contributing
Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request following standard Git workflows. Ensure all code adheres to C# coding conventions and includes appropriate XML documentation for public APIs.