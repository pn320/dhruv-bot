# suggestions.py
"""module to add suggestions to github repository based on messages send to #bot-suggestions channel"""
import os

from discord import Embed
from discord.ext import commands
from dotenv import load_dotenv
from github import Github

load_dotenv()
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', None)
OWNER_USERNAME = os.environ.get('OWNER_USERNAME', None)
PATH_TO_REPO = f'{OWNER_USERNAME}/dhruv-bot'


class SuggestionsCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name='suggestion')
    async def create_feature_req(self, ctx, *, arg):
        """retrieves feature request and creates github enhancement issue"""
        if ctx.channel.name != 'suggestions':
            return
        await ctx.send(f'Creating feature request in repository!')
        
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
            title=f'Request by {ctx.author.display_name}', 
            type='rich',
            description=arg, 
            color=0x00c09a
        )
        embed.set_author(
            name= f'DRP Bot Feature Request #{issue.number}',
            url=f'https://github.com/{OWNER_USERNAME}/dhruv-bot/issues/{issue.number}'  # type: ignore
        )
        embed.set_footer(text='Add to the issue by clicking the link in the title!')  # type: ignore
        await ctx.send(embed=embed) 
        

# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(SuggestionsCog(bot)) 
