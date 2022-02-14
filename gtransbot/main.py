import os
from translation_bot.bot_client import GTransClient
from dotenv import load_dotenv

load_dotenv(".env")

if __name__ == "__main__":
    client = GTransClient()
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
