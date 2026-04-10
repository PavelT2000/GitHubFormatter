# Lab-6-Test-Task

## 📖 Overview
**Lab-6-Test-Task** is a .NET ASP.NET Core Web API application designed to manage and query warehouse inventory data. Built following a clean, layered architecture, it exposes RESTful endpoints that retrieve specific products and warehouses based on predefined business rules. The application utilizes Entity Framework Core for data access, SQL Server for persistence, and includes Swagger/OpenAPI for interactive documentation.

## 🛠️ Tech Stack
| Category | Technology |
|----------|------------|
| **Framework** | .NET 8/9 (ASP.NET Core Web API) |
| **Language** | C# |
| **ORM** | Entity Framework Core |
| **Database** | Microsoft SQL Server |
| **API Docs** | Swagger UI + OpenAPI Generator |
| **Architecture** | Controller → Service → Repository/DbContext |

## 📁 Project Structure
```
Lab-6-Test-Task/
├── Lab6TestTask/
│   ├── Controllers/          # API endpoints (Products, Warehouses)
│   ├── Data/                 # EF Core DbContext & configuration
│   ├── Enums/                # Domain enumerations (ProductStatus)
│   ├── Migrations/           # EF Core migration artifacts
│   ├── Models/               # Domain entities (Product, Warehouse)
│   ├── Services/
│   │   ├── Interfaces/       # Service contracts
│   │   └── Implementations/  # Business logic implementations
│   ├── Program.cs            # App entry point, DI, middleware pipeline
│   └── appsettings.json      # Configuration & connection strings
├── .gitignore
└── .aiignore
```

## 🚀 Getting Started

### Prerequisites
- [.NET 8.0 SDK](https://dotnet.microsoft.com/download) or later
- Local SQL Server instance (or update the connection string in `appsettings.json`)
- IDE: Visual Studio 2022, VS Code, or JetBrains Rider

### Installation & Setup
1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Lab-6-Test-Task
   ```

2. **Restore dependencies**
   ```bash
   dotnet restore
   ```

3. **Configure Database Connection**
   Open `Lab6TestTask/appsettings.json` and verify the `DbConnection` string matches your local SQL Server instance:
   ```json
   "ConnectionStrings": {
     "DbConnection": "Data Source=.;Initial Catalog=Lab6TestTask;Integrated Security=True;..."
   }
   ```

4. **Run the Application**
   ```bash
   dotnet run
   ```
   > 💡 **Note:** The `ApplicationDbContext` constructor calls `Database.EnsureDeleted()` and `Database.EnsureCreated()` on startup. This guarantees a clean, seeded database on every run. Migrations are included for reference but are bypassed by this design.

## 🔌 API Endpoints
Once running, Swagger UI is available at: `https://localhost:<port>/swagger`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/products/selected-product` | Returns the `Reserved` product with the highest price. |
| `GET` | `/api/products/selected-products` | Returns all products received in `2025` with `Quantity > 1000`. |
| `GET` | `/api/warehouses/selected-warehouse` | Returns the warehouse with the highest total inventory value (`Quantity × Price`) among `ReadyForDistribution` products. |
| `GET` | `/api/warehouses/selected-warehouses` | Returns warehouses containing products received between `2025-04-01` and `2025-07-01`. |

## 💾 Database & Data Seeding
- **Seed Data:** The `ApplicationDbContext` automatically seeds 5 warehouses and 10 products with varying statuses, quantities, prices, and receipt dates.
- **Enum Mapping:** `ProductStatus` maps to integers (`0: ReadyForDistribution`, `1: Reserved`, `2: Shipped`, `3: InTransit`).
- **Relationships:** `Warehouse` ↔ `Product` is a one-to-many relationship configured via EF Core navigation properties.

## 📝 Notes & Constraints
- 🔒 **Immutable Files:** Several files (`Models`, `Controllers`, `Interfaces`, `Program.cs`, `appsettings.json`, `Enums`) are marked `DO NOT change anything here`. Business logic is strictly confined to the `Services/Implementations` layer.
- 🔄 **Stateless Design:** The API is stateless and relies on dependency injection for service resolution (`AddScoped`).
- 📊 **Query Optimization:** EF Core LINQ queries are translated to SQL and executed asynchronously (`ToListAsync`, `FirstOrDefaultAsync`, `MaxAsync`).
- ⚠️ **Development Behavior:** `EnsureDeleted()` + `EnsureCreated()` is used for rapid testing. For production, replace with standard EF Core migrations (`dotnet ef database update`).

## 📄 License
This project is provided for assessment and educational purposes. All rights reserved by the original author.