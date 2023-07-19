import discord
from discord.ext import commands
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def ticketcmd(ctx):
    await usermessagedelete(ctx)
    channel = await ctx.guild.create_text_channel(f'{ctx.author.name}s-ticket')
    await channel.set_permissions(ctx.guild.default_role, read_messages=False)
    await channel.set_permissions(ctx.author, read_messages=True)
    await channel.set_permissions(ctx.guild.get_role(1130764272746635314), read_messages=True)
    embed = discord.Embed(title="Ticket", description="Please explain your issue", color=0x00ffff)
    embed.add_field(name="Note", value="You can close this ticket by using the command `!close`", inline=False)
    embed.add_field(name="Note", value="You can add another user with `!add @user`", inline=False)
    embed.add_field(name="Note", value="You can remove any added user with `!remove @user`", inline=False)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    embed.set_footer(text="Bot by ItzSimplyJoe")
    await channel.send(embed=embed)    
    embed = discord.Embed(title="Ticket", description=f"Your ticket has been created {channel.mention}", color=0x00ffff)
    embed.set_footer(text="Bot by ItzSimplyJoe")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
    await ctx.send(embed=embed)
    await delete_message(ctx)
    