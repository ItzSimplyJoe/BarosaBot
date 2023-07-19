import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete
async def applycmd(ctx):
    await usermessagedelete(ctx)
    channel = await ctx.guild.create_text_channel(f'{ctx.author.name}s-application')
    await channel.set_permissions(ctx.guild.default_role, read_messages=False)
    await channel.set_permissions(ctx.author, read_messages=True)
    await channel.set_permissions(ctx.guild.get_role(1130764272746635314), read_messages=True)
    embed = discord.Embed(title="Staff Application", description="Please answer the following questions", color=0x00ffff)
    embed.add_field(name="Note", value="You can close this application by using the command `!close`", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    embed.set_footer(text="Bot by ItzSimplyJoe")
    await channel.send(embed=embed)    
    embed = discord.Embed(title="Staff Application", description=f"Your application has been created {channel.mention}", color=0x00ffff)
    embed.set_footer(text="Bot by ItzSimplyJoe")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    await ctx.send(embed=embed)
