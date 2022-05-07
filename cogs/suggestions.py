# suggestions.py
"""module to add suggestions to github repository based on messages send to #bot-suggestions channel"""
import os

from discord import  Embed
from discord.ext import commands
from dotenv import load_dotenv
from github import Github

load_dotenv()
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', None)
PATH_TO_REPO = f'{GITHUB_USERNAME}/dhruv-bot'


class SuggestionsCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name='suggestion')
    async def create_feature_req(self, ctx, *, arg):
        """retrieves feature request and passes it helper function"""
        if ctx.channel.name != 'bot-suggestions':
            return
        await ctx.send(f'Creating feature request for {arg} in repository')
        
        # this logic really needs to be separated into another function
        git_session = Github(GITHUB_TOKEN)
        repository = git_session.get_repo(PATH_TO_REPO)
        issue = repository.create_issue(
            title=arg,
            labels=[
                repository.get_label("enhancement")
            ]
        )
        
        assert issue.created_at is not None, f'could not create the issue'

        # also needs to be separated
        embed=Embed(
            title=f'Request #{issue.number}', 
            type='rich',
            description=arg, 
            color=0x00c09a
        )
        embed.set_author(
            name= 'DRP Bot Feature Request',
            url=f'https://github.com/{GITHUB_USERNAME}/dhruv-bot/issues/{issue.number}'  # type: ignore
        )
        embed.set_footer(text='Add to the issue by clicking the link in the title!')  # type: ignore
        print(embed)
        await ctx.send(embed=embed) 
        

# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(SuggestionsCog(bot)) 
