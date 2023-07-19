import discord
from discord.ext import commands
import datetime
from general.stafflogs import stafflogs
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def kickcmd(ctx, member : discord.Member, *, reason=None):
    await usermessagedelete(ctx)
    await member.kick(reason=reason)
    embed = discord.Embed(title="Kick", description=f"{member} has been kicked", color=0x00ffff)
    embed.set_footer(text="Bot by ItzSimplyJoe")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    await ctx.send(embed=embed)
    await delete_message(ctx)
    await stafflogs.add_log(ctx.author, "Kick", member, datetime.datetime.now())