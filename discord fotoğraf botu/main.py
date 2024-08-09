import discord
from discord.ext import commands
import os,random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def mem1(ctx ):
    with open("william afton/mem1.png", "rb") as a:
        funny = discord.File(a)
    await ctx.send(file = funny)

@bot.command()
async def mem2(ctx ):
    with open("william afton/mem2.png", "rb") as a:
        funny = discord.File(a)
    await ctx.send(file = funny)

@bot.command()
async def mem3(ctx ):
    with open("william afton/mem3.png", "rb") as a:
        funny = discord.File(a)
    await ctx.send(file = funny)


@bot.command()
async def mem4(ctx ):
    with open("william afton/mem4.png", "rb") as a:
        funny = discord.File(a)
    await ctx.send(file = funny)

bot.run("YOUR_TOKEN_HERE")