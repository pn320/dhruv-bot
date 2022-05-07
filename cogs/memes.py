import random
from discord.ext import commands
from discord import Message

class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Loaded memes cog")
        
    @commands.command(name='ping')
    async def ping(self, ctx):
        """Pings, I guess"""
        await ctx.send("this command doesn't work")
        
    @commands.Cog.listener('on_message')
    async def send_dhruv_meme(self, message: Message):
        if message.author == self.bot.user:
            return

        # meme message for dhruv
        if message.author.display_name == 'Dhruv':
            if random.random() >= 0.80:
                await message.channel.send(f'dhruv you can come out now.')

    @commands.Cog.listener('on_message')
    async def send_rahul_meme(message: Message):
        print(f'{message.author.display_name}')
        if message.author == bot.user:
            return

        # meme message for dhruv
        if message.author.display_name == 'Rahul':
            if random.random() >= 0.80:
                await message.channel.send(f'rahul you can come out now.')

# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))
