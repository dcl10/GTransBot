from google.cloud.translate_v3 import TranslationServiceClient
from dotenv import load_dotenv


load_dotenv(".env")


client = TranslationServiceClient()
