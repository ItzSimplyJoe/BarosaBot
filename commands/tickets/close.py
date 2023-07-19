import discord
from discord.ext import commands
import os
from general.usermessagedelete import usermessagedelete

async def closecmd(ctx):
    await usermessagedelete(ctx)
    if ctx.channel.name.endswith("ticket") or ctx.channel.name.endswith("application"):
        with open(f"{ctx.channel.name}.txt", "w+") as f:
            async for message in ctx.channel.history(limit=1000000):
                f.write(f"{message.author.name}#{message.author.discriminator}: {message.content}\n")
        await ctx.channel.delete()
        embed = discord.Embed(title="Ticket", description="Your ticket has been closed", color=0x00ffff)
        embed.set_footer(text="Bot by ItzSimplyJoe")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
        await ctx.author.send(embed=embed)
        await ctx.author.send(file=discord.File(f"{ctx.channel.name}.txt"))
        os.remove(f"{ctx.channel.name}.txt")
    else:
        await ctx.send("You cannot use this command in this channel")