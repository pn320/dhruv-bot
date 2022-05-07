# suggestions.py
"""module to add suggestions to github repository based on messages send to #bot-suggestions channel"""

from discord.ext import commands


class SuggestionsCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name='suggestion')
    async def create_feature_req(self, ctx, *, arg):
        """retrieves feature request and passes it helper function"""
        await ctx.send("adding suggestion to repository")
        print(f'arg is {arg}, and type of argument is {type(arg)}')
        SuggestionsCog._create_feature_req(arg)
    
    @staticmethod
    def _create_feature_req(arg: str):
        print(f'connecting to github api')

# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(SuggestionsCog(bot)) 
