import os

from . import client
from google.cloud.translate_v3.types import DetectLanguageResponse


def detect_lang(content: str) -> DetectLanguageResponse:
    """Detect the language of a text string.

    Args:
        content (str): The text in unknown language

    Returns:
        DetectLanguageResponse: the detected language
    """
    return client.detect_language(
        parent="projects/translation-discord-bot-341022", content=content
    )
