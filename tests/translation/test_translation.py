from unittest import TestCase
from gtransbot.translation.translation import detect_lang
import os


class TestDetectLanguage(TestCase):
    def test_detect_lang(self):
        # correctly identifies English phrase
        self.assertEqual(detect_lang("Hello, there"), "en")
        # correctly identifies Japanese phrase
        self.assertEqual(detect_lang("こんにちは"), "ja")
