# saves

A lightweight, Windows-based utility for managing, backing up, and synchronizing save files using Git. This project provides automated batch scripts to streamline version control workflows for save data.

## 📁 Directory Structure
```text
├── .aiignore
├── AutoGit.bat
├── GitFetch.bat
├── Save1.zip
├── Save1Solo.zip
├── Save2.zip
├── Save2Solo.zip
├── Save3.zip
├── Save3NotSolo.zip
├── Save4NotSolo.zip
├── Save5NotSolo.zip
├── Save6NotSolo.zip
├── Save7NotSolo.zip
├── _autosave1.zip
├── _autosave2.zip
└── _autosave3.zip
```

## 📋 Overview
The `saves` project provides a minimal automation layer for Git-based save file management. It includes two Windows batch scripts that handle repository synchronization, alongside a structured naming convention for manual and automated backups.

## ⚙️ Prerequisites
- **Operating System:** Windows 10 or later
- **Git:** Installed and accessible via system `PATH`
- **Repository Configuration:** 
  - Initialized local repository (`git init`)
  - Remote origin configured (`git remote add origin <repository-url>`)
  - Git credentials cached or configured to prevent interactive authentication prompts

## 🚀 Usage

### Push Changes (`AutoGit.bat`)
Executes a complete staging, commit, and push cycle:
1. Stages all tracked and untracked files (`git add .`)
2. Commits changes with a static message (`git commit -m "edit"`)
3. Pushes commits to the remote repository (`git push`)
4. Pauses execution for 5 seconds to display console output

**Execution:**
```cmd
AutoGit.bat
```

### Pull Updates (`GitFetch.bat`)
Fetches and merges the latest changes from the remote repository:
1. Pulls updates (`git pull`)
2. Pauses execution for 5 seconds to display console output

**Execution:**
```cmd
GitFetch.bat
```

## 🔧 Configuration & Notes

| File/Component | Purpose |
|----------------|---------|
| `.aiignore` | Excludes `*.zip` and `*.bat` files from AI context windows. **Note:** This does not affect Git tracking. Use `.gitignore` if you need to exclude files from version control. |
| `AutoGit.bat` | Uses a static commit message (`edit`). Modify the script to implement dynamic timestamps or descriptive messages if required. |
| `timeout 5` | Both scripts include a 5-second console pause for output visibility. Adjust or remove this value based on workflow preferences. |
| Save Naming Convention | `SaveX.zip` / `SaveXSolo.zip` / `SaveXNotSolo.zip` indicate manual backups. `_autosaveX.zip` indicates automated or system-generated backups. |

## ⚠️ Important Considerations
- **Binary Tracking:** `.zip` files are binary assets. Git is not optimized for large binary versioning. Consider using Git LFS if repository size becomes a concern.
- **Authentication:** Ensure Git credential helpers are configured (`git config --global credential.helper manager-core` or similar) to avoid interactive prompts during automated execution.
- **Conflict Resolution:** `GitFetch.bat` performs a standard `git pull`. If local and remote histories diverge, manual conflict resolution may be required before subsequent pushes.

## 📄 License
[Specify License, e.g., MIT, Apache 2.0, or Proprietary]

---
*Documentation generated for technical reference. Verify all Git operations against your organization's data retention and backup policies.*