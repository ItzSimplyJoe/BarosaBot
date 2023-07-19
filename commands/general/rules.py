import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def rulescmd(ctx):
    await usermessagedelete(ctx)
    if ctx.channel.id == 1121896451509858336:
        embed = discord.Embed(title="General Rules", description="General Chat rules", color=0x00ffff)
        embed.add_field(name="Rule 1", value="Be nice", inline=False)
        embed.add_field(name="Rule 2", value="No spamming", inline=False)
        embed.add_field(name="Rule 3", value="No NSFW", inline=False)
        embed.add_field(name="Rule 4", value="No advertising", inline=False)
        embed.add_field(name="Rule 5", value="No racism", inline=False)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
        await ctx.send(embed=embed)
        await delete_message(ctx)
    elif ctx.channel.id == 1130622698884698224:
        embed = discord.Embed(title="Test Rules", description="Test rules", color=0x00ffff)
        embed.add_field(name="Rule 1", value="Gay", inline=False)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
        await ctx.send(embed=embed)
        await delete_message(ctx)