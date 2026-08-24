# ♿ AccessAI — AI Accessibility Assistant

> An AI-powered accessibility platform designed to make visual information, communication, translation, and voice interaction more accessible and easier to understand.

---

## 📌 Overview

**AccessAI** is a multimodal AI accessibility assistant that combines **Artificial Intelligence, Computer Vision, Natural Language Processing, Translation, and Text-to-Speech** into a single platform.

The system is designed to help users understand visual information and communicate more easily through simple AI-generated language and voice output.

AccessAI provides two major capabilities:

- 🖼️ **Vision Assistant** — Understand and explain visual information using Gemini AI.
- 🔊 **Communicator** — Generate accessible communication phrases, translate them into different languages, and convert them into speech.

The application is built using **Python and Streamlit**, with **Google Gemini AI** powering the intelligent image analysis and communication features.

---
## 🚀 Live Demo

👉 **[Open ACCESSAI Live](YOUR_RENDER_LIVE_URL)**

## 🎯 Problem Statement

People with different accessibility needs may face difficulties when:

- Understanding signs, notices, maps, symbols, or other visual information.
- Communicating their needs quickly.
- Converting messages into speech.
- Communicating across different languages.
- Understanding complex information written in difficult language.

Traditional accessibility tools often focus on only one type of assistance.

**AccessAI combines visual understanding, communication, translation, and voice assistance into one unified platform.**

---

## 💡 Proposed Solution

AccessAI provides an AI-powered interface where users can:

1. Upload or capture an image.
2. Ask Gemini AI to understand the visual information.
3. Receive a simple explanation.
4. Generate communication phrases.
5. Translate messages into multiple languages.
6. Convert messages into speech.
7. Review previous activities.
8. Customize accessibility settings.

---

# ✨ Key Features

## 🖼️ 1. Vision Assistant

The Vision Assistant allows users to upload or capture an image and receive an AI-generated explanation.

### Supported inputs

- JPG
- JPEG
- PNG
- WEBP
- Camera input

### AI analysis includes:

- What is this?
- Meaning
- Important Warning
- Simple Explanation
- Recommended Action
- AI Confidence

This makes complicated visual information easier to understand.

### Example

A user can upload:

- A road sign
- A notice
- A map
- A symbol
- An informational board

The AI analyzes the image and provides an easy-to-understand explanation.

---

# 🔊 2. Communicator

The Communicator helps users create simple messages that can be spoken aloud.

### Quick Communication Phrases

The application provides predefined phrases such as:

- 🆘 I need help.
- 🚑 I need medical assistance.
- 💧 I need water.
- 🍽️ I need food.
- 🚻 I need to use the restroom.
- 📞 Please call someone for me.

Users can select a phrase instantly without typing.

---

# ✨ 3. AI Phrase Generation

Users can enter a custom request such as:

> "Tell someone that I need help finding the nearest bus stop."

The AI generates a simple and accessible communication phrase.

This helps users convert complex requests into clear communication.

---

# 🌐 4. Multilingual Communication

AccessAI supports an expanded language catalogue covering Indian and international languages.

### Indian Languages

- English
- Hindi
- Bengali
- Telugu
- Marathi
- Tamil
- Gujarati
- Urdu
- Kannada
- Odia
- Malayalam
- Punjabi
- Assamese
- Maithili
- Sanskrit
- Kashmiri
- Konkani
- Nepali
- Sindhi
- Dogri
- Manipuri
- Bodo

### International Languages

- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Arabic
- Chinese
- Japanese
- Korean
- Turkish
- Dutch
- Polish
- Ukrainian
- Vietnamese
- Thai
- Indonesian
- Malay
- Swedish
- Danish
- Norwegian
- Finnish
- Greek
- Hebrew
- Romanian
- Czech
- Hungarian

---

# 🔄 5. Translation

Users can translate the currently generated communication message into another supported language.

### Translation Flow

```text
Generated Message
       ↓
Select Target Language
       ↓
AI Translation
       ↓
Translated Message

## AI ARCHITECTURE:
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Streamlit UI       │
                    │      AccessAI        │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┴─────────────────┐
             │                                   │
             ▼                                   ▼
   ┌────────────────────┐              ┌────────────────────┐
   │  Vision Assistant  │              │    Communicator    │
   └─────────┬──────────┘              └─────────┬──────────┘
             │                                   │
             ▼                                   ▼
   ┌────────────────────┐              ┌────────────────────┐
   │   Gemini AI        │              │    Gemini AI       │
   │ Image Analysis     │              │ Phrase Generation  │
   └─────────┬──────────┘              └─────────┬──────────┘
             │                                   │
             │                         ┌─────────┴──────────┐
             │                         │                    │
             │                         ▼                    ▼
             │                ┌────────────────┐   ┌───────────────┐
             │                │  Translation   │   │ Text-to-Speech│
             │                └────────────────┘   └───────────────┘
             │
             └─────────────────┬─────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Accessible Output    │
                    │ Text + Audio         │
                    └──────────────────────┘


## 🛠️ Tech Stack

| Technology    | Purpose                    |
| ------------- | -------------------------- |
| Python        | Core programming language  |
| Streamlit     | Web application interface  |
| Google Gemini | AI story generation        |
| gTTS          | Text-to-speech audio       |
| JSON          | Structured story data      |
| Requests      | API communication          |
| Pillow        | Image processing           |
| Git & GitHub  | Version control            |
| Render        | Deployment                 |


---

## 📂 Project Structure

```text
ACCESSAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── ai_engine.py
│
└── other project files
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd ACCESSAI
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🔐 API Key Setup

ACCESSAI uses the **Google Gemini API**.

### Option 1 — Local `.env` Setup

Create a file named:

```text
.env
```

inside the project root directory.

Add:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Then make sure `.env` is included in `.gitignore`.

**Never upload your API key to GitHub.**

---

## 4. Run the Application Locally

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

If it does not open automatically, copy the URL shown in the terminal and open it in your browser.

---

# ☁️ Deployment on Render

ACCESSAI is deployed using **Render**.

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py 
---

### Live Demo

👉 YOUR_RENDER_LIVE_URL

---


🧑‍💻 AUTHOR
❤️Diksha Deepak

B.Tech — Computer Science & Engineering (AI/ML)

📜 LICENSE

This project was created as part of the **MirAI School of Technology AI Builder Track – Virtual Summer Internship 2026**.

© 2026 YOUR NAME. All rights reserved.

❤️ FINAL NOTE

AccessAI demonstrates how multimodal AI can be combined with thoughtful interface design to build technology that is not only intelligent, but also accessible, understandable, and easy to use.

The project combines AI, computer vision, natural language processing, translation, speech generation, and modern SaaS dashboard design into one complete capstone application.
