import discord
from discord.ext import commands
import datetime
from general.stafflogs import stafflogs
from general.delete_message import delete_message
from general.usermessagedelete import usermessagedelete

async def unbancmd(ctx, *, member):
    await usermessagedelete(ctx)
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")
    for banned_entry in banned_users:
        user = banned_entry.user
        if(user.name, user.discriminator) == (member_name, member_disc):
            await ctx.guild.unban(user)
            embed = discord.Embed(title="Unban", description=f"{user.mention} has been unbanned", color=0x00ffff)
            embed.set_footer(text="Bot by ItzSimplyJoe")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/961724055881400420/1122649367875170386/DreamShaper_v5_Animated_minecraft_sword_on_shield_logo_1-removebg-preview.png")
            await ctx.send(embed=embed)
            await delete_message(ctx)
            await stafflogs.add_log(ctx.author, "Unban", member, datetime.datetime.now())
            return