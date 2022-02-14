import os

from . import client
from google.cloud.translate_v3.types import DetectLanguageResponse


def detect_lang(content: str) -> str:
    """Detect the language of a text string.

    Args:
        content (str): The text in unknown language.

    Returns:
        str: the detected language.
    """
    languages = client.detect_language(
        parent="projects/translation-discord-bot-341022", content=content
    )
    language = languages.languages[0]
    code = language.language_code
    return code


def translate_text(content: str, target_lang: str = "ja") -> str:
    """Translate the content of a string into the target language.

    Args:
        content (str): The text to be translated.
        target_lang (str, optional): The target language code. Defaults to "ja".

    Returns:
        str: The translated content.
    """
    response = client.translate_text(
        contents=[content],
        target_language_code=target_lang,
        parent="projects/translation-discord-bot-341022",
        mime_type="text/plain",
    )
    translation = response.translations[0]
    translated_text = translation.translated_text
    return translated_text
