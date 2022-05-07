# bot.py
import os

from discord import Guild, Intents, utils
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']
COMMAND_PREFIX = '.'


intents = Intents.all()
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

@bot.event
async def on_ready() -> None:
    guild: Guild | None = utils.find(
      lambda g: g.name == GUILD, bot.guilds
    )
    assert guild
    print(f'{bot.user} is connected to {guild.name}')


@bot.event
async def on_member_join(member) -> None:
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey there, {member.name}! Welcome to the DRP server!'
    )

# Below cogs represents our folder our cogs are in. Following is the file name. So 'meme.py' in cogs, would be cogs.meme
# Think of it like a dot path import
initial_extensions = ['cogs.memes', 'cogs.suggestions']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True)
