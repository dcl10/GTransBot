import os
from google.cloud.translate_v3 import TranslationServiceClient
import google.auth


os.environ.update({"GOOGLE_APPLICATION_CREDENTIALS": "venv/translation-config.json"})

client = TranslationServiceClient()
