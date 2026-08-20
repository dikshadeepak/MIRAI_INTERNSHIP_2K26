# 🧠 LIFE-OS

```text
╔════════════════════════════════════════════════════════════╗
║                       LIFE-OS v1.0                         ║
║              DIGITAL WELLBEING COMMAND CENTER             ║
╚════════════════════════════════════════════════════════════╝

> initializing Life-OS...
> loading screen-time data...
> analyzing digital habits...
> connecting AI coach...
> system ready.
```

## 🚀 About

**Life-OS** is an AI-powered digital wellbeing dashboard built for the **MirAI School of Technology Virtual Summer Internship 2026 — AI Builder Track**.

The goal of Life-OS is to help users understand their daily screen-time habits and turn raw usage data into practical lifestyle improvements.

Instead of simply telling users to "use their phone less," Life-OS analyzes their screen-time patterns and uses Gemini AI to provide personalized, practical and real-world alternatives.

---

## ✨ Features

* 📊 **14-Day Screen-Time Visualization**
* 📱 **App-Level Usage Analysis**
* 🧩 **Category-Level Usage Analysis**
* 🎯 **Custom Daily Screen-Time Goal**
* 📈 **Daily Screen-Time Trend**
* 🤖 **Gemini AI Wellbeing Coach**
* 💡 **Personalized Lifestyle Recommendations**
* 🔥 **Most-Used App Detection**
* ⚠️ **Goal Overuse Warnings**
* 🔗 **Shareable Accountability Link**
* 🌙 **Professional Dark SaaS Dashboard**
* 🔍 **Selected-Day Raw Data Explorer**

---

## 🧠 How Life-OS Works

```text
                 ┌──────────────────────┐
                 │    screentime.csv    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Pandas DataFrame   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Daily Aggregation  │
                 └──────────┬───────────┘
                            │
              ┌─────────────┴─────────────┐
              ▼                           ▼
      ┌───────────────┐           ┌───────────────┐
      │ App Analysis  │           │Category       │
      │               │           │Analysis       │
      └───────────────┘           └───────┬───────┘
                                          │
                                          ▼
                                ┌──────────────────┐
                                │  Gemini AI Coach │
                                └────────┬─────────┘
                                         │
                                         ▼
                                ┌──────────────────┐
                                │ Personalized     │
                                │ Lifestyle Advice │
                                └──────────────────┘
```

---

## 📊 Dashboard

The Life-OS dashboard provides an interactive command center where users can:

* Select a specific day.
* Set their maximum daily screen-time goal.
* View total screen time.
* Identify their most-used application.
* Compare actual usage against their daily goal.
* Analyze usage by category.
* View the 14-day screen-time trend.
* Generate personalized AI coaching.

---

## 🤖 AI Life Coach

The AI coach is powered by the **Google Gemini API**.

The application first converts the selected day's Pandas data into a clean summarized string.

The summarized data contains:

* Total screen time
* Daily goal
* Category usage
* Application usage
* Most-used application

Gemini then analyzes this information and provides a structured coaching report.

### AI Coach Sections

```text
## Reality Check

## Biggest Time Leak

## What To Replace It With

## Tomorrow's Action Plan

## Coach's Verdict
```

The coach is designed to be **brutal-but-fair**:

* Honest about excessive screen time
* Respectful toward the user
* Specific instead of generic
* Focused on practical lifestyle changes
* Provides offline alternatives

---

## 🌱 Real-World Replacements

Instead of generic advice like:

```text
"Use your phone less."
```

Life-OS asks the AI to recommend practical alternatives.

For example:

### Social Media

```text
📱 Social Media
        ↓
🚶 Walking
📚 Reading
🏃 Exercise
👥 Meeting friends
📝 Journaling
```

### Entertainment

```text
📺 Entertainment
        ↓
🍳 Cooking
🎵 Music
🏃 Sports
🎨 Creative hobbies
🌳 Outdoor activities
```

### Passive Browsing

```text
🌐 Passive Browsing
        ↓
📖 Reading
📝 Planning
📚 Studying
🧹 Organizing
🚶 Outdoor activity
```

---

## 🔗 Innovation Feature

### Shareable Accountability Link

Life-OS implements the **Shareable Accountability Link** innovation.

The application uses Streamlit query parameters to store:

* Selected date
* Total screen time

Example:

```text
https://your-app.streamlit.app/?date=2026-08-14&minutes=395
```

This allows a user to share their daily screen-time statistics with an accountability partner.

---

## 📁 Project Structure

```text
life-os/
│
├── app.py
├── screentime.csv
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── config.toml
```

### Secret Configuration

During local development, a secret file may be created:

```text
.streamlit/secrets.toml
```

This file is intentionally excluded from GitHub using `.gitignore`.

---

## 🛠️ Tech Stack

```text
Python
│
├── Streamlit
│   └── Dashboard & UI
│
├── Pandas
│   └── Data Processing
│
└── Google Gemini API
    └── AI Coaching
```

### Technologies Used

* **Python**
* **Streamlit**
* **Pandas**
* **Google GenAI SDK**
* **Google Gemini API**
* **Git**
* **GitHub**
* **Streamlit Community Cloud**

---

## 📊 Dataset

The application uses a synthetic screen-time dataset because real digital wellbeing APIs such as Apple Screen Time are restricted.

The dataset contains at least 14 days of screen-time information.

### Dataset Columns

```text
Date
App_Name
Category
Minutes_Used
```

### Example

```csv
Date,App_Name,Category,Minutes_Used
2026-08-14,Instagram,Social Media,60
2026-08-14,Netflix,Entertainment,90
2026-08-14,VS Code,Coding,145
2026-08-14,LeetCode,Education,70
2026-08-14,WhatsApp,Social Media,30
```

---

## 🎯 Daily Goal

Users can set their desired maximum screen-time limit using the sidebar slider.

The dashboard compares:

```text
Actual Screen Time
        ↓
Daily Goal
        ↓
Difference
```

Example:

```text
Actual Usage = 395 minutes

Daily Goal = 240 minutes

Difference = +155 minutes
```

The dashboard uses:

```python
delta_color="inverse"
```

so exceeding the screen-time goal is visually represented as negative progress.

---

## 📈 Data Visualization

Life-OS uses Streamlit's built-in visualization components.

### 14-Day Trend

```python
st.line_chart()
```

### Category Usage

```python
st.bar_chart()
```

### Application Usage

```python
st.bar_chart()
```

These visualizations allow users to quickly understand their digital behavior.

---

## 🔐 API Key Security

The Gemini API key is **not stored inside the Python source code**.

For local development, create:

```text
.streamlit/secrets.toml
```

and add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

The secrets file is excluded from GitHub using:

```text
.streamlit/secrets.toml
```

inside `.gitignore`.

For Streamlit Community Cloud deployment, the Gemini API key should be added through the application's **Secrets** configuration.

**Never commit your real API key to GitHub.**

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Enter the project directory

```bash
cd life-os
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API

Create:

```text
.streamlit/secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

### 5. Run Streamlit

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

Life-OS is designed to be deployed using **Streamlit Community Cloud**.

Deployment steps:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Select Repository
       ↓
Select main Branch
       ↓
Select app.py
       ↓
Add GEMINI_API_KEY to Secrets
       ↓
Deploy
```

---

## 🧪 Testing Checklist

Before deployment, verify:

* [x] CSV loads correctly
* [x] Date selector works
* [x] Daily goal slider works
* [x] KPI metrics update
* [x] Most-used app is displayed
* [x] Goal delta is displayed
* [x] 14-day chart is displayed
* [x] Category chart works
* [x] App chart works
* [x] Gemini AI coach works
* [x] AI gives specific recommendations
* [x] Accountability link is generated
* [x] API key is not committed
* [x] Application works on Streamlit Cloud

---

## 📌 Assignment Requirements

| Requirement                   | Status |
| ----------------------------- | ------ |
| Synthetic Dataset             | ✅      |
| 14+ Days of Data              | ✅      |
| Pandas Data Ingestion         | ✅      |
| Sidebar Controls              | ✅      |
| Date Selectbox                | ✅      |
| Daily Goal Slider             | ✅      |
| KPI Metrics                   | ✅      |
| Most Used App                 | ✅      |
| Goal Delta                    | ✅      |
| 14-Day Visualization          | ✅      |
| Data Aggregation              | ✅      |
| Gemini API Integration        | ✅      |
| Specific AI Advice            | ✅      |
| Professional UI               | ✅      |
| `st.columns`                  | ✅      |
| Innovation Feature            | ✅      |
| Shareable Accountability Link | ✅      |
| `st.query_params`             | ✅      |
| `requirements.txt`            | ✅      |
| `.gitignore`                  | ✅      |
| Custom README                 | ✅      |
| GitHub Repository             | ✅      |
| Streamlit Deployment          | ✅      |

---

## 🚀 Future Improvements

Possible future versions of Life-OS could include:

* 🎙️ Voice Journal
* 🧠 Mood tracking
* 📅 Weekly wellbeing reports
* 🏆 Productivity streaks
* 🔔 Smart reminders
* 📱 Real device screen-time integration
* 📊 Monthly analytics
* 👥 Accountability partner dashboard
* 🤖 More personalized AI coaching
* 🌐 Multi-user authentication

---

## 👩‍💻 Author

**Diksha Deepak**

B.Tech CSE — Artificial Intelligence & Machine Learning
```
