import os
from dotenv import load_dotenv
from google.cloud.translate_v3 import TranslationServiceClient
from translation_bot.bot_client import GTransClient

load_dotenv(".env")


if __name__ == "__main__":
    bot = GTransClient(
        command_prefix="!", translation_client=TranslationServiceClient()
    )
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
