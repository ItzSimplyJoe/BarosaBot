import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def addcmd(ctx, member : discord.Member):
    await usermessagedelete(ctx)
    if ctx.channel.name.endswith("ticket"):
        await ctx.channel.set_permissions(member, read_messages=True)
        embed = discord.Embed(title="Ticket", description=f"{member.mention} has been added to the ticket", color=0x00ffff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
        embed.set_footer(text="Bot by ItzSimplyJoe")
        await ctx.send(embed=embed)
        await delete_message(ctx)
    else:
        await ctx.send("You can only use this command in a ticket channel")