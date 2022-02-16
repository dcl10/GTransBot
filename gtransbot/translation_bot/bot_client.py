import os
from discord.ext import commands
from gtransbot.translation.translation import detect_lang, translate_text


class GTransClient(commands.Bot):
    async def on_message(self, message):
        # Do not reply to bots
        if message.author.bot:
            return

        # If someone
        if detect_lang(message.content) != os.getenv("DEFAULT_SERVER_LANG"):
            translation = translate_text(message.content)
            await message.reply(translation)
