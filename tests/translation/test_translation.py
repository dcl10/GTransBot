from unittest import TestCase
from gtransbot.translation.translation import detect_lang
import os


class TestDetectLanguage(TestCase):
    def test_detect_lang(self):
        print(os.environ.items())
        print(detect_lang("hello there!"))
        self.assertFalse(True)
