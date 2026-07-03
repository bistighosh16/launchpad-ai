<div align="center">

```
██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗██████╗  █████╗ ██████╗ 
██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔══██╗██╔══██╗██╔══██╗
██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║██████╔╝███████║██║  ██║
██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔═══╝ ██╔══██║██║  ██║
███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║██║     ██║  ██║██████╔╝
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝ 
                                    
                            🚀  A I  🚀
```

# LaunchPad AI

### One sentence to a full landing page blueprint.

*Turn your product idea into a complete landing page — hero, features, FAQs, and a design system — in under a minute.*

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq-F55036?style=for-the-badge)](https://groq.com)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-B57BFF?style=for-the-badge)](LICENSE)

**Made with 💜 by [Vivi](https://github.com/bistighosh16)**

</div>

---

## 🚀 Live Demo

🌐 **[Try LaunchPad AI Live →](https://launchpad-ai-vivi.streamlit.app/)**

---

## ✨ What Is LaunchPad AI?

**LaunchPad AI** is an AI-powered landing page blueprint generator. Describe your product in a single sentence, and it generates a complete, well-structured landing page with:

- 🎯 **Hero Section** — Headlines and CTAs that convert
- ✨ **Feature Highlights** — 4 killer features positioned around user benefits
- 🚀 **How It Works** — 3-step process that reduces friction
- 💬 **Social Proof** — Authentic testimonials and trust signals
- ❓ **Smart FAQs** — Answers to real objections
- 🎨 **Design System** — Custom color palette, typography, and design principles

All wrapped in a beautiful, editorial-grade UI inspired by Framer × Claude's design languages.

---

## 🎨 Design Philosophy

LaunchPad AI's visual identity is a **fusion of two iconic design systems**:

| Inspiration | What We Took |
|-------------|--------------|
| 🖤 **Framer** | Poster-like typography, bold display headlines, gradient spotlight cards |
| 🍦 **Claude (Anthropic)** | Warm editorial tone, serif/sans pairing, cream ↔ dark rhythm |
| 💜 **Vivi Signature** | Purple accent, "Made with 💜" branding, warm midnight canvas |

### The "Warm Midnight" Palette

```
Canvas       #0F0B1A   (warm dark purple-navy)
Surface 1    #1A1526   (elevated cards)
Cream        #F5F0E8   (editorial breaks)
Accent       #B57BFF   (electric purple)
```

### Typography

- **Display:** Fraunces (Google Fonts) — Modern serif with personality
- **Body:** Inter (Google Fonts) — Universal, clean, professional
- **Code:** JetBrains Mono — Developer credibility

---


## 🛠️ Tech Stack

| Category | Technology |
|----------|-----------|
| **Language** | Python 3.11 |
| **Framework** | Streamlit (multi-page app) |
| **AI Model** | Llama 3.3 70B (via Groq API) |
| **Styling** | Custom CSS design system with Google Fonts |
| **Deployment** | Streamlit Cloud |

---

## 🧠 Architecture Highlights

### Multi-Section AI Generation
Instead of one massive prompt, LaunchPad AI calls the AI **6 separate times** — one for each section. This gives:
- 🎯 More focused, higher-quality outputs
- 📊 Reliable structured JSON responses
- ⚡ Live progress updates during generation
- 💪 Ability to retry individual sections

### Specialized AI Personas
Each generator method uses a **dedicated system prompt** with an expert persona:
- Hero: World-class SaaS copywriter
- Features: Product marketer specializing in positioning
- How It Works: UX writer focused on friction reduction
- Social Proof: Conversion psychology expert
- FAQ: Customer success specialist
- Design System: Senior brand designer

### Design System as Code
Every visual token — colors, typography, spacing, shadows — is defined as a CSS variable and applied consistently across both pages via reusable Python helper functions.

---

## 📦 Installation

### Prerequisites

- Python 3.11
- A [Groq API key](https://console.groq.com/keys) (free!)

### Setup

Clone the repo:

```bash
git clone https://github.com/bistighosh16/launchpad-ai.git
cd launchpad-ai
```

Create a virtual environment:

```bash
py -3.11 -m venv venv
```

Activate it (Windows):

```bash
.\venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Add your API key to `.env`:

```
GROQ_API_KEY=your_groq_api_key_here
```

Run it:

```bash
streamlit run Home.py
```

Open your browser to `http://localhost:8501` 🎨

---

## 📁 Project Structure

```
launchpad-ai/
│
├── .streamlit/
│   └── config.toml              # Streamlit theme config
│
├── pages/
│   └── 2_⚡_Generator.py         # AI generator tool
│
├── utils/
│   ├── __init__.py
│   ├── ai_engine.py             # Groq AI logic
│   └── styles.py                # Design system + helpers
│
├── .env                          # API keys (not committed)
├── .gitignore
├── Home.py                       # Landing page
├── requirements.txt
└── README.md
```

---

## 💡 How It Works

1. **User describes their product** in one sentence
2. **AI engine calls Groq's Llama 3.3 70B** six times in sequence
3. **Each call has a specialized system prompt** + expects structured JSON
4. **Progress bar updates** as each section generates
5. **Results render in a beautiful UI** with animations
6. **User can download** the blueprint as Markdown or JSON

---

## 🎯 Use Cases

- 🚀 **Indie hackers** validating startup ideas quickly
- 💼 **Founders** drafting first-version landing pages
- 🎨 **Designers** getting content structure to design around
- ✍️ **Marketers** brainstorming copy variations
- 📚 **Students** learning about landing page anatomy

---

## 🗺️ Roadmap

- [ ] Multiple landing page style variants (SaaS / E-commerce / Portfolio)
- [ ] Export as HTML/CSS (not just Markdown)
- [ ] A/B copy variations
- [ ] Multi-language support
- [ ] Direct integration with design tools (Figma export)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feat/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feat/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **[Groq](https://groq.com)** — For blazing-fast free AI inference
- **[Streamlit](https://streamlit.io)** — For the incredible Python web framework
- **[design.md](https://design.md)** — For the design system inspiration
- **[Framer](https://framer.com)** & **[Anthropic Claude](https://claude.ai)** — For the design language inspiration

---

## 👋 About the Creator

Hi! I'm **Vivi** — a builder who loves crafting beautiful, functional AI products.

- 🏆 National Hardware Hackathon Winner
- 📦 PyPI Publisher ([NeonUI](https://pypi.org/project/neonui/))
- 🌟 Open Source Contributor
- 💜 Building AI products with taste

**Connect with me:**
- 🐙 GitHub: [@bistighosh16](https://github.com/bistighosh16)
- 💼 LinkedIn: [Find me on LinkedIn]()

---

<div align="center">

### If LaunchPad AI helped you ship faster, give it a ⭐️!

**Made with 💜 by Vivi**

*Because launching should be the fun part.*

</div>
