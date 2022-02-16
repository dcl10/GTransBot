from unittest import TestCase
from google.cloud.translate_v3 import TranslationServiceClient
from gtransbot.translation import detect_lang, translate_text


class TestTranslationModule(TestCase):
    def setUp(self):
        self.client = TranslationServiceClient()

    def tearDown(self):
        del self.client

    def test_detect_lang(self):
        # correctly identifies English phrase
        self.assertEqual(detect_lang(self.client, "Hello, there"), "en")
        # correctly identifies Japanese phrase
        self.assertEqual(detect_lang(self.client, "こんにちは"), "ja")

    def test_translate_text(self):
        # correctly translates English to Japanese
        self.assertEqual(translate_text(self.client, "test"), "テスト")
        # correctly translates Japanese to English
        self.assertEqual(translate_text(self.client, "テスト", target_lang="en"), "test")
