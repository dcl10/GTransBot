from unittest import TestCase
from gtransbot.translation.translation import detect_lang, translate_text


class TestTranslationModule(TestCase):
    def test_detect_lang(self):
        # correctly identifies English phrase
        self.assertEqual(detect_lang("Hello, there"), "en")
        # correctly identifies Japanese phrase
        self.assertEqual(detect_lang("こんにちは"), "ja")

    def test_translate_text(self):
        # correctly translates English to Japanese
        self.assertEqual(translate_text("test"), "テスト")
        # correctly translates Japanese to English
        self.assertEqual(translate_text("テスト", target_lang="en"), "test")
