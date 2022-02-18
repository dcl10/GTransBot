from ast import arg
from discord.ext import commands
from translation import translate_text, detect_lang


class Translation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tr")
    async def translate_msg(self, ctx, lang_name, *args):
        text = " ".join(args)
        async with ctx.channel.typing():
            lang_code = detect_lang(self.bot.translation_client, lang_name)
            translation = translate_text(
                client=self.bot.translation_client, content=text, target_lang=lang_code
            )
            await ctx.message.reply(translation)
