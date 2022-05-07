from discord.ext import commands

class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Loaded memes cog")
        
    @commands.command(name='ping')
    async def ping(self, ctx):
        """Pings, I guess"""
        print("pinging")
        await ctx.send("pong")

# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))