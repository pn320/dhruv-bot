import os
import random

from dotenv import load_dotenv
from discord import Message
from discord.ext import commands

def dhruv_display_name():
    load_dotenv()
    DHRUV_ID = os.environ.get('DHRUV_ID', None)
    return "Dhruv" if None else f'<@{DHRUV_ID}>'

DHRUV_DISPLAY_NAME = dhruv_display_name()
DHRUV_MEMES = [
    f"I'm {DHRUV_DISPLAY_NAME} and I love Python.",
    f"{DHRUV_DISPLAY_NAME} you can come out now.",
]

class Memes(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.dhruv_meme_threshold = 0.69
        print("Loaded memes cog")
        
    @commands.command(name='ping')
    async def ping(self, ctx):
        """Pings, I guess"""
        await ctx.send("epic fail")
        
    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        responses = [
            'nahhh', 'obviously lol', 'kinda', 'you think? helll naww', 
            'maybe a little bit', 'helll no', 'yeah I guess', 'awhhhh yeah',
            'no shit, sherlock', 'Your PintOS group says yes', 'I missed the part where I\'m obliged to answer',
            'you think you\'re a funny fellow?' 
        ]
        await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

    @commands.Cog.listener(name='on_message')
    async def send_dhruv_meme(self, message: Message):
        # meme message for dhruv
        if message.author.display_name == 'Dhruv':
            await Memes.probably_message(message.channel, random.choice(DHRUV_MEMES), "dhruv meme", self.dhruv_meme_threshold)
                

    @commands.Cog.listener(name='on_message')
    async def crab_react(self, message: Message):
        if message.author.id == self.bot.user.id:
            return
        
        crab_words = ['rust', 'rusty', 'rustling', 'rustacean']
        content = message.content.lower().split()
        if any(x in crab_words for x in content):
            await message.add_reaction("🦀")
            await Memes.probably_message(message.channel, "Fuck Python, I hate myself too", "crab message", 0.5)
            
    
    @commands.Cog.listener(name='on_message')
    async def fuck_react(self, message: Message):
        if message.author.id == self.bot.user.id:
            return

        words = ['fuck', 'tf', 'wtf']
        content = message.content.lower().split()
        if any(x in words for x in content):
            await Memes.probably_message(message.channel, f"nah <@{message.author.id}>, fuck you.", "fuck you message", 0.5)


    @commands.group(name='override', invoke_without_command=True)
    async def override_group(self, ctx):
        """Command group to override various internal meme state.
        """
        pass
    

    @override_group.command(name='dhruv_meme_threshold')
    async def override_dhruv_meme_threshold(self, ctx, new_threshold=None):
        if await Memes.is_dhruv(ctx): return
        if not await Memes.is_valid_threshold(ctx, new_threshold): return

        self.dhruv_meme_threshold = float(new_threshold)
        await ctx.send(f'New Dhruv meme threshold set to {new_threshold}')
        

    @commands.group(name='check',invoke_without_command=True)
    async def check_group(self, ctx):
        """Command group to check various internal meme state.
        """
        pass
    

    @check_group.command(name='dhruv_meme_threshold')
    async def check_dhruv_meme_threshold(self, ctx):
        if await Memes.is_dhruv(ctx): return
        await ctx.send(f'Current Dhruv meme threshold is {self.dhruv_meme_threshold}')
        

    @staticmethod
    async def is_dhruv(ctx):
        if ctx.message.author.display_name == "Dhruv":
            await ctx.send("lmaooo, you thought xD")
            return True
        else:
            return False
            

    @staticmethod
    async def is_valid_threshold(ctx, threshold):
        try:
            if not 0.00 <= float(threshold) <= 1.00:
                await ctx.send("send a value between 0 and 1, dumbass")
                return False        
        except:
            await ctx.send("enter a float, lmao noob")
            return False

        return True
            

    @staticmethod
    async def probably_message(channel, message, message_description, send_threshold=0.69):
        message_chance = random.random()
        print(f'chance of {message_description}: {message_chance}')
        if message_chance >= send_threshold:
            await channel.send(message)


# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(Memes(bot))