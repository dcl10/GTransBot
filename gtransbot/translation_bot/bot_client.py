import os
from discord.ext import commands
from gtransbot.translation import detect_lang, translate_text


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

        # If someone sends a command in the message, execute it
        ctx = await self.get_context(message)
        if ctx.valid:
            await self.process_commands(message)
            return

        # If someone sends a message in the non-default language
        # translate it to the default language
        if detect_lang(self.translation_client, message.content) != os.getenv(
            "DEFAULT_SERVER_LANG"
        ):
            async with message.channel.typing():
                translation = translate_text(
                    self.translation_client,
                    message.content,
                    os.getenv("DEFAULT_SERVER_LANG"),
                )
                await message.reply(translation)
