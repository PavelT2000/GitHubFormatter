# HtmlLearning

🎓 **Educational Sandbox for Web Development & Algorithmic Programming**

## 📖 Overview
**HtmlLearning** is a structured, hands-on repository designed to explore and practice fundamental concepts in modern web development and algorithmic programming. This project serves as a modular learning environment where each directory focuses on a specific technical objective, ranging from semantic HTML and CSS layout techniques to JavaScript DOM manipulation and C++ string-based arithmetic.

> ⚠️ **Note**: This repository is intended for educational purposes. Code snippets reflect iterative learning and may contain experimental implementations, intentional syntax variations, or incomplete features.

## 📁 Project Structure
```
HtmlLearning/
├── .aiignore
├── .gitattributes
├── README.md
├── DataBaseTest/                 # C++ algorithm & static UI mockup
├── Dynmamic website/             # Interactive JS & DOM manipulation
├── HtmlTest/                     # Basic HTML table practice
├── Работа с текстом/             # Typography & text styling
├── Работа с таблицами/           # Table structure & layout
├── Работа с ссылками/            # Internal/external linking & navigation
└── Работа с позиционированием/   # CSS positioning & layered compositions
    └── position-1/               # Nested positioning exercise
```
*(Note: Cyrillic directory names are preserved to match the original learning environment.)*

## 🛠️ Prerequisites & Setup
This project requires no external package managers or build tools. Follow these steps to run the modules locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/HtmlLearning.git
   cd HtmlLearning
   ```

2. **Environment Requirements**
   - **Web Modules**: Any modern browser (Chrome, Firefox, Edge, Safari).
   - **C++ Module**: A standard C++ compiler (`g++`, `clang++`, or MSVC).
   - **IDE (Optional)**: Visual Studio Code. The `DataBaseTest/.vscode/launch.json` is preconfigured for `lldb` debugging.

3. **Local Server (Recommended)**
   To prevent CORS restrictions and ensure proper asset loading, serve the project locally:
   ```bash
   # Python 3
   python -m http.server 8000
   # Node.js
   npx serve .
   ```

## 🚀 Usage Guide
Each module operates independently. Navigate to the target directory and open `index.html` in your browser or via the local server.

### 🌐 Web Development Modules
| Module | Focus Area | Key Features |
|--------|------------|--------------|
| `Работа с текстом/` | Typography & CSS | Custom font styling, heading hierarchy, list formatting, color/line-height control |
| `Работа с таблицами/` | Data Layout | Semantic `<table>` structure (`thead`, `tbody`, `tfoot`), column spanning, CSS styling |
| `Работа с ссылками/` | Navigation & Routing | Internal page linking, external targets (`_blank`), PDF asset embedding |
| `Работа с позиционированием/` | CSS Layout | Absolute/relative positioning, layered image composition, responsive asset placement |
| `Dynmamic website/` | JavaScript & DOM | Mouse-tracking cursor, event-driven state toggling, dynamic element generation |
| `HtmlTest/` | HTML Fundamentals | Basic markup structure, table layout practice |

### ⚙️ C++ Algorithm Module (`DataBaseTest/aboba.cpp`)
Demonstrates manual digit-by-digit multiplication using string manipulation to handle large integers.
```bash
cd DataBaseTest
g++ aboba.cpp -o aboba
./aboba
# Follow terminal prompts to input values
```

## 📝 Development Notes
- **Experimental Implementations**: Several files contain iterative code (e.g., incomplete `spawn()` function in `index.js`, minor HTML tag mismatches in table structures). These are intentional learning artifacts.
- **Debugging**: Use the provided `.vscode/launch.json` configuration to attach `lldb` for step-through debugging of the C++ module.
- **Asset Paths**: Ensure relative paths are preserved when moving files. The positioning module relies on local image assets (`*.png`, `*.jpg`).

## 🔮 Future Improvements
- [ ] Refactor JavaScript event listeners for optimal performance and memory management
- [ ] Standardize HTML syntax validation and implement semantic markup (`<main>`, `<section>`, `<nav>`)
- [ ] Add responsive breakpoints, mobile-first CSS, and WCAG accessibility attributes
- [ ] Implement robust input validation and error handling in the C++ arithmetic logic
- [ ] Migrate to a unified build system or module bundler for cross-module consistency

---
*📚 Built for learning. Contributions, feedback, and code reviews are welcome.*