# .NET Learning & Project Repository

A structured, hands-on repository documenting a progressive learning journey through **C# fundamentals**, **Object-Oriented Programming**, and **ASP.NET Core Web API development**. This project contains daily exercises, console applications, and a production-ready Task Management API featuring JWT authentication, Entity Framework Core, and Swagger documentation.

---

## 🛠 Tech Stack
| Category | Technologies |
|----------|--------------|
| **Language** | C# 12 / .NET 8 |
| **Web Framework** | ASP.NET Core Web API |
| **Data Access** | Entity Framework Core 8 + SQLite |
| **Authentication** | JWT (JSON Web Tokens) |
| **API Documentation** | Swagger / OpenAPI |
| **Tooling** | .NET CLI, EF Core Migrations, Visual Studio / VS Code |

---

## 📁 Project Structure
The repository is organized by learning phases and project types. Below is a breakdown of the directory hierarchy:

```
├── First_week/                 # Console exercises covering C# basics
│   ├── Projects/               # Consolidated Week 1 console apps
│   └── README.md               # Week 1 syllabus & exercise links
├── Second_week/                # ASP.NET Core & Web API projects
│   ├── MyFirstApi/             # Initial API exploration
│   ├── TaskManager/            # MVC + EF Core prototype
│   ├── TaskManagerV2.0/        # Final API project (JWT, EF Core, Swagger)
│   └── README.md               # Week 2 syllabus & API roadmap
├── Projects/                   # Archived/backup copy of Week 1 console apps
├── 1Task/ ... 7Task/           # Standalone algorithmic exercises
├── Burley/, CorrectDays/       # Additional practice projects
├── TODOLIst/                   # Console-based task manager (Week 1 capstone)
├── ProgTask/                   # C++ exercise (non-.NET reference)
├── Trash/                      # Deprecated/experimental code snippets
├── .gitignore, .gitattributes  # Version control configurations
├── aicontext.txt               # AI/context prompt reference
└── README.md                   # This file
```

> 💡 **Note:** `First_week/Projects/` and `Projects/` contain identical console applications. The former is actively referenced in the Week 1 syllabus, while the latter serves as a historical backup.

---

## 📅 Learning Roadmap

### 📘 Week 1: C# Fundamentals
| Day | Focus Area | Key Concepts | Deliverables |
|-----|------------|--------------|--------------|
| 1 | Syntax & Control Flow | Data types, `Nullable`, branching, loops | `IsOdd`, `ThreeDividingNumbers`, `Calculator` |
| 2 | Methods & Collections | Method overloading, `ref`/`out`, arrays, `List<T>` | `MasSum`, `MaxValue`, `PasswordGenerator` |
| 3 | OOP Principles | Classes, objects, inheritance, polymorphism | `PersonSays`, `Books` |
| 4 | Encapsulation & I/O | Access modifiers, file reading/writing | `UserData`, `TODOList` |
| 5 | Exception Handling | `try/catch/finally`, custom exceptions | `ZeroDividingCheck`, `TextFileReader` |
| 6 | Asynchronous Programming | `async`/`await`, `Task`, UI responsiveness | `Loading` |
| 7 | Capstone | Integration of Week 1 concepts | `TODOList` (Console) |

### 📗 Week 2: ASP.NET Core & Web APIs
| Day | Focus Area | Key Concepts | Deliverables |
|-----|------------|--------------|--------------|
| 1 | ASP.NET Core Intro | Middleware pipeline, `Program.cs`, DI container | `MyFirstApi` |
| 2 | Routing & Controllers | Attribute routing, HTTP verbs, query/body params | `TaskManager` (MVC) |
| 3 | EF Core & Migrations | `DbContext`, code-first migrations, SQLite | Database schema setup |
| 4 | Validation & Errors | Data annotations, HTTP status codes, error responses | Model validation layer |
| 5 | JWT Authentication | Token generation, claims, `[Authorize]` | Secure endpoints |
| 6 | API Refinement | DTOs, separation of concerns, Swagger | `TaskManagerV2.0` |
| 7 | Capstone | Full-stack API with auth & CRUD | `TaskManagerV2.0` |

---

## 🚀 Getting Started

### Prerequisites
- [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
- IDE: Visual Studio 2022, VS Code, or JetBrains Rider
- (Optional) SQLite CLI or DB Browser for SQLite

### Running Console Applications
Navigate to any console project folder and execute:
```bash
cd First_week/Projects/Calculator
dotnet run
```

### Running the TaskManager API (`TaskManagerV2.0`)
1. Navigate to the project directory:
   ```bash
   cd Second_week/TaskManagerV2.0
   ```
2. Restore dependencies:
   ```bash
   dotnet restore
   ```
3. Apply database migrations:
   ```bash
   dotnet ef database update
   ```
4. Start the API:
   ```bash
   dotnet run
   ```
5. Open Swagger UI in your browser:
   ```
   https://localhost:<PORT>/swagger
   ```

---

## 🔌 API Documentation (`TaskManagerV2.0`)

### 🔐 Authentication
All endpoints under `/api/tasks` require a valid JWT Bearer token.
```http
Authorization: Bearer <your_jwt_token>
```

### 📡 Endpoints
| Method | Route | Description | Auth |
|--------|-------|-------------|------|
| `GET` | `/api/tasks/user` | Retrieves all tasks for the authenticated user | ✅ Required |
| `POST` | `/api/tasks/add` | Creates a new task (accepts `MyTaskDTO`) | ✅ Required |
| `DELETE` | `/api/tasks/delete/{id}` | Deletes a task by ID (owner validation) | ✅ Required |

### 📦 Data Models
**`MyTask` (Entity)**
```csharp
public class MyTask
{
    public int Id { get; set; }
    [Required, StringLength(100)] public string Title { get; set; }
    [StringLength(500)] public string Description { get; set; }
    public bool IsCompleted { get; set; } = false;
    public int UserId { get; set; }
    public User User { get; set; } // Navigation property
}
```

**`MyTaskDTO` (Request Payload)**
```json
{
  "name": "string",
  "description": "string"
}
```

### 🗄 Database Configuration
- **Provider:** SQLite
- **Connection String:** Defined in `appsettings.json` (`DefaultConnection`)
- **Relationships:** One-to-Many (`User` → `Tasks`) with `Cascade` delete behavior

---

## 📝 Technical Notes & Best Practices
1. **JWT Configuration:** `Program.cs` currently sets `DefaultAuthenticateScheme` twice. For production, consider consolidating to a single assignment or using `options.DefaultScheme`.
2. **EF Core Navigation Properties:** `MyTask.User` is declared as a field (`public User User;`). EF Core recommends using properties (`public User User { get; set; }`) for reliable lazy/eager loading.
3. **DTO Pattern:** The API correctly separates domain entities from request payloads using `MyTaskDTO`, improving security and versioning flexibility.
4. **Error Handling:** Controller methods return appropriate HTTP status codes (`401`, `404`, `200`). Consider implementing a global exception middleware for consistent error formatting.

---

## 📄 License
This repository is intended for educational and portfolio purposes. Code is provided as-is for learning reference.

---
*Generated for technical documentation purposes. Structure and code align with the provided repository hierarchy and source files.*