import discord
from discord.ext import commands
import os
import json
from commands.general.ip import ipcmd
from commands.general.store import storecmd
from commands.general.site import websitecmd
from commands.general.staffhelp import shelpcmd
from commands.general.help import helpcmd
from commands.general.rules import rulescmd
from commands.staff.clear import clearcmd
from commands.staff.kick import kickcmd
from commands.staff.ban import bancmd
from commands.staff.unban import unbancmd
from commands.tickets.ticketcreation import ticketcmd
from commands.tickets.close import closecmd
from commands.tickets.add import addcmd
from commands.tickets.remove import removecmd
from commands.tickets.staffapplication import applycmd


config = json.load(open('config.json', 'r'))

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=config['prefix'], intents=intents, help_command=None)
################################################### Events ###################################################

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(813021075667249152)
    embed = discord.Embed(title=f'{member} joined!', description=f'Welcome to the server!', color=0x00ffff)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(813021075667249152)
    embed = discord.Embed(title=f'{member} left!', description=f'Goodbye!', color=0x00ffff)
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

################################################### Command Creation ###################################################
@bot.command()
async def help(ctx):
    await helpcmd(ctx)
@bot.command()
async def shelp(ctx):
    await shelpcmd(ctx)
@bot.command()
async def ip(ctx):
    await ipcmd(ctx)
@bot.command()
async def store(ctx):
    await storecmd(ctx)
@bot.command()
async def website(ctx):
    await websitecmd(ctx)
@bot.command()
async def rules(ctx):
    await rulescmd(ctx)
@bot.command()
async def clear(ctx,amount=5 ):
    await clearcmd(ctx, amount)
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await kickcmd(ctx, member, reason)
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await bancmd(ctx, member, reason)
@bot.command()
async def unban(ctx, *, member):
    await unbancmd(ctx, member)
@bot.command()
async def ticket(ctx):
    await ticketcmd(ctx)
@bot.command()
async def close(ctx):
    await closecmd(ctx)
@bot.command()
async def add(ctx, member : discord.Member):
    await addcmd(ctx, member)
@bot.command()
async def remove(ctx, member : discord.Member):
    await removecmd(ctx, member)
@bot.command()
async def apply(ctx):
    await applycmd(ctx)

################################################### Error Handling ###################################################
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Error", description="Command not found", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="Error", description="You do not have permission to use this command", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title="Error", description="Please specify all required arguments", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(title="Error", description="Please specify all required arguments", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title="Error", description="This command is on cooldown", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", description=f"{error}", color=0xff0000)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
################################################### Run ###################################################
bot.run(config['token'])
