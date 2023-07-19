import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def helpcmd(ctx):
    await usermessagedelete(ctx)
    embed = discord.Embed(title="Help", description="These are some of the commands avaliable to you!", color=0x00ffff)
    embed.add_field(name="!Help", value="Shows this message", inline=False)
    embed.add_field(name="!Shelp", value="Shows staff commands", inline=False)
    embed.add_field(name="!Ip", value="Shows the server ip", inline=False)
    embed.add_field(name="!Store", value="Shows the store link", inline=False)
    embed.add_field(name="!Website", value="Shows the website link", inline=False)
    embed.add_field(name="!Rules", value="Shows the rules", inline=False)
    embed.add_field(name="!ticket", value="Creates a ticket", inline=False)
    embed.set_footer(text="Bot by ItzSimplyJoe")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    await ctx.send(embed=embed)
    await delete_message(ctx)
