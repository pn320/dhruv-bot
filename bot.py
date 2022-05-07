# bot.py
import os

from discord import Client, Guild, Intents, utils, Message


TOKEN = os.environ['TOKEN']
GUILD = os.environ['GUILD']
DHRUV_ID = os.environ['DHRUV_ID']

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
    if message.author == client.user:
        return

    print(f'the author is {message.author}')

    if message.author.id == DHRUV_ID:
        await message.channel.send(f'dhruv you\'re super gay.')
    else:
        await message.channel.send(f'you\'re not dhruv.')

client.run(TOKEN)