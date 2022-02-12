from google.cloud.translate_v3 import TranslationServiceClient

client = TranslationServiceClient.from_service_account_json(
    "venv/translation-config.json"
)
