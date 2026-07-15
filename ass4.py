import streamlit as st
import requests
import random
from urllib.parse import quote

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title=" AI Image Studio",
    page_icon="🎨",
    layout="centered",
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

/* Background */
.stApp{
    background: linear-gradient(135deg,#0f172a,#111827,#1e293b);
    color:white;
}

/* Main Container */
.block-container{
    padding-top:2rem;
    max-width:950px;
}

/* Titles */
h1{
    text-align:center;
    color:white !important;
    font-size:46px !important;
    font-weight:800;
}

h2,h3,h4{
    color:white !important;
}

/* Paragraph */
p,label{
    color:#d1d5db !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:linear-gradient(
    180deg,
    #111827,
    #0f172a,
    #020617
    );
}

section[data-testid="stSidebar"] *{
    color:white !important;
}
            /* Selected value inside selectbox */
section[data-testid="stSidebar"] div[data-baseweb="select"] span{
    color:black !important;
}

/* Input text */
section[data-testid="stSidebar"] input{
    color:black !important;
}

/* Textarea */
section[data-testid="stSidebar"] textarea{
    color:black !important;
}

/* Text Input */
.stTextInput input{
    background:white;
    color:black;
    border-radius:12px;
}

/* Text Area */
textarea{
    color:black !important;
}

/* Selectbox */
div[data-baseweb="select"]{
    color:black;
}

/* Slider */
.stSlider{
    padding-top:10px;
    padding-bottom:10px;
}

/* Buttons */
.stButton>button{

    width:100%;
    height:48px;

    background:linear-gradient(
    90deg,
    #2563eb,
    #06b6d4
    );

    color:white;

    border:none;

    border-radius:12px;

    font-size:18px;

    font-weight:bold;

    transition:.3s;

}

.stButton>button:hover{

    transform:scale(1.02);

    box-shadow:0 0 18px rgba(37,99,235,.5);

}

/* Image */

img{

    border-radius:18px;

}

/* Success Box */

[data-testid="stAlert"]{

    border-radius:14px;

}

/* Scrollbar */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#3b82f6;

    border-radius:20px;

}

.footer{

    text-align:center;

    color:#cbd5e1;

    margin-top:30px;

    font-size:15px;

}

</style>
""", unsafe_allow_html=True)
# ============================================================
#                    SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎨 AI Image Studio")

    st.success("🟢 Pollinations AI Connected")

    st.divider()

    st.subheader("🎭 Art Style")

    art_style = st.selectbox(
        "Choose an Art Style",
        [
            "Realistic",
            "Anime",
            "Oil Painting",
            "Watercolor",
            "Digital Art",
            "Fantasy",
            "Cyberpunk",
            "Pixel Art",
            "3D Render",
            "Sketch"
        ]
    )

    st.divider()

    st.subheader("🖼 Image Size")

    width = st.slider(
        "Width",
        min_value=256,
        max_value=1024,
        value=512,
        step=64
    )

    height = st.slider(
        "Height",
        min_value=256,
        max_value=1024,
        value=512,
        step=64
    )

    st.divider()

    # Assignment Task 3
    magic_enhance = st.checkbox(
        "✨ Enable Magic Enhance"
    )

    st.divider()

    st.info("""
### Assignment Features

✅ Working Width Slider

✅ Working Height Slider

✅ Magic Enhance

✅ Surprise Me

✅ Download PNG
""")

    st.divider()

    st.caption("❤️ Developed by Diksha Deepak")


#                  MAIN PAGE
st.title("🎨 AI Image Studio")

st.caption(
    "❤️ Developed by Diksha Deepak"
)

st.info(
"""
👋 Welcome!

Describe anything you can imagine and let AI turn it into beautiful artwork.

You can also enable **Magic Enhance** for much higher quality images.
"""
)


# PROMPT INPUT


prompt = st.text_area(
    "📝 Enter your prompt",
    height=120,
    placeholder="Example: A futuristic city floating in the clouds at sunset..."
)


# SURPRISE PROMPTS


surprise_prompts = [

    "An astronaut riding a horse on Mars",

    "A cyberpunk street food vendor in Tokyo",

    "A dragon reading books inside a magical library",

    "A floating island with glowing waterfalls",

    "A giant panda driving a Formula One race car"

]

# BUTTONS


col1, col2 = st.columns(2)

with col1:

    generate = st.button(
        "🎨 Generate Image"
    )

with col2:

    surprise = st.button(
        "🎲 Surprise Me!"
    )
# IMAGE GENERATION FUNCTION

def generate_image(user_prompt):

    
    full_prompt = f"{user_prompt}, {art_style}"

    
    # TASK 3 : MAGIC ENHANCE
    
    if magic_enhance:

        full_prompt += (
            ", masterpiece,"
            " 8k resolution,"
            " highly detailed,"
            " trending on artstation,"
            " unreal engine 5 render"
        )

    # Encode spaces and special characters
    encoded_prompt = quote(full_prompt)

    # ========================================================
    # TASK 1 : FIX WIDTH & HEIGHT SLIDERS
    # ========================================================
    url = (
        f"https://image.pollinations.ai/prompt/"
        f"{encoded_prompt}"
        f"?width={width}&height={height}"
    )

    with st.spinner("🎨 Creating your masterpiece..."):

        try:

            response = requests.get(url)

            if response.status_code == 200:

                st.success("✅ Image Generated Successfully!")

                st.image(
                    response.content,
                    caption="Generated AI Artwork",
                    use_container_width=True
                )

                # ====================================================
                # TASK 2 : DOWNLOAD BUTTON (.png)
                # ====================================================
                st.download_button(
                    label="📥 Download Image",
                    data=response.content,
                    file_name=f"{art_style}_image.png",
                    mime="image/png"
                )

            else:

                st.error(
                    "❌ Failed to generate image."
                )

        except Exception as e:

            st.error(f"❌ {e}")


# ============================================================
# GENERATE BUTTON
# ============================================================

if generate:

    if prompt.strip() == "":

        st.warning(
            "⚠ Please enter a prompt first."
        )

    else:

        generate_image(prompt)


# ============================================================
# TASK 4 : SURPRISE ME
# ============================================================

if surprise:

    random_prompt = random.choice(
        surprise_prompts
    )

    st.success(
        f"🎲 Surprise Prompt:\n\n{random_prompt}"
    )

    generate_image(random_prompt)










VIDEO LINK:
https://github.com/dikshadeepak/MIRAI_INTERNSHIP_2K26/blob/main/ass4.mp4
