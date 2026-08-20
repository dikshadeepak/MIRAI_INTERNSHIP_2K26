import streamlit as st
import pandas as pd
from google import genai
from google.genai import types


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Life-OS | Wellbeing Dashboard",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top right,
            #172033 0%,
            #080b12 35%,
            #05070b 100%
        );
    color: white;
}

[data-testid="stSidebar"] {
    background: #090c13;
    border-right: 1px solid #202938;
}

.main-title {
    font-size: 45px;
    font-weight: 800;
    margin-bottom: 0;
}

.subtitle {
    color: #9ca3af;
    font-size: 17px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 23px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
}

.coach-box {
    background: #101621;
    border: 1px solid #2d3748;
    border-radius: 18px;
    padding: 25px;
    margin-top: 15px;
}

.info-card {
    background: #101621;
    border: 1px solid #202938;
    border-radius: 15px;
    padding: 20px;
}

.share-box {
    background: #101621;
    border: 1px dashed #4b5563;
    border-radius: 15px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD CSV DATA
# =========================================================

@st.cache_data
def load_data():

    data = pd.read_csv("screentime.csv")

    data["Date"] = pd.to_datetime(data["Date"])

    return data


df = load_data()


# =========================================================
# GEMINI CLIENT
# =========================================================

def get_gemini_client():

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

    except Exception:

        st.error(
            "Gemini API key is missing. "
            "Please configure GEMINI_API_KEY in Streamlit Secrets."
        )

        st.stop()

    return genai.Client(api_key=api_key)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# 🧠 Life-OS")

st.sidebar.caption(
    "Personal Digital Wellbeing Command Center"
)

st.sidebar.divider()


# Get available dates

available_dates = sorted(
    df["Date"].dt.strftime("%Y-%m-%d").unique(),
    reverse=True
)


# Date selector

selected_date = st.sidebar.selectbox(
    "📅 Select Day",
    available_dates
)


# Daily goal

daily_goal = st.sidebar.slider(
    "🎯 Daily Screen-Time Goal",
    min_value=60,
    max_value=720,
    value=240,
    step=15
)


st.sidebar.divider()

st.sidebar.markdown("### 📊 Dashboard")

st.sidebar.caption(
    "Track your digital habits and receive "
    "AI-powered lifestyle recommendations."
)


# =========================================================
# FILTER SELECTED DAY
# =========================================================

selected_day = df[
    df["Date"].dt.strftime("%Y-%m-%d") == selected_date
].copy()


# =========================================================
# CALCULATE STATISTICS
# =========================================================

total_today = int(
    selected_day["Minutes_Used"].sum()
)


# App usage

app_usage = (
    selected_day
    .groupby("App_Name")["Minutes_Used"]
    .sum()
    .sort_values(ascending=False)
)


# Category usage

category_usage = (
    selected_day
    .groupby("Category")["Minutes_Used"]
    .sum()
    .sort_values(ascending=False)
)


# Most used app

most_used_app = app_usage.index[0]

most_used_minutes = int(
    app_usage.iloc[0]
)


# Difference from goal

delta_minutes = total_today - daily_goal


# Goal percentage

goal_percentage = (
    total_today / daily_goal * 100
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🧠 Life-OS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your AI-powered digital wellbeing command center'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# KPI ROW
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "📱 Screen Time Today",
        f"{total_today // 60}h {total_today % 60}m",
        f"{delta_minutes:+d} min vs goal",
        delta_color="inverse"
    )


with col2:

    st.metric(
        "🔥 Most Used App",
        most_used_app,
        f"{most_used_minutes} min"
    )


with col3:

    st.metric(
        "🎯 Daily Goal",
        f"{daily_goal // 60}h {daily_goal % 60}m",
        f"{goal_percentage:.0f}% used"
    )


with col4:

    st.metric(
        "🧩 Categories",
        len(category_usage),
        "tracked today"
    )


# =========================================================
# STATUS
# =========================================================

if total_today <= daily_goal:

    st.success(
        f"🟢 **Great!** You stayed within your "
        f"{daily_goal}-minute screen-time goal."
    )

elif total_today <= daily_goal * 1.25:

    st.warning(
        f"🟡 **Warning:** You are "
        f"{total_today - daily_goal} minutes "
        f"above your daily goal."
    )

else:

    st.error(
        f"🔴 **High Usage:** You are "
        f"{total_today - daily_goal} minutes "
        f"above your daily goal."
    )


# =========================================================
# 14-DAY TREND
# =========================================================

st.markdown(
    '<div class="section-title">'
    '📈 14-Day Screen-Time Trend'
    '</div>',
    unsafe_allow_html=True
)


daily_totals = (
    df.groupby("Date")["Minutes_Used"]
    .sum()
    .sort_index()
)


st.line_chart(
    daily_totals,
    height=350
)


# =========================================================
# CATEGORY + APP CHARTS
# =========================================================

left, right = st.columns(2)


with left:

    st.markdown(
        '<div class="section-title">'
        '📊 Usage by Category'
        '</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        category_usage,
        height=300
    )


with right:

    st.markdown(
        '<div class="section-title">'
        '📱 App Breakdown'
        '</div>',
        unsafe_allow_html=True
    )

    st.bar_chart(
        app_usage,
        height=300
    )


# =========================================================
# DATA BRIDGE
# =========================================================

def create_ai_summary(day_data):

    category_summary = (
        day_data
        .groupby("Category")["Minutes_Used"]
        .sum()
        .sort_values(ascending=False)
    )

    app_summary = (
        day_data
        .groupby("App_Name")["Minutes_Used"]
        .sum()
        .sort_values(ascending=False)
    )

    category_text = category_summary.to_string()

    app_text = app_summary.to_string()

    total = int(
        day_data["Minutes_Used"].sum()
    )

    summary = f"""
DATE:
{selected_date}

TOTAL SCREEN TIME:
{total} minutes

DAILY GOAL:
{daily_goal} minutes

CATEGORY USAGE:
{category_text}

APP USAGE:
{app_text}

MOST USED APP:
{app_summary.index[0]} ({int(app_summary.iloc[0])} minutes)
"""

    return summary


ai_data = create_ai_summary(selected_day)


# =========================================================
# GEMINI AI COACH
# =========================================================

def get_coaching_response(summary):

    client = get_gemini_client()

    prompt = f"""
You are Life-OS, a brutal-but-fair digital wellbeing coach.

Analyze the user's screen-time data below.

================ USER DATA ================

{summary}

============================================

Give a complete, personalized coaching report.

IMPORTANT:

- Do NOT shame or insult the user.
- Do NOT simply say "use your phone less."
- Identify the biggest time-consuming category.
- Identify the most-used application.
- Compare screen time with the daily goal.
- Explain the user's behavior pattern.
- Give specific real-world replacements.
- Focus especially on replacing passive entertainment
  and social media with meaningful offline activities.
- Give a practical plan for tomorrow.
- Be direct, honest and useful.

Use EXACTLY these five sections:

## Reality Check

Explain today's screen time compared with the goal.
Mention the total screen time and whether the user exceeded
or stayed below the goal.

## Biggest Time Leak

Identify the biggest category and the biggest app.
Explain where the user's time is going.

## What To Replace It With

Give at least 4 specific offline replacements.
Make them realistic and connected to the user's usage.

Examples:
- walking
- exercise
- reading
- studying
- cooking
- journaling
- hobbies
- meeting friends
- outdoor activities

## Tomorrow's Action Plan

Give 4 concrete actions for tomorrow.

Include specific limits such as:
- social media limit
- entertainment limit
- focused work period
- one offline activity

## Coach's Verdict

Give a short final verdict in 2-3 sentences.

Keep the entire response around 500-700 words maximum.
Do not stop halfway through a section.
"""

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=2500
            )
        )

        if response.text:
            return response.text

        return "The AI coach returned an empty response."

    except Exception as e:

        return f"""
## Gemini API Error

Something went wrong while generating your coaching report.

Error:

`{str(e)}`
"""

# =========================================================
# AI COACH UI
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🤖 AI Life Coach'
    '</div>',
    unsafe_allow_html=True
)


if st.button(
    "🧠 Analyze My Day",
    type="primary",
    use_container_width=True
):

    with st.spinner(
        "Your AI coach is analyzing your habits..."
    ):

        coaching = get_coaching_response(
            ai_data
        )


    st.markdown(
        '<div class="coach-box">',
        unsafe_allow_html=True
    )

    st.markdown(coaching)

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# =========================================================
# RAW DATA
# =========================================================

with st.expander("🔍 View Selected Day Data"):

    st.dataframe(
        selected_day.sort_values(
            "Minutes_Used",
            ascending=False
        ),
        use_container_width=True
    )


# =========================================================
# INNOVATION:
# SHAREABLE ACCOUNTABILITY LINK
# =========================================================

st.markdown(
    '<div class="section-title">'
    '🔗 Accountability Link'
    '</div>',
    unsafe_allow_html=True
)


# Add data to URL

st.query_params["date"] = selected_date

st.query_params["minutes"] = str(
    total_today
)


# Current app URL

base_url = st.context.url.split("?")[0]


share_url = (
    f"{base_url}"
    f"?date={selected_date}"
    f"&minutes={total_today}"
)


st.markdown(
    """
    <div class="share-box">

    <h3>📤 Share Your Daily Stats</h3>

    <p>
    Create an accountability link containing your
    selected date and screen-time total.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


st.code(share_url)


st.caption(
    "Copy this link and share it with an accountability partner."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Life-OS • AI Builder Track • "
    "MirAI School of Technology • Virtual Summer Internship 2026"
)