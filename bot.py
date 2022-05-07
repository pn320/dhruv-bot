# bot.py
import os
import random

from discord import Client, Guild, Intents, Message, utils

TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']


intents = Intents.all()
client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    guild: Guild | None = utils.find(
      lambda g: g.name == GUILD, client.guilds
    )
    assert guild
    print(f'{client.user} is connected to {guild.name}')


@client.event
async def on_member_join(member) -> None:
    await member.create_dm()
    await member.dm_channel.send(
        f'Hey there, {member.name}! Welcome to the DRP server!'
    )

@client.event
async def on_message(message: Message):
    print(f'{message.author.display_name}')
    if message.author == client.user:
        return

    # meme message for dhruv    
    if message.author.display_name == 'Dhruv':
        if random.random() >= 0.80:
            await message.channel.send(f'dhruv you can come out now, it\'s safe')
    

client.run(TOKEN)
