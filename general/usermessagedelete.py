import discord
from discord.ext import commands

async def usermessagedelete(ctx):
    await ctx.message.delete()