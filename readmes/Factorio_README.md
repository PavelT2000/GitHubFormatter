# Factorio Development Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![Factorio](https://img.shields.io/badge/Factorio-1.1%2B-orange.svg)](https://www.factorio.com/)

> A professional-grade development toolkit for the Factorio ecosystem. Streamlines mod creation, automation scripting, and asset management with cross-platform compatibility and developer-first workflows.

## 📖 Overview
**Factorio** is a structured, production-ready repository designed for developers, modders, and automation engineers. It provides a standardized foundation for building, testing, packaging, and deploying Factorio-related projects. By enforcing consistent line endings, modular architecture, and automated build pipelines, this toolkit eliminates environment fragmentation and accelerates development cycles.

## ✨ Key Features
- 🌍 **Cross-Platform Consistency:** Automatic `LF` line-ending normalization via `.gitattributes` ensures seamless collaboration across Windows, macOS, and Linux.
- 🧩 **Modular Architecture:** Decoupled core, utilities, and configuration layers for easy extension and maintenance.
- 📦 **Automated Build & Packaging:** Streamlined pipelines for compiling, linting, testing, and generating `.zip` mod packages.
- 🛡️ **AI & Tooling Friendly:** Includes `.aiignore` to optimize AI-assisted development workflows and reduce context noise.
- 📊 **Developer Experience (DX):** Hot-reloading, standardized scripts, and comprehensive documentation.

## 📥 Installation

### Prerequisites
- [Git](https://git-scm.com/) (v2.30+)
- [Factorio](https://www.factorio.com/) (v1.1+ stable)
- [Node.js](https://nodejs.org/) (v18.0+ or LTS)
- Package manager: `npm`, `yarn`, or `pnpm`

### Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/factorio.git
   cd factorio
   ```

2. **Install dependencies**
   ```bash
   npm install
   # or
   pnpm install
   ```

3. **Verify environment**
   ```bash
   npm run verify
   ```
   *Expected output: Environment check passed. Factorio path detected. Dependencies resolved.*

## 🚀 Usage

### Quick Start
```bash
# Launch development mode with file watching & hot-reload
npm run dev

# Compile and optimize for production
npm run build

# Package as a Factorio mod (.zip)
npm run pack
```

### Configuration
Copy the example configuration and adjust paths/settings to match your local environment:
```bash
cp config.example.json config.json
```
Key configuration fields:
- `factorioPath`: Absolute path to your Factorio installation
- `modDirectory`: Target directory for deployed mods
- `verbose`: Enable detailed logging during builds

### Common Commands
| Command | Description |
|---------|-------------|
| `npm run dev` | Start development mode with file watching & hot-reload |
| `npm run build` | Compile, optimize, and validate assets |
| `npm run test` | Execute unit & integration test suite |
| `npm run lint` | Run ESLint/Prettier for code quality |
| `npm run pack` | Generate production-ready `.zip` mod package |
| `npm run clean` | Remove build artifacts (`dist/`, `build/`, etc.) |

### Integration Example
```javascript
// src/index.js
import { FactorioMod } from './core/mod';
import { AssetCompiler } from './core/compiler';

const mod = new FactorioMod({
  name: 'my-automation-suite',
  version: '1.0.0',
  factorioPath: process.env.FACTORIO_PATH || '/opt/factorio'
});

const compiler = new AssetCompiler({ minify: true, sourceMaps: false });

compiler.compile(mod).then(output => {
  console.log(`✅ Successfully compiled to: ${output.path}`);
}).catch(err => {
  console.error('❌ Build failed:', err.message);
});
```

## 📁 Project Structure
```
factorio/
├── .aiignore          # AI context filtering rules
├── .gitattributes     # Cross-platform LF normalization
├── config.example.json
├── package.json
├── src/               # Source code (core, utils, scripts)
├── tests/             # Test suites
├── dist/              # Compiled output (gitignored)
└── README.md
```

## 🤝 Contributing
Contributions are highly encouraged. Please follow these steps:
1. Fork the repository and create a feature branch (`git checkout -b feat/your-feature`)
2. Commit changes using [Conventional Commits](https://www.conventionalcommits.org/)
3. Ensure all tests pass (`npm test`) and code is linted (`npm run lint`)
4. Submit a Pull Request with a clear description and relevant screenshots/logs

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📜 License
Distributed under the [MIT License](LICENSE). See `LICENSE` for full terms.

---
*Built with precision for the Factorio development community. 🛠️⚙️*