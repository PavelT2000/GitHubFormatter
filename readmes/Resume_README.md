# Resume - Personal Portfolio Website

A responsive, single-page personal resume website built with **Bootstrap 5**, designed to showcase professional background, technical skills, education, and project experience. This repository is based on the [Start Bootstrap Resume](https://startbootstrap.com/theme/resume) template, customized and extended for personal use.

## 📖 Overview
This project serves as a static, client-side portfolio site. It features a fixed sidebar navigation, smooth scroll behavior, and a clean, print-friendly layout. Content is statically embedded in `index.html` for optimal performance and zero build-step requirements, with `data/resume.txt` provided as a structured reference for future content updates or automation.

## ✨ Features
- **Responsive Layout:** Fully adaptive design using Bootstrap 5 grid and utility classes.
- **Smooth Navigation:** Fixed sidebar with Bootstrap ScrollSpy and auto-collapsing mobile menu.
- **Skill Visualization:** Icon-driven layout for programming languages, frameworks, and tools.
- **Structured Sections:** Dedicated areas for About, Experience, Education, Skills, Interests, and Awards.
- **External Integrations:** Direct, accessible links to GitHub, Telegram, Email, and LinkedIn.
- **Zero Dependencies:** No build tools or package managers required; runs natively in any modern browser.

## 🛠️ Tech Stack
| Category       | Technologies & Versions                          |
|----------------|--------------------------------------------------|
| **Markup**     | HTML5                                            |
| **Styling**    | CSS3, Bootstrap 5.2.3                            |
| **Scripting**  | Vanilla JavaScript (ES6+)                        |
| **Icons**      | Font Awesome 6.3.0, Flaticon UIcons              |
| **Typography** | Google Fonts (`Saira Extra Condensed`, `Muli`)   |
| **Assets**     | Optimized SVGs, WebP/JPG images, Favicon         |

## 📁 Project Structure
```
Resume/
├── assets/
│   └── img/          # Profile photo, tech stack SVGs, favicon
├── css/
│   └── styles.css    # Custom theme overrides & Bootstrap integration
├── data/
│   └── resume.txt    # Structured reference data for content management
├── js/
│   └── scripts.js    # ScrollSpy initialization & mobile nav toggle logic
└── index.html        # Main single-page layout & content
```

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- Optional: Local development server (e.g., VS Code Live Server, Python `http.server`, or Node `serve`)

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/PavelT2000/resume.git
   cd resume
   ```
2. Open `index.html` directly in your browser, or serve it locally:
   ```bash
   # Python 3
   python -m http.server 8000
   # Navigate to http://localhost:8000
   ```

### Deployment
This is a static site and can be deployed to any static hosting provider:
- **GitHub Pages:** Push to the `main` branch and enable Pages in repository settings.
- **Netlify/Vercel:** Drag-and-drop the project folder or connect the Git repository for automatic CI/CD.

## ✏️ Content Management
All visible content is hardcoded in `index.html` for simplicity and performance. To update the resume:
1. **Text & Links:** Edit the relevant `<section>` blocks in `index.html`.
2. **Experience Section:** Replace placeholder content in the `#experience` section as professional roles are acquired.
3. **Assets:** Update images in `assets/img/` and adjust `src` paths accordingly. Maintain consistent aspect ratios for optimal rendering.
4. **Reference Data:** Use `data/resume.txt` as a single source of truth when drafting updates before applying them to the HTML.

## 📬 Contact
- **Name:** Pavel Zabelich
- **Location:** Minsk, Belarus
- **Email:** [zabelich.pavel@gmail.com](mailto:zabelich.pavel@gmail.com)
- **Telegram:** [@Seiranami](https://t.me/Seiranami)
- **GitHub:** [PavelT2000](https://github.com/PavelT2000)
- **LinkedIn:** [Pavel Zabelich](https://www.linkedin.com/in/павел-забелич-90545b3b3)

## 📜 License
This project is built upon the **Start Bootstrap Resume** template, licensed under the [MIT License](https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE). All personal content, customizations, and assets are the property of the author.

## 🙏 Acknowledgments
- [Start Bootstrap](https://startbootstrap.com/) for the foundational template
- [Font Awesome](https://fontawesome.com/) & [Flaticon](https://www.flaticon.com/) for iconography
- [Google Fonts](https://fonts.google.com/) for typography