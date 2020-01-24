import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Bot connected....')

# Очистка чата
@bot.command()
@commands.has_permissions( administrator = True)

async def clear(ctx,amount= 100):

    await ctx.channel.purge( limit = amount )
    channel = bot.get_channel(619655595837882437)
    await channel.send(embed = discord.Embed(description = f''f' Удалено ``{amount}`` сообщений''', color=0x0c0c0c))

#Kик из сервера

@bot.command(pass_conext= True)
@commands.has_permissions( administrator = True)

async def kick(ctx, member: discord.Member, *, reason= None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send(f'Выгнали { member. mention }')

#Бан
@bot.command(pass_conext= True)
@commands.has_permissions(administrator= True)

async def ban(ctx, member: discord.Member, *, reason= None):
    await ctx.channel.purge(limit = 1)
    await member.ban(reason = reason)
    await ctx.send(f'Улител в бан { member.mention }')

#Розбан
@bot.command(pass_conext= True)
@commands.has_permissions(administrator= True)

async def unban(ctx, *,member):
    await ctx.channel.purge(limit = 1)
    banned_user = ctx.guild.bans()

    for ban_entry in banned_user:
        user = ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send(f'Прилител из бан { user.mention }')
        
        return

#help

@bot.command(pass_conext= True)
@commands.has_permissions(administrator= True)

async def help(ctx):

    emb = discord.Embed(title= 'Навигация по командам: ')

    emb.add_field(name= '{}clear'.format(command_prefix), value= 'Очистка чата')
    emb.add_field(name= '{}kick'.format(command_prefix), value= 'Кик из сервера')
    emb.add_field(name= '{}ban'.format(command_prefix), value= 'Бан на сервере')
    emb.add_field(name= '{}unban'.format(command_prefix), value= 'Разбан на сервере')

    await ctx.send(embed= emb)



#Conect
bot.run('NjY5NTkxNTE2MDE2Mjc5NTky.Xii4IQ.7_EbqaM-jA81xpml7O08VkQ1lZc')