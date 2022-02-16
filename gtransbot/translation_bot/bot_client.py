import os

from discord.ext import commands


class GTransClient(commands.Bot):
    async def on_ready(self):
        channel = self.get_channel(int(os.getenv("TEST_CHANNEL_ID")))
        await channel.send(
            f"Hello! My name is {self.user.name}. "
            "I can translate your words into any language!"
        )
