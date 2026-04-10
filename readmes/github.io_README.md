# 📄 Personal Resume & Portfolio Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Active-brightgreen)](https://github.com/PavelT2000/PavelT2000.github.io)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.2.3-blue)](https://getbootstrap.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A clean, responsive, and professional resume/CV website built with modern web technologies. Designed to showcase educational background, technical skills, and professional experience. Hosted via **GitHub Pages**.

> 🌐 **Note:** The primary content is written in Russian. All text nodes in `index.html` can be easily translated or updated to match your preferred language.

## ✨ Features
- 📱 **Fully Responsive:** Optimized layout for desktop, tablet, and mobile viewports.
- 🧭 **Smooth Navigation:** Fixed sidebar with Bootstrap ScrollSpy and smooth anchor scrolling.
- 🛠️ **Skill Visualization:** Grid-based icon display for programming languages, frameworks, and tools.
- 🔗 **Contact Integration:** Direct links to email, GitHub, and Telegram.
- ⚡ **Lightweight & Fast:** Static HTML/CSS/JS architecture with CDN-loaded dependencies and optimized assets.

## 🛠️ Tech Stack
| Category       | Technology                                      |
|----------------|-------------------------------------------------|
| **Frontend**   | HTML5, CSS3, JavaScript (ES6+)                  |
| **Framework**  | Bootstrap 5.2.3                                 |
| **Icons**      | Font Awesome 6.3.0                              |
| **Typography** | Google Fonts (`Saira Extra Condensed`, `Muli`)  |
| **Hosting**    | GitHub Pages                                    |
| **Base Theme** | [Start Bootstrap - Resume v7.0.6](https://startbootstrap.com/theme/resume) |

## 📁 Project Structure
```
.
├── .aiignore
├── .gitattributes
├── README.md
├── index.html              # Main HTML structure & content
├── css/
│   └── styles.css          # Custom styles & Bootstrap overrides
├── js/
│   └── scripts.js          # ScrollSpy, navbar collapse & UI logic
└── assets/
    └── img/                # Profile photo, tech stack SVGs & favicon
```

## 🚀 Getting Started

### Prerequisites
- A GitHub account
- Basic familiarity with HTML/CSS/JS
- Git (optional, for local development)

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/PavelT2000/PavelT2000.github.io.git
   cd PavelT2000.github.io
   ```
2. Open `index.html` directly in a browser, or serve it locally:
   ```bash
   # Python 3
   python -m http.server 8000
   # Visit: http://localhost:8000
   ```

### Deployment to GitHub Pages
1. Ensure the repository is named `username.github.io` (replace `username` with your GitHub handle).
2. Push the code to the `main` (or `master`) branch.
3. Navigate to **Settings > Pages** in your repository.
4. Set **Source** to `Deploy from a branch` → `main` → `/ (root)`.
5. Click **Save**. Your site will be live at `https://username.github.io` within a few minutes.

## 🎨 Customization Guide
| Task                  | File to Edit                          | Instructions                                                                 |
|-----------------------|---------------------------------------|------------------------------------------------------------------------------|
| Update personal info  | `index.html`                          | Modify text inside `<section id="about">`, `#experience`, `#education`, etc. |
| Change colors/fonts   | `css/styles.css`                      | Override Bootstrap variables or add custom CSS rules.                        |
| Add/remove skills     | `index.html` (`#skills` section)      | Add/remove `<img>` tags in `.dev-icons` and update the checklist below.      |
| Update social links   | `index.html` (`.social-icons`)        | Replace `href` values with your actual profile URLs.                         |
| Replace profile photo | `assets/img/Моя фотка.jpg`            | Overwrite the file or update the `src` path in the navbar.                   |

## 📜 License & Credits
This project is built upon the **[Start Bootstrap Resume](https://startbootstrap.com/theme/resume)** template, which is licensed under the [MIT License](https://github.com/StartBootstrap/startbootstrap-resume/blob/master/LICENSE). All custom content, modifications, and assets are owned by the author.

## 📬 Contact
- **Name:** Zabelich Pavel
- **Email:** [zabelich.pavel@gmail.com](mailto:zabelich.pavel@gmail.com)
- **GitHub:** [@PavelT2000](https://github.com/PavelT2000)
- **Telegram:** [@Seiranami](https://t.me/Seiranami)

---
*Built with ❤️ and hosted on GitHub Pages.*