import discord
from discord.ext import commands
import asyncio

async def delete_message(ctx):
    try:
        await asyncio.sleep(10)
        await ctx.message.delete()
    except:
        pass