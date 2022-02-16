import os
from translation_bot.bot_client import GTransClient


if __name__ == "__main__":
    client = GTransClient(command_prefix="!")
    client.run(os.getenv("DISCORD_BOT_TOKEN"))
