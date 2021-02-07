import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import csv

bot = commands.Bot(command_prefix='!')
lista = []
with open('C:/Users/Manu/Documents/cursos/disc_bot/src/form_Prueba.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    lista = list(reader)


@bot.command()
async def saludo(ctx):
    await ctx.send('Funcionando')


@bot.command()
async def usuario(ctx, email):
    await ctx.channel.purge(limit=1)
    if email == ' ':
        await ctx.send('Tienes que poner algo')
    else:
        for usuario_registrado in lista:
            if usuario_registrado[2] == email:
                await ctx.send('Encontrado')
                await ctx.send('Hola '+ usuario_registrado[0] +'. Su cargo es: '+ usuario_registrado[4])
                if usuario_registrado[4] != 'TestR':
                    role = discord.utils.get(email.server.roles, name= 'TestR')
                    await ctx.add_roles(email, role)
                    break
                elif usuario_registrado[4] == 'TestR':
                    await ctx.remove_roles(email, role)
                    break
                break
            elif usuario_registrado == usuario_registrado[:-1] and usuario_registrado[2] != email:
                await ctx.send('No encontrado')
                break
    await ctx.send('Recibido')



@bot.event
async def on_ready():
    print('READY!')

bot.run('TOKEN')
