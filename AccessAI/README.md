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

🧑‍💻 AUTHOR
❤️Diksha Deepak

B.Tech — Computer Science & Engineering (AI/ML)

📜 LICENSE

This project is developed as an academic/capstone project.

It may be modified and extended for educational purposes.

❤️ FINAL NOTE

AccessAI demonstrates how multimodal AI can be combined with thoughtful interface design to build technology that is not only intelligent, but also accessible, understandable, and easy to use.

The project combines AI, computer vision, natural language processing, translation, speech generation, and modern SaaS dashboard design into one complete capstone application.
