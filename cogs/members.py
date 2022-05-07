# members.py
"""Module to manage members of the discord server"""

from discord import Member
from discord.ext import commands


class MembersCog(commands.Cog):
    """Manages server members on the discord channel"""
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: Member):
        """Says when a member joined."""
        await ctx.send(f'{member.display_name} joined on {member.joined_at}')
    
    @commands.Cog.listener()
    async def on_member_join(self, member) -> None:
        """Sends a personal message on joining the server."""
        await member.create_dm()
        await member.dm_channel.send(
            f'Hey there, {member.name}! Welcome to the DRP server!'
        )
    
# Register the cog for our bot
def setup(bot: commands.Bot):
    bot.add_cog(MembersCog(bot)) 
