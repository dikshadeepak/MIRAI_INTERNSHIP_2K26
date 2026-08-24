# ============================================================
# ACCESSAI - AI ACCESSIBILITY ASSISTANT
# ============================================================

from datetime import datetime

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from ai_engine import (
    analyze_image,
    generate_phrase,
    make_speech,
    translate_phrase,
    check_gemini,
    COMMUNICATION_LANGUAGES,
)


# ============================================================
# CONFIG
# ============================================================

st.set_page_config(
    page_title="AccessAI",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background-color: #080808;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: white !important;
}

p, label {
    color: #dddddd;
}

section[data-testid="stSidebar"] {
    background-color: #0d0d0d;
}

section[data-testid="stSidebar"] button {
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background-color: white !important;
    border-radius: 14px;
    padding: 15px;
}

div[data-testid="stMetric"] label,
div[data-testid="stMetric"] label *,
div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] * {
    color: #111111 !important;
    opacity: 1 !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] * {
    color: #111111 !important;
    opacity: 1 !important;
}

/* ============================================================
   SIDEBAR BUTTON TEXT - BLACK
   ============================================================ */

section[data-testid="stSidebar"] .stButton > button {
    border-radius: 10px;
    font-weight: 700;
    color: #111111 !important;
}

section[data-testid="stSidebar"] .stButton > button p {
    color: #111111 !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] .stButton > button span {
    color: #111111 !important;
    opacity: 1 !important;
}

section[data-testid="stSidebar"] .stButton > button div {
    color: #111111 !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    color: #111111 !important;
}

section[data-testid="stSidebar"] .stButton > button:hover p,
section[data-testid="stSidebar"] .stButton > button:hover span,
section[data-testid="stSidebar"] .stButton > button:hover div {
    color: #111111 !important;
}

div[data-testid="stFileUploader"] {
    background-color: white;
    border-radius: 12px;
    padding: 10px;
}

textarea,
input {
    border-radius: 10px !important;
}

.access-card {
    background: white !important;
    color: #111111 !important;
    padding: 22px;
    border-radius: 16px;
    margin-bottom: 15px;
}

.access-card h3,
.access-card h3 *,
.access-card p,
.access-card p * {
    color: #111111 !important;
    opacity: 1 !important;
}
/* ============================================================
   SIDEBAR TEXT VISIBILITY
   ============================================================ */

section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li,
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] label {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] a {
    color: #ffffff !important;
    text-decoration: none !important;
}

section[data-testid="stSidebar"] a:hover {
    color: #dddddd !important;
}


</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {

    "page": "Dashboard",

    "vision_history": [],

    "communication_history": [],

    "images_analyzed": 0,

    "explanations": 0,

    "phrases_generated": 0,

    "total_activity": 0,

    "language": "English",

    "voice_speed": 1.0,

    "auto_play": False,

    "last_phrase": "",

    "last_analysis": None,

    "translation_result": "",

}

for key, value in DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# HELPERS
# ============================================================

# ============================================================
# COMMUNICATION LANGUAGE CATALOGUE
# ============================================================

COMMUNICATION_LANGUAGES = [
    "English",
    "Hindi",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Gujarati",
    "Urdu",
    "Kannada",
    "Odia",
    "Malayalam",
    "Punjabi",
    "Assamese",
    "Maithili",
    "Sanskrit",
    "Kashmiri",
    "Konkani",
    "Nepali",
    "Sindhi",
    "Dogri",
    "Manipuri",
    "Bodo",
    "Spanish",
    "French",
    "German",
    "Italian",
    "Portuguese",
    "Russian",
    "Arabic",
    "Chinese",
    "Japanese",
    "Korean",
    "Turkish",
    "Dutch",
    "Polish",
    "Ukrainian",
    "Vietnamese",
    "Thai",
    "Indonesian",
    "Malay",
    "Swedish",
    "Danish",
    "Norwegian",
    "Finnish",
    "Greek",
    "Hebrew",
    "Romanian",
    "Czech",
    "Hungarian",
]


def language_code(language):
    return {
        "English": "en", "Hindi": "hi", "Bengali": "bn", "Telugu": "te",
        "Marathi": "mr", "Tamil": "ta", "Gujarati": "gu", "Urdu": "ur",
        "Kannada": "kn", "Odia": "or", "Malayalam": "ml", "Punjabi": "pa",
        "Assamese": "as", "Nepali": "ne", "Sanskrit": "sa",
        "Chinese": "zh-CN", "Japanese": "ja", "Korean": "ko", "Spanish": "es",
        "French": "fr", "German": "de", "Italian": "it", "Portuguese": "pt",
        "Russian": "ru", "Arabic": "ar", "Turkish": "tr", "Dutch": "nl",
        "Polish": "pl", "Ukrainian": "uk", "Vietnamese": "vi", "Thai": "th",
        "Indonesian": "id", "Malay": "ms", "Swedish": "sv", "Danish": "da",
        "Norwegian": "no", "Finnish": "fi", "Greek": "el", "Hebrew": "he",
        "Romanian": "ro", "Czech": "cs", "Hungarian": "hu",
    }.get(language, "en")



def now_string():

    return datetime.now().strftime(
        "%d %b %Y, %I:%M %p"
    )


def add_activity(
    activity_type,
    activity,
    language="English"
):

    item = {

        "Type": activity_type,

        "Activity": activity,

        "Language": language,

        "Time": now_string()

    }

    if activity_type == "Vision":

        st.session_state.vision_history.insert(
            0,
            item
        )

    else:

        st.session_state.communication_history.insert(
            0,
            item
        )

    st.session_state.total_activity += 1


def all_activity():

    rows = (
        st.session_state.vision_history
        +
        st.session_state.communication_history
    )

    return rows


def go_to(page):

    st.session_state.page = page

    st.rerun()


def show_result(label, value):

    st.markdown(
        f"""
<div class="result-card">

<div class="result-title">
{label}
</div>

<div class="result-value">
{value}
</div>

</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("♿ AccessAI")

    st.caption(
        "Accessibility Intelligence Platform"
    )
    st.caption(
        "❤️ Designed & Developed by Diksha Deepak"
        )

    st.divider()

    st.subheader("Workspace")

    if st.button(
        "🏠 Dashboard",
        use_container_width=True
    ):
        go_to("Dashboard")

    if st.button(
        "🖼️ Vision Assistant",
        use_container_width=True
    ):
        go_to("Vision Assistant")

    if st.button(
        "🔊 Communicator",
        use_container_width=True
    ):
        go_to("Communicator")

    if st.button(
        "📊 Activity History",
        use_container_width=True
    ):
        go_to("Activity History")

    if st.button(
        "⚙️ Settings",
        use_container_width=True
    ):
        go_to("Settings")

    st.divider()

    try:

        check_gemini()

        st.success(
            "Gemini AI connected"
        )

    except Exception:

        st.error(
            "Gemini API not configured"
        )

    st.caption(
        "Vision + Communication + Voice"
    )
    st.divider()

    # ========================================================
    # ABOUT ME
    # ========================================================

    st.subheader("About Me")

    st.markdown(
        "**Developed by Diksha Deepak**"
    )

    st.write(
        "B.Tech CSE (AI & ML) student passionate about "
        "Artificial Intelligence, accessibility technology, "
        "and building practical AI-powered solutions."
    )

    # ========================================================
    # CONTACT ME
    # ========================================================

    st.subheader("Contact Me")

    st.markdown(
        "📧 **Email:**  dikshadeepak0195@gmail.com"
    )

    st.markdown(
        "💼 **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/diksha-deepak-72bab7391)"
    )

    st.markdown(
        "💻 **GitHub:** [GitHub Profile](https://github.com/dikshadeepak)"
    )

# ============================================================
# TOP BAR
# ============================================================

top1, top2 = st.columns(
    [4, 1]
)

with top1:

    st.title("AccessAI")

    st.caption(
        "Multimodal accessibility intelligence platform"
    )

with top2:

    st.success(
        "● AI SYSTEM ONLINE"
    )


# ============================================================
# DASHBOARD
# ============================================================

if st.session_state.page == "Dashboard":

    st.header("Dashboard")

    st.write(
        "Your AI accessibility assistant for visual understanding "
        "and accessible communication."
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Images Analyzed",
            st.session_state.images_analyzed
        )

    with c2:

        st.metric(
            "AI Explanations",
            st.session_state.explanations
        )

    with c3:

        st.metric(
            "Voice Phrases",
            st.session_state.phrases_generated
        )

    with c4:

        st.metric(
            "Total Activity",
            st.session_state.total_activity
        )

    st.divider()

    st.subheader("Quick Actions")

    q1, q2 = st.columns(2)

    with q1:

        st.markdown(
            """
<div class="access-card">

<h3>🖼️ Vision Assistant</h3>

<p>
Upload or capture a sign, map, notice, symbol or
other visual information and Gemini will explain it
in simple accessible language.
</p>

</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "ANALYZE AN IMAGE →",
            use_container_width=True,
            key="dashboard_vision"
        ):

            go_to("Vision Assistant")

    with q2:

        st.markdown(
            """
<div class="access-card">

<h3>🔊 Communicator</h3>

<p>
Generate a simple communication phrase and convert
it into speech using the expanded Indian and international language catalogue.
</p>

</div>
""",
            unsafe_allow_html=True
        )

        if st.button(
            "OPEN COMMUNICATOR →",
            use_container_width=True,
            key="dashboard_communicator"
        ):

            go_to("Communicator")

    st.divider()

    left, right = st.columns(
        [1.5, 1]
    )

    with left:

        st.subheader("Recent Activity")

        activities = all_activity()

        if activities:

            for item in activities[:5]:

                icon = (
                    "🖼️"
                    if item["Type"] == "Vision"
                    else "🔊"
                )

                st.write(
                    f"{icon} **{item['Activity']}**"
                )

                st.caption(
                    item["Time"]
                )

        else:

            st.info(
                "No activity yet."
            )

    with right:

        st.subheader("System Status")

        st.success(
            "Gemini AI — READY"
        )

        st.success(
            "Vision Engine — READY"
        )

        st.success(
            "Communication — READY"
        )

        st.success(
            "Voice Output — READY"
        )


# ============================================================
# VISION ASSISTANT
# ============================================================

elif st.session_state.page == "Vision Assistant":

    st.header("Vision Assistant")

    st.write(
        "Turn confusing visual information into simple, "
        "actionable language."
    )

    st.divider()

    left, right = st.columns(2)

    # ========================================================
    # INPUT
    # ========================================================

    with left:

        st.subheader("Visual Input")

        st.write(
            "Upload a sign, map, notice, symbol or image."
        )

        input_mode = st.radio(
            "Input method",
            [
                "Upload Image",
                "Use Camera"
            ],
            horizontal=True
        )

        image_file = None

        if input_mode == "Upload Image":

            image_file = st.file_uploader(
                "Choose an image",
                type=[
                    "jpg",
                    "jpeg",
                    "png",
                    "webp"
                ],
                key="vision_uploader"
            )

        else:

            image_file = st.camera_input(
                "Take a photo",
                key="vision_camera"
            )

        if image_file:

            st.image(
                image_file,
                caption="Selected visual",
                use_container_width=True
            )

            if st.button(
                "🔍 ANALYZE WITH GEMINI",
                type="primary",
                use_container_width=True,
                key="analyze_image_button"
            ):

                try:

                    with st.spinner(
                        "Gemini is analyzing the image..."
                    ):

                        result = analyze_image(
                            image_file.getvalue(),
                            image_file.type
                        )

                    st.session_state.last_analysis = result

                    st.session_state.images_analyzed += 1

                    st.session_state.explanations += 1

                    add_activity(
                        "Vision",
                        result.get(
                            "title",
                            "Image analyzed"
                        ),
                        st.session_state.language
                    )

                    st.success(
                        "Image analyzed successfully."
                    )

                except Exception as exc:

                    st.error(
                        str(exc)
                    )

    # ========================================================
    # RESULT
    # ========================================================

    with right:

        st.subheader("AI Explanation")

        result = st.session_state.last_analysis

        if result:

            show_result(
                "What is this?",
                result.get(
                    "title",
                    "Not available"
                )
            )

            show_result(
                "Meaning",
                result.get(
                    "meaning",
                    "Not available"
                )
            )

            show_result(
                "Important Warning",
                result.get(
                    "important_warning",
                    "None identified"
                )
            )

            show_result(
                "Simple Explanation",
                result.get(
                    "simple_explanation",
                    "Not available"
                )
            )

            show_result(
                "Recommended Action",
                result.get(
                    "recommended_action",
                    "Not available"
                )
            )

            confidence = result.get(
                "confidence",
                "Unknown"
            )

            st.info(
                f"AI confidence: **{confidence}**"
            )

            explanation = result.get(
                "simple_explanation",
                ""
            )

            if explanation:

                if st.button(
                    "🔊 READ EXPLANATION ALOUD",
                    use_container_width=True,
                    key="vision_speak"
                ):

                    try:

                        audio = make_speech(
                            explanation,
                            language="en"
                        )

                        st.audio(
                            audio,
                            format="audio/mp3"
                        )

                    except Exception as exc:

                        st.warning(
                            f"Voice output unavailable: {exc}"
                        )

        else:

            st.info(
                "Upload or capture an image to begin."
            )


# ============================================================
# COMMUNICATOR
# ============================================================

elif st.session_state.page == "Communicator":

    st.header("Communicator")

    st.write(
        "Create a simple communication message and speak it aloud."
    )

    st.divider()

    left, right = st.columns(
        [1.2, 1]
    )

    # ========================================================
    # QUICK PHRASES
    # ========================================================

    with left:

        st.subheader(
            "Quick Communication"
        )

        phrases = [

            ("🆘", "I need help."),

            (
                "🚑",
                "I need medical assistance."
            ),

            (
                "💧",
                "I need water."
            ),

            (
                "🍽️",
                "I need food."
            ),

            (
                "🚻",
                "I need to use the restroom."
            ),

            (
                "📞",
                "Please call someone for me."
            )

        ]

        cols = st.columns(2)

        for i, (icon, phrase) in enumerate(
            phrases
        ):

            with cols[i % 2]:

                if st.button(
                    f"{icon} {phrase}",
                    use_container_width=True,
                    key=f"quick_{i}"
                ):

                    st.session_state.last_phrase = phrase

                    st.session_state.translation_result = ""

                    st.session_state.phrases_generated += 1

                    add_activity(
                        "Voice",
                        phrase,
                        st.session_state.language
                    )

                    if st.session_state.auto_play:

                        try:

                            lang_code = language_code(st.session_state.language)

                            audio = make_speech(
                                phrase,
                                lang_code
                            )

                            st.audio(
                                audio,
                                format="audio/mp3"
                            )

                        except Exception:
                            pass

        st.divider()

        st.subheader(
            "Custom Message"
        )

        user_request = st.text_area(
            "What would you like to communicate?",
            placeholder=(
                "Example: Tell someone that I need help "
                "finding the nearest bus stop."
            ),
            height=120
        )

        language = st.selectbox(
            "Output language",
            COMMUNICATION_LANGUAGES,
            index=COMMUNICATION_LANGUAGES.index(
                st.session_state.language
            )
        )

        if st.button(
            "✨ GENERATE ACCESSIBLE PHRASE",
            type="primary",
            use_container_width=True
        ):

            if not user_request.strip():

                st.warning(
                    "Please describe what you want to communicate."
                )

            else:

                try:

                    with st.spinner(
                        "Generating communication phrase..."
                    ):

                        generated = generate_phrase(
                            user_request,
                            language
                        )

                    st.session_state.last_phrase = generated

                    st.session_state.language = language

                    st.session_state.translation_result = ""

                    st.session_state.phrases_generated += 1

                    add_activity(
                        "Voice",
                        generated,
                        language
                    )

                    st.success(
                        "Phrase generated."
                    )

                except Exception as exc:

                    st.error(
                        str(exc)
                    )

    # ========================================================
    # CURRENT MESSAGE
    # ========================================================

    with right:

        st.subheader(
            "Current Message"
        )

        phrase = st.session_state.last_phrase

        if phrase:

            st.markdown(
                f"""
<div class="access-card"
style="border:2px solid #d71920;text-align:center;">

<h3>READY TO SPEAK</h3>

<p style="font-size:22px;font-weight:700;">
{phrase}
</p>

</div>
""",
                unsafe_allow_html=True
            )

            if st.button(
                "🔊 PLAY VOICE",
                type="primary",
                use_container_width=True
            ):

                try:

                    voice_code = language_code(st.session_state.language)

                    audio = make_speech(
                        phrase,
                        voice_code
                    )

                    st.audio(
                        audio,
                        format="audio/mp3"
                    )

                except Exception as exc:

                    st.error(
                        f"Voice generation failed: {exc}"
                    )

            st.divider()

            st.subheader(
                "Translation"
            )

            target = st.selectbox(
                "Translate to",
                COMMUNICATION_LANGUAGES,
                key="translation_target"
            )

            if st.button(
                "🌐 TRANSLATE CURRENT MESSAGE",
                use_container_width=True
            ):

                try:

                    translated = translate_phrase(
                        phrase,
                        target
                    )

                    st.session_state.translation_result = translated

                except Exception as exc:

                    st.error(
                        str(exc)
                    )

            if st.session_state.translation_result:

                st.success(
                    st.session_state.translation_result
                )

        else:

            st.info(
                "Choose a quick phrase or generate a custom message."
            )


# ============================================================
# ACTIVITY HISTORY
# ============================================================

elif st.session_state.page == "Activity History":

    st.header("Activity History")

    st.write(
        "Review your current AccessAI session."
    )

    rows = all_activity()

    if rows:

        filter_type = st.selectbox(
            "Filter activity",
            [
                "All",
                "Vision",
                "Voice"
            ]
        )

        if filter_type != "All":

            rows = [
                row for row in rows
                if row["Type"] == filter_type
            ]

        df = pd.DataFrame(rows)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            "⬇️ DOWNLOAD ACTIVITY CSV",
            data=csv_data,
            file_name="accessai_activity.csv",
            mime="text/csv",
            use_container_width=True
        )

        if st.button(
            "🗑️ CLEAR HISTORY",
            use_container_width=True
        ):

            st.session_state.vision_history = []

            st.session_state.communication_history = []

            st.session_state.total_activity = 0

            st.rerun()

    else:

        st.info(
            "No activity yet."
        )


# ============================================================
# SETTINGS
# ============================================================

elif st.session_state.page == "Settings":

    st.header("Settings")

    st.write(
        "Personalize your accessibility experience."
    )

    st.divider()

    language = st.selectbox(
        "Default language",
        [
            "English",
            "Hindi",
            "Hinglish"
        ],
        index=[
            "English",
            "Hindi",
            "Hinglish"
        ].index(
            st.session_state.language
        )
    )

    st.session_state.language = language

    speed = st.slider(
        "Voice speed",
        0.7,
        1.5,
        float(
            st.session_state.voice_speed
        ),
        0.1
    )

    st.session_state.voice_speed = speed

    auto_play = st.toggle(
        "Auto-play generated voice",
        value=st.session_state.auto_play
    )

    st.session_state.auto_play = auto_play

    st.divider()

    st.subheader(
        "Accessibility Features"
    )

    st.info(
        "AccessAI provides large controls, simple language, "
        "high contrast, image understanding, communication "
        "phrase generation, translation and text-to-speech."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AccessAI • AI-powered accessibility assistant"
)
