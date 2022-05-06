# bot.py
import os

from discord import Client, Guild, Intents, utils
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = Intents.all()
client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    guild: Guild | None = utils.find(lambda g: g.name == GUILD, client.guilds)
    assert guild

    print(
        f'{client.user} is connected to the following server:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


client.run(TOKEN)
