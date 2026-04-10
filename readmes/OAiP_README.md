# OAiP — Fundamentals of Algorithms and Programming

## 📖 Overview
This repository serves as the central archive for the **Fundamentals of Algorithms and Programming (OAiP)** academic course. It contains Delphi (Object Pascal) source code, project configurations, technical reports, and architectural diagrams corresponding to laboratory assignments and control works.

All applications are developed using the **VCL (Visual Component Library)** framework and are structured to demonstrate core programming concepts, including algorithmic design, recursion, sorting, string manipulation, and data structure implementation.

## 🛠 Prerequisites
- **IDE:** Embarcadero RAD Studio / Delphi (10.2 Tokyo or newer recommended for `.dproj` compatibility)
- **OS:** Microsoft Windows (required for VCL compilation and execution)
- **Documentation Viewers:** Microsoft Word, Visio, or Draw.io (for `.doc`/`.docx`, `.vsd`/`.vsdx`, and `.drawio` assets)
- **Version Control:** Git (with automatic line-ending normalization)

## 📁 Project Structure
The repository is organized by assignment type and academic sequence:

| Directory | Description |
|-----------|-------------|
| `ЛаборатонаяРабота№1` – `Лабораторная№7` | Core laboratory assignments covering foundational algorithms, recursion, sorting, arrays, and string processing. |
| `КР1задание` – `КР3задание` | Control work (midterm/final assessment) implementations, project groups, and supporting diagrams. |
| `2ая кр` / `DelphiTest` | Supplementary test projects and secondary control work iterations. |
| `__history` / `__recovery` | Delphi IDE auto-backup and crash-recovery artifacts (excluded from version control). |

> **Note:** Directory and file names preserve the original Russian academic naming convention for traceability.

## 🚀 Getting Started
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd OAiP
   ```
2. **Open in Delphi:**
   - Launch RAD Studio / Delphi.
   - Navigate to the desired assignment folder and open the corresponding `.dproj` (single project) or `.groupproj` (multi-project) file.
3. **Build & Run:**
   - Press `F9` or select **Run > Run** to compile and execute.
   - Verify the target platform (`Win32`/`Win64`) matches your system architecture in the Project Manager.

## 📦 Repository Management
This repository includes configuration files to maintain version control hygiene and optimize context processing:

- **`.aiignore`**: Custom exclusion rules that filter out Delphi build artifacts (`*.dcu`, `*.exe`, `*.dproj.local`), IDE history/recovery directories, binary documentation, and temporary files. Intended for AI-assisted development workflows and repository cleanliness.
- **`.gitattributes`**: Enforces `text=auto` LF normalization across all tracked text files to prevent cross-platform line-ending conflicts.

> 💡 **Tip:** If using standard Git workflows, rename `.aiignore` to `.gitignore` or configure your Git client to respect custom ignore paths.

## 📄 Documentation & Diagrams
Each assignment directory typically contains:
- **Technical Reports:** `.doc` / `.docx` files detailing algorithm analysis, implementation methodology, test cases, and results.
- **Architecture & Flow Diagrams:** `.vsd`, `.vsdx`, and `.drawio` files illustrating program logic, control flow, and structural design.

## ⚠️ Academic Disclaimer
This repository is intended strictly for educational and reference purposes. Code and documentation reflect academic coursework and may not adhere to production-grade software engineering standards. Users are encouraged to review, adapt, and cite appropriately in accordance with their institution's academic integrity policies.

## 📜 License
**Educational Use Only.** Redistribution, commercial exploitation, or submission of this code as original work without explicit authorization is prohibited.