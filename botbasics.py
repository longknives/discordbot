import discord
from discord import member
from discord import guild
from discord.ext import commands
import random

from discord.ext.commands import bot



client = commands.Bot(command_prefix = '.')




@client.command()
async def kick(ctx, n : discord.Member):
    await n.kick()

@client.command()
async def ban(ctx, n : discord.Member):
    await n.ban()





@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split('#')


    for ban_entry in banned_users:
        user = ban_entry.user


        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            return

                


@client.command()
async def clear(ctx):
    await ctx.channel.purge(limit = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)







     


        


client.run('')

 

    
