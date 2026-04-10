# 🏠 My Home Server App

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=for-the-badge&logo=githubactions)](https://github.com/features/actions)

A lightweight, self-hosted web application built with **FastAPI**, designed to run on an **Orange Pi Zero 3**. This project serves as a personal dashboard, documentation hub, and Linux command cheat sheet, featuring fully automated CI/CD deployment via GitHub Actions.

## ✨ Features
- 🚀 **FastAPI Backend**: High-performance, async-ready Python web framework.
- 🎨 **Jinja2 Templating**: Clean, responsive UI with server-side rendering.
- 🔄 **Automated CI/CD**: Zero-touch deployment on `push` to `main`.
- 🔒 **Secure Remote Access**: Tailscale mesh network + Cloudflare Tunnel.
- 📖 **Built-in Documentation**: Server architecture overview & Linux command cheat sheet.
- 🖥️ **Optimized for SBC**: Lightweight footprint tailored for Orange Pi Zero 3.

## 🛠️ Tech Stack
| Category       | Technology                          |
|----------------|-------------------------------------|
| **Backend**    | Python 3.x, FastAPI, Uvicorn        |
| **Frontend**   | HTML5, CSS3, Jinja2 Templates       |
| **Deployment** | GitHub Actions, SSH, systemd        |
| **Networking** | Tailscale, Cloudflare Tunnel        |
| **Hardware**   | Orange Pi Zero 3 (Ubuntu/Debian)    |

## 📂 Project Structure
```
my-home-server-app/
├── .github/workflows/deploy.yml   # CI/CD pipeline configuration
├── main.py                        # FastAPI application entry point
├── requirements.txt               # Python dependencies
├── static/                        # Static assets (images, scripts)
│   └── sync.bat                   # Windows sync utility (optional)
└── templates/                     # Jinja2 HTML templates
    ├── index.html                 # Homepage
    ├── author.html                # About the author
    ├── work.html                  # Server architecture & tech stack
    └── commands.html              # Linux/systemd command cheat sheet
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- `pip` & `venv`
- A Linux-based host (Orange Pi Zero 3 recommended)
- Tailscale & Cloudflare accounts (for remote access)
- GitHub repository with configured secrets

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/my-home-server-app.git
   cd my-home-server-app
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
5. Open `http://localhost:8000` in your browser.

## 🌐 Deployment & CI/CD

This project uses a fully automated deployment pipeline. Pushing to the `main` branch triggers the following workflow:

1. **Checkout**: Pulls the latest code.
2. **Tailscale Auth**: Establishes a secure connection to your home network.
3. **SSH Deploy**: Connects to the Orange Pi, force-syncs to `origin/main`, updates dependencies, and restarts the systemd service.

### 🔑 Required GitHub Secrets
| Secret Name          | Description                                  |
|----------------------|----------------------------------------------|
| `TAILSCALE_AUTHKEY`  | Tailscale auth key for GitHub Actions runner |
| `HOST_IP`            | Tailscale IP of your Orange Pi               |
| `HOST_USER`          | SSH username (e.g., `ubuntu` or `pi`)        |
| `SSH_PRIVATE_KEY`    | Private SSH key for passwordless login       |

### ⚙️ Systemd Service Setup
Create `/etc/systemd/system/my-website.service`:
```ini
[Unit]
Description=My Home Server App
After=network.target

[Service]
User=your_username
WorkingDirectory=/home/your_username/My/webSite
ExecStart=/home/your_username/My/webSite/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now my-website.service
```

> 💡 **Note**: Ensure your deployment user has passwordless `sudo systemctl restart my-website.service` privileges via `visudo` for seamless CI/CD execution.

## 📖 Usage
- **`/`** – Homepage & server overview
- **`/author`** – About the developer
- **`/work`** – Architecture, tech stack, and server photo
- **`/commands`** – Quick reference for `systemctl` & `journalctl` commands

## 🔒 Security & Networking
- **Tailscale**: Provides encrypted, zero-config mesh networking for secure SSH access from GitHub Actions.
- **Cloudflare Tunnel**: Exposes the local FastAPI server to the public internet without opening inbound firewall ports.
- **SSH Keys**: Passwordless authentication with restricted deployment scope.

## 📝 Notes
- The web interface is localized in **Russian**.
- The `static/sync.bat` file is a Windows utility for manual asset synchronization and is not required for core functionality.
- `requirements.txt` should contain at minimum: `fastapi`, `uvicorn`, `jinja2`.
- The CI/CD pipeline uses `git reset --hard origin/main` to ensure the server state exactly matches the repository.

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).

---
*Built with ❤️ for self-hosting enthusiasts.*