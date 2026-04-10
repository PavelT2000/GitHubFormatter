```markdown
# HelloWorld

A minimal, production-ready C# console application targeting **.NET Framework 4.7.2**. Designed as a foundational template for developers working with traditional .NET workflows, this project demonstrates standard Visual Studio solution architecture, MSBuild configuration, assembly metadata management, and basic console I/O.

## 📖 Overview

When executed, the application initializes the .NET Framework runtime, invokes the `Main` entry point, and outputs a standard `"Hello, World!"` message to the console. It serves as a reference implementation for legacy .NET Framework projects, showcasing proper project file structure, configuration management, and build pipeline compatibility.

## 🛠️ Prerequisites

- **Operating System:** Windows 10/11 or Windows Server (required for .NET Framework 4.7.2)
- **IDE:** Visual Studio 2019 or 2022 with the `.NET desktop development` workload
- **Framework:** .NET Framework 4.7.2 Developer Pack (included with modern Visual Studio installations)
- **Build Tool:** MSBuild 15.0+ (bundled with Visual Studio)

> **Note:** .NET Framework is Windows-exclusive. For cross-platform development, consider migrating to .NET 6+ or .NET 8+.

## 📦 Setup & Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-root>/Day1/HelloWorld
```

### 2. Open in Visual Studio
```bash
start HelloWorld.sln
```
Visual Studio will automatically resolve the target framework, configure build paths, and load the project. No package restoration is required, as this project contains no external NuGet dependencies.

### 3. Command-Line Build (Alternative)
If you prefer a headless workflow, use the **Developer Command Prompt for Visual Studio**:
```bash
# Build the project (Debug configuration)
msbuild HelloWorld.sln /p:Configuration=Debug /t:Build

# Build for Release
msbuild HelloWorld.sln /p:Configuration=Release /t:Build
```

## 🚀 Usage

### ▶️ Via Visual Studio
1. Open `HelloWorld.sln`
2. Press `F5` to run with debugging, or `Ctrl + F5` to run without debugging.
3. The console window will display:
   ```
   Hello, World!
   ```

### 💻 Via Command Line
Execute the compiled binary directly:
```bash
# Debug build
.\HelloWorld\bin\Debug\HelloWorld.exe

# Release build
.\HelloWorld\bin\Release\HelloWorld.exe
```

### 📝 Expected Behavior
- The .NET Framework runtime initializes and loads the assembly.
- `Program.Main()` executes `Console.WriteLine("Hello, World!");`.
- The process terminates gracefully with exit code `0`.

## 📁 Project Structure
```
Day1/HelloWorld/
├── HelloWorld.sln                 # Visual Studio solution file
├── HelloWorld/
│   ├── HelloWorld.csproj          # MSBuild project configuration (.NET Framework 4.7.2)
│   ├── App.config                 # Application runtime configuration
│   ├── Program.cs                 # Application entry point
│   └── Properties/
│       └── AssemblyInfo.cs        # Assembly metadata, versioning & COM settings
├── .gitattributes                 # Line-ending normalization rules
└── .gitignore                     # Standard Visual Studio & .NET ignore patterns
```

## ⚙️ Configuration & Architecture Notes

- **`HelloWorld.csproj`**: Uses the legacy MSBuild project format (`ToolsVersion="15.0"`). Explicitly references core .NET Framework assemblies and defines `Debug`/`Release` build configurations.
- **`App.config`**: Provides runtime configuration hooks (e.g., binding redirects, CLR settings). Currently uses framework defaults.
- **`AssemblyInfo.cs`**: Manages assembly-level metadata (version, copyright, GUID, COM visibility) separate from source code, following traditional .NET Framework conventions.
- **Deterministic Builds**: Enabled via `<Deterministic>true</Deterministic>` to ensure reproducible compilation outputs across environments.

## 🔍 Troubleshooting

| Issue | Resolution |
|-------|------------|
| `MSB4019: The imported project was not found` | Ensure you are using the **Developer Command Prompt for VS** or have MSBuild in your system `PATH`. |
| Missing `.sln` file | Generate one via Visual Studio (`File > New > Project from Existing Code`) or run `devenv /upgrade` on the `.csproj`. |
| `TargetFrameworkVersion` mismatch | Verify .NET Framework 4.7.2 Developer Pack is installed via the Visual Studio Installer. |
| Build fails with `CSC` errors | Confirm `Program.cs` and `AssemblyInfo.cs` are correctly referenced in the `.csproj` `<Compile>` items. |

## 📄 License

This project is provided as-is for educational, reference, and internal development purposes. Modify, distribute, and integrate according to your organization's standards and compliance requirements.
```