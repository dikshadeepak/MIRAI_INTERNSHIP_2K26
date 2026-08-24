
import io
import json
import os
import re
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types
from gtts import gTTS



# ENVIRONMENT


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = None

if API_KEY:
    client = genai.Client(api_key=API_KEY)


# MODELS
# Current Gemini models.
# 3.7 Flash is the primary model, with stable fallbacks.
MODELS = [
    "gemini-3.7-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
]

# COMMUNICATION LANGUAGES
# 22 Scheduled Indian languages + major international languages.
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


# CHECK GEMINI

def check_gemini():
    """
    Check whether Gemini is configured.
    """

    if not API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing.\n\n"
            "Create a .env file in the project folder:\n\n"
            "GEMINI_API_KEY=YOUR_API_KEY"
        )

    if client is None:
        raise RuntimeError(
            "Gemini client could not be initialized."
        )


# GEMINI REQUEST WITH FALLBACK

def generate_with_fallback(contents, config=None):

    check_gemini()

    errors = []

    for model in MODELS:

        try:

            print(f"Trying Gemini model: {model}")

            response = client.models.generate_content(
                model=model,
                contents=contents,
                config=config,
            )

            if response is not None:

                text = getattr(
                    response,
                    "text",
                    None
                )

                if text and text.strip():

                    print(
                        f"Gemini SUCCESS: {model}"
                    )

                    return response

                errors.append(
                    f"{model}: Empty response"
                )

        except Exception as exc:

            error = str(exc)

            print(
                f"Gemini FAILED: {model}\n{error}"
            )

            errors.append(
                f"{model}: {error}"
            )

    raise RuntimeError(
        "All Gemini models failed.\n\n"
        + "\n\n".join(errors)
    )


# CLEAN JSON

def clean_json_response(text):

    if not text:
        raise ValueError(
            "Gemini returned an empty response."
        )

    text = text.strip()

    # Remove markdown fences if Gemini still returns them.
    text = re.sub(
        r"```json",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = text.replace(
        "```",
        ""
    ).strip()

    # Try direct JSON first.
    try:
        return json.loads(text)

    except json.JSONDecodeError:
        pass

    # Find JSON object inside extra text.
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:

        raise ValueError(
            "Gemini did not return a valid JSON object."
        )

    json_text = text[start:end + 1]

    try:

        return json.loads(json_text)

    except json.JSONDecodeError as exc:

        raise ValueError(
            "Gemini returned malformed JSON."
        ) from exc


# VISION RESPONSE SCHEMA

VISION_SCHEMA = {
    "type": "OBJECT",
    "properties": {

        "title": {
            "type": "STRING",
            "description":
                "Short description of the visual."
        },

        "meaning": {
            "type": "STRING",
            "description":
                "Meaning of the visual information."
        },

        "important_warning": {
            "type": "STRING",
            "description":
                "Important warning, restriction or uncertainty."
        },

        "simple_explanation": {
            "type": "STRING",
            "description":
                "Simple explanation suitable for accessibility."
        },

        "recommended_action": {
            "type": "STRING",
            "description":
                "Action the user should consider."
        },

        "confidence": {
            "type": "STRING",
            "enum": [
                "High",
                "Medium",
                "Low"
            ],
            "description":
                "Confidence in the interpretation."
        }
    },

    "required": [
        "title",
        "meaning",
        "important_warning",
        "simple_explanation",
        "recommended_action",
        "confidence"
    ]
}


# VISION ASSISTANT

def analyze_image(
    image_bytes,
    mime_type="image/jpeg"
):

    if not image_bytes:
        raise ValueError(
            "Image data is empty."
        )

    if not mime_type:
        mime_type = "image/jpeg"

    prompt = """
You are AccessAI, an accessibility-focused visual assistant.

Analyze the supplied image.

The image can contain:
- road signs
- maps
- notices
- symbols
- instructions
- warnings
- transportation information
- accessibility signs
- public information
- charts
- diagrams
- general visual information

Your task is to convert the visual information into simple,
practical and accessible language.

IMPORTANT:

1. Do not invent unreadable text.
2. If information is unclear, say so.
3. Identify important warnings.
4. Explain the actual meaning.
5. Use simple language.
6. Give a practical recommended action.
7. Do not claim legal certainty.
8. Do not hallucinate details.
9. If there is readable text, accurately summarize it.
10. Keep every field concise.

Return ONLY the structured response matching the supplied schema.
"""

    try:

        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=mime_type
        )

        config = types.GenerateContentConfig(

            temperature=0.2,

            max_output_tokens=1000,

            response_mime_type="application/json",

            response_schema=VISION_SCHEMA,
        )

        response = generate_with_fallback(
            contents=[
                image_part,
                prompt
            ],
            config=config
        )

        result = clean_json_response(
            response.text
        )

        required = [
            "title",
            "meaning",
            "important_warning",
            "simple_explanation",
            "recommended_action",
            "confidence"
        ]

        for field in required:

            if field not in result:

                result[field] = "Not available."

        return result

    except Exception as exc:

        raise RuntimeError(
            f"Gemini Vision error: {exc}"
        ) from exc


# COMMUNICATION PHRASE

def generate_phrase(
    user_request,
    language="English"
):

    if not user_request or not user_request.strip():

        raise ValueError(
            "Please enter what you want to communicate."
        )

    prompt = f"""
You are AccessAI's communication assistant.

User wants to communicate:

{user_request}

Target language:

{language}

Use the selected language exactly. It may be an Indian or international language.

Create exactly ONE short, natural and respectful sentence.

Rules:
- Preserve the user's meaning.
- Do not add information.
- Keep it easy to understand.
- Keep it short.
- No explanations.
- No quotation marks.
- For Hinglish, naturally combine Hindi and English.

Return ONLY the final sentence.
"""

    try:

        config = types.GenerateContentConfig(
            temperature=0.3,
            max_output_tokens=200
        )

        response = generate_with_fallback(
            contents=prompt,
            config=config
        )

        result = response.text.strip()

        if not result:

            raise ValueError(
                "Gemini returned an empty phrase."
            )

        # Remove accidental quotation marks.
        result = result.strip('"').strip("'")

        return result

    except Exception as exc:

        raise RuntimeError(
            f"Phrase generation error: {exc}"
        ) from exc


# TRANSLATION

def translate_phrase(
    text,
    target_language
):

    if not text or not text.strip():

        raise ValueError(
            "Text cannot be empty."
        )

    if not target_language or not target_language.strip():

        raise ValueError(
            "Please select a target language."
        )

    target_language = target_language.strip()

    # Allow only languages available in the AccessAI
    # communication language catalogue.
    if target_language not in COMMUNICATION_LANGUAGES:

        raise ValueError(
            f"Unsupported language: {target_language}. "
            f"Please select a language from COMMUNICATION_LANGUAGES."
        )

    if target_language == "Hinglish":

        language_instruction = """
Convert the phrase into natural Hinglish.

Hinglish means a natural combination of Hindi and English
as commonly spoken in India.

Do not translate every word mechanically.
Keep the sentence natural, simple and conversational.
"""

    else:

        language_instruction = f"""
Translate the phrase naturally into {target_language}.
Use the selected language exactly.
"""

    prompt = f"""
You are AccessAI's multilingual communication assistant.

Translate the following communication phrase.

Phrase:
{text}

Target language:
{target_language}

{language_instruction}

Rules:
- Preserve the exact meaning.
- Do not add information.
- Do not remove important information.
- Keep the sentence natural and respectful.
- Keep it concise.
- Use the correct script for the selected language.
- Do not explain the translation.
- Do not add quotation marks.
- Return ONLY the translated phrase.

The supported language catalogue includes:
{", ".join(COMMUNICATION_LANGUAGES)}
"""

    try:

        config = types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=300
        )

        response = generate_with_fallback(
            contents=prompt,
            config=config
        )

        result = response.text.strip()

        if not result:

            raise ValueError(
                "Gemini returned an empty translation."
            )

        return result.strip('"').strip("'")

    except Exception as exc:

        raise RuntimeError(
            f"Translation error: {exc}"
        ) from exc

# ============================================================
# TEXT TO SPEECH
# ============================================================

# Common gTTS language codes for the expanded catalogue.
TTS_LANGUAGE_CODES = {
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
}


def make_speech(
    text,
    language="en"
):

    if not text or not text.strip():

        raise ValueError(
            "Text cannot be empty."
        )

    buffer = io.BytesIO()

    try:

        # Accept either an AccessAI language name or a gTTS code.
        language = TTS_LANGUAGE_CODES.get(language, language)

        tts = gTTS(
            text=text,
            lang=language,
            slow=False
        )

        tts.write_to_fp(buffer)

        buffer.seek(0)

        return buffer.getvalue()

    except Exception as exc:

        raise RuntimeError(
            f"Text-to-speech error: {exc}"
        ) from exc


# TEST

if __name__ == "__main__":

    print("Testing AccessAI Gemini...")

    response = generate_with_fallback(
        contents="Reply with exactly: AccessAI working",
        config=types.GenerateContentConfig(
            temperature=0.2,
            max_output_tokens=50
        )
    )

    print(response.text)

