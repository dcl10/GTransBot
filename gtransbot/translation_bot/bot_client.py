import os
from discord.ext import commands
from gtransbot.translation.translation import detect_lang, translate_text


class GTransClient(commands.Bot):
    def __init__(
        self,
        command_prefix,
        translation_client,
        help_command=None,
        description=None,
        **options
    ):
        super().__init__(command_prefix, help_command, description, **options)
        self.translation_client = translation_client

    async def on_message(self, message):
        # Do not reply to bots
        if message.author.bot:
            return

        # If someone
        if detect_lang(message.content) != os.getenv("DEFAULT_SERVER_LANG"):
            translation = translate_text(message.content)
            await message.reply(translation)
