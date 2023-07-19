import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def shelpcmd(ctx):
    await usermessagedelete(ctx)
    embed = discord.Embed(title="Staff Help", description="Staff Help", color=0x00ffff)
    embed.add_field(name="!sHelp", value="Shows this message", inline=False)
    embed.add_field(name="!clear {amount}", value="Clears messages", inline=False)
    embed.add_field(name="!kick {user}", value="Kicks a user", inline=False)
    embed.add_field(name="!ban {user}", value="Bans a user", inline=False)
    embed.add_field(name="!unban {user}", value="Unbans a user", inline=False)
    embed.set_footer(text="Bot by ItzSimplyJoe")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    await ctx.send(embed=embed)
    await delete_message(ctx)