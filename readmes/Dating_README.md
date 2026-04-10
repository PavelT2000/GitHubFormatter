# Dating

A lightweight, Telegram-authenticated dating profile manager built with **FastAPI**, **SQLite**, and **JWT**. Designed as a functional MVP, it demonstrates secure passwordless authentication, stateless session management, and server-side rendered routing.

---

## 📋 Overview

This application replaces traditional email/password flows with Telegram's official Login Widget. Upon successful cryptographic verification, the backend issues a time-bound JWT, enabling secure access to profile routes. The architecture prioritizes simplicity, async readiness, and clear separation of concerns.

---

## ✨ Features

- 🔐 **Telegram Authentication**: HMAC-SHA256 payload verification using your bot token.
- 🎫 **JWT Session Management**: Stateless tokens with 1-hour expiration and `Bearer` header validation.
- 👤 **User Registration & Routing**: Automatic SQLite upsert on first login, with profile page redirection.
- 🗄️ **SQLite Persistence**: File-based storage with Pydantic-backed data validation.
- 🌐 **FastAPI + Jinja2**: High-performance async backend with server-side HTML rendering.
- 📖 **Auto-Generated Docs**: Interactive Swagger UI (`/docs`) and ReDoc (`/redoc`) endpoints.

---

## 🛠️ Tech Stack

| Layer | Technologies |
|-------|--------------|
| **Backend** | Python 3.10+, FastAPI, Uvicorn, Pydantic, PyJWT, `python-dotenv` |
| **Database** | SQLite3 (`sqlite3` stdlib) |
| **Frontend** | HTML5, CSS3, Vanilla JS, Jinja2 Templating |
| **Auth** | Telegram Login Widget, JWT (HS256) |

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.10 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Domain configured for the Telegram Login Widget (must match deployment URL)

### 2. Installation
```bash
# Clone & navigate
git clone https://github.com/your-username/dating.git
cd dating

# Create & activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic PyJWT python-dotenv jinja2
```

### 3. Configuration
Create a `.env` file in the project root:
```env
BOT_TOKEN=your_telegram_bot_token_here
JWT_SECRET=your_strong_random_secret_key
JWT_ALGORITHM=HS256
```
> 🔒 **Security Note**: Never commit `.env` to version control. Add it to `.gitignore`.

### 4. Run the Server
```bash
python main.py
```
The application starts at `http://127.0.0.1:80`.  
⚠️ *Note: Binding to port `80` requires `sudo`/Administrator privileges on most OS. For local development, change `port=80` to `port=8000` in `main.py`.*

---

## 🔐 Authentication Flow

1. **Frontend**: User clicks the Telegram Login Widget → Widget POSTs user payload to `/telegram-callback`.
2. **Verification**: Backend strips the `hash`, sorts parameters, and computes HMAC-SHA256 using `BOT_TOKEN`.
3. **Token Issuance**: If valid, the backend checks/creates the user in SQLite and returns a JWT.
4. **Session**: Frontend stores the token in `localStorage` and attaches it as `Authorization: Bearer <token>` for protected routes.

---

## 📡 API Reference

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET`  | `/` | Renders the login page | ❌ |
| `POST` | `/telegram-callback` | Verifies Telegram payload & issues JWT | ❌ |
| `GET`  | `/profile` | Renders the user profile page | ✅ (`Bearer <token>`) |
| `PUT`  | `/profile` | *(Placeholder in `app.py`)* Updates profile data | ✅ |

> 📘 Interactive documentation: `http://127.0.0.1/docs` (Swagger) | `http://127.0.0.1/redoc`

---

## 📁 Project Structure

```
dating/
├── main.py              # Primary FastAPI app, auth logic, routing & server entry
├── app.py               # Standalone prototype module (dummy profile endpoints)
├── database.py          # SQLite connection, table creation & user CRUD
├── models.py            # Pydantic validation schemas
├── .env                 # Environment variables (gitignored)
├── database.db          # Auto-generated SQLite file
├── .aiignore            # AI context exclusion rules
└── README.md            # Project documentation
```

---

## ⚠️ Technical Notes & Production Readiness

This codebase is a **functional MVP**. The following items should be addressed before production deployment:

| Area | Current State | Recommended Action |
|------|---------------|-------------------|
| **Database ID Generation** | Uses a hardcoded `_id = 1` counter | Switch to `ID INTEGER PRIMARY KEY AUTOINCREMENT` or pass `NULL` |
| **SQL Injection Risk** | Uses f-strings in `database.py` | Use parameterized queries: `cursor.execute("SELECT 1 FROM users WHERE telegramID=?", (id,))` |
| **Profile Endpoint** | `app.py` runs a separate FastAPI instance | Merge `/profile` PUT logic into `main.py` and wire it to JWT auth |
| **Jinja2 Context** | `profile.html` route omits `request` object | Pass `{"request": request}` to `TemplateResponse` |
| **Port Binding** | Defaults to port `80` | Use `8000` for dev; reverse proxy (Nginx/Caddy) for prod |
| **Security** | No rate limiting, CORS, or input sanitization | Add `slowapi`, strict CORS, and `bleach`/`html.escape` for user inputs |
| **Migrations** | Manual schema creation | Integrate `Alembic` for version-controlled DB migrations |

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for details.