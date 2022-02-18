import os
from dotenv import load_dotenv
from google.cloud.translate_v3 import TranslationServiceClient
from translation_bot.bot_client import GTransClient
from translation_bot.translation_cog import Translation

load_dotenv(".env")


if __name__ == "__main__":
    bot = GTransClient(
        command_prefix="!", translation_client=TranslationServiceClient()
    )
    bot.add_cog(Translation())
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
