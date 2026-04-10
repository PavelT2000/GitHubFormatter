# 🌐 webApp

A full-stack Telegram Mini App & Web Platform built with **FastAPI** and **React 19**. Features secure Telegram authentication, JWT-protected APIs, profile matching/swipe mechanics, photo management, and an integrated Telegram bot.

---

## 📖 Overview
`webApp` is a modern dating/social discovery platform designed to run seamlessly as a Telegram Mini App (TMA) and a standalone web SPA. The backend handles authentication via Telegram's `initData`, manages relational data with SQLAlchemy, and serves the compiled React frontend in production. The frontend leverages React Router, Material UI, and the official Telegram Web Apps SDK for a native-like mobile experience.

---

## ✨ Features
- 🔐 **Telegram Mini App Authentication**: Secure login via `initData` validation & JWT issuance
- 🃏 **Profile Discovery**: Swipe-style `Ankete` system with skip/like logic
- 💬 **Likes & Mutual Matching**: Track sent/received likes, handle mutual matches
- 🖼️ **Media Management**: Photo uploads, gallery preview, and main photo selection
- 🔍 **Advanced Filtering**: Age range, city, gender, and like-status filters
- 🤖 **Telegram Bot Integration**: Background bot process for notifications & admin tasks
- 🗄️ **Database Migrations**: Alembic-powered schema versioning with cascade deletes
- 📱 **Responsive SPA**: Vite + React 19 with CSS Modules & Material UI components

---

## 🛠 Tech Stack

| Layer        | Technologies                                                                 |
|--------------|------------------------------------------------------------------------------|
| **Backend**  | Python 3.11+, FastAPI, SQLAlchemy, Alembic, Uvicorn, PyJWT, aiogram, Telethon |
| **Frontend** | React 19, Vite, React Router DOM, Material UI, CSS Modules, `@twa-dev/sdk`   |
| **Database** | SQLite (dev) / PostgreSQL/MySQL (prod-ready via SQLAlchemy)                  |
| **Tooling**  | ESLint, Babel, npm, Git, Cloudflare Tunnel (dev proxy)                       |

---

## 📁 Project Structure
```
webApp/
├── backend/                 # FastAPI application
│   ├── App/
│   │   ├── API/             # Route handlers (user, ankete)
│   │   ├── DB/              # SQLAlchemy models & session config
│   │   └── Other/           # Auth, bot, business logic, security
│   ├── main.py              # App entry, static serving, startup hooks
│   └── requirements.txt
├── frontend/                # React SPA
│   ├── src/
│   │   ├── components/      # UI modules (Ankets, Profile, Likes, etc.)
│   │   ├── auth/            # TMA auth utilities
│   │   └── App.jsx          # Router & layout
│   ├── package.json
│   └── vite.config.js
├── alembic/                 # Database migration scripts
├── images/                  # User-uploaded media (auto-created)
└── .env                     # Environment variables (not tracked)
```

---

## 🚀 Getting Started

### Prerequisites
- Python `3.11+`
- Node.js `18+` & `npm`/`pnpm`
- Git
- Telegram Bot Token & Web App URL

### Installation
```bash
# 1. Clone the repository
git clone <repository-url>
cd webApp

# 2. Setup Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Setup Frontend
cd ../frontend
npm install
```

### Environment Configuration
Create a `.env` file in the `backend/` directory:
```env
DATABASE_URL=sqlite:///./app.db
JWT_SECRET_KEY=your-super-secret-jwt-key
BOT_TOKEN=your-telegram-bot-token
TELEGRAM_BOT_USERNAME=your_bot_username
ALLOWED_ORIGINS=http://localhost:5937,https://your-domain.com
```

### Running the Application

#### 🔧 Development Mode
```bash
# Terminal 1: Start Backend (FastAPI)
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Start Frontend (Vite)
cd frontend
npm run dev
```
> 💡 The Vite dev server runs on `http://localhost:5937`. Use the Cloudflare tunnel URL in `vite.config.js` for Telegram Mini App testing.

#### 📦 Production Build
```bash
# 1. Build Frontend
cd frontend
npm run build

# 2. Start Backend (serves static SPA)
cd ../backend
uvicorn main:app --host 0.0.0.0 --port 80
```

---

## 🔌 API Reference

| Method | Endpoint        | Description                          | Auth Required |
|--------|-----------------|--------------------------------------|---------------|
| `GET`  | `/authorize`    | Validates TMA `initData`, returns JWT | ❌            |
| `GET`  | `/get-ankete`   | Fetches next profile for discovery   | ✅ JWT        |
| `POST` | `/like`         | Sends a like + optional message      | ✅ JWT        |
| `POST` | `/skip`         | Skips current profile                | ✅ JWT        |
| `GET`  | `/get-likes`    | Retrieves received likes             | ✅ JWT        |
| `POST` | `/get-like`     | Fetches specific like details        | ✅ JWT        |
| `POST` | `/like-like`    | Handles mutual match logic           | ✅ JWT        |

> 🔑 **Authentication Header**: `Authorization: tma <telegram_init_data_string>`

---

## 🗄 Database & Migrations

The project uses **Alembic** for schema versioning. Models include `User`, `Photo`, `Like`, `View`, and `Ban` with proper cascade relationships.

```bash
# Apply pending migrations
alembic upgrade head

# Generate new migration after model changes
alembic revision --autogenerate -m "describe changes"
```

> ⚠️ Ensure `DATABASE_URL` in `.env` matches your target database before running migrations.

---

## 🌍 Deployment Notes
- The backend is configured to serve the compiled React SPA (`frontend/dist/`) in production.
- Uploaded images are stored in `./images/` and served via `/images/*`.
- For production, replace SQLite with PostgreSQL/MySQL and set `JWT_SECRET_KEY` to a cryptographically secure string.
- Use a reverse proxy (Nginx/Caddy) or Cloudflare Tunnel for HTTPS & domain routing.
- The Telegram bot runs as a daemon thread on startup (`threading.Thread(target=run_bot, daemon=True)`).

---

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure all migrations are tested and frontend builds pass before submitting.

---

## 📄 License
This project is proprietary. All rights reserved. Unauthorized distribution or modification is prohibited.

---

*Built with ❤️ using FastAPI, React, and Telegram Mini Apps.*