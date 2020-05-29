import discord
from discord.ext import commands
import async_cleverbot as ac


class CleverbotCog(commands.Cog):
    """Commands for interacting with the Travitia Cleverbot API"""

    def __init__(self, bot):
        self.bot = bot
        self.cleverbot = ac.Cleverbot("Your TravitiaAPI Key")
        self.cleverbot.set_context(ac.DictContext(self.cleverbot))

    @commands.command(name="botarc", aliases=["ba"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cleverbot_(self, ctx, *, query: str):
        """Ask Cleverbot a question!"""
        await ctx.trigger_typing()
        try:
            r = await self.cleverbot.ask(query, ctx.author.id)
        except ac.InvalidKey:
            return await ctx.send(
                "An error has occurred. The API key provided was not valid."
            )
        except ac.APIDown:
            return await ctx.send("I have to sleep sometimes. Please ask me later!")
        else:
            await ctx.send("{}, {}".format(ctx.author.mention, r.text))

    def cog_unload(self):
        self.bot.loop.create_task(self.cleverbot.close())


def setup(bot):
    bot.add_cog(CleverbotCog(bot))