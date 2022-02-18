import os
from dotenv import load_dotenv
from google.cloud.translate_v3 import TranslationServiceClient
from gtransbot.translation_bot.bot_client import GTransClient
from gtransbot.translation_bot.translation_cog import Translation

load_dotenv(".env")


def main():
    bot = GTransClient(
        command_prefix="!", translation_client=TranslationServiceClient()
    )
    bot.add_cog(Translation(bot=bot))
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))


if __name__ == "__main__":
    main()
