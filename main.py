import discord
from discord.ext import commands
from setuptools import Command
from config import settings
import json
import requests
import urllib.request
import random

import googletrans
from googletrans import Translator

bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command()
async def hello(ctx):
    author = ctx.message.author    
    await ctx.send(f'Пошёл нахуй {author.mention}!')
    
@bot.command()    
async def sosi(ctx):
    author = ctx.message.author    
    await ctx.send(f'Как скажешь {author.mention}!')

@bot.command()
async def random_niger(ctx):
    value = random.randint(1,4)
    
    if value == 1:
        img = 'D:\\Bot\\img\\1.jpg'
        return await ctx.send(file=discord.File(img))
    if value == 2:
        img = 'D:\\Bot\\img\\2.jpg'
        return await ctx.send(file=discord.File(img))
    if value == 3:
        img = 'D:\\Bot\\img\\3.jpg'
        return await ctx.send(file=discord.File(img))
    if value == 4:
        img = 'D:\\Bot\\img\\4.jpg'
        return await ctx.send(file=discord.File(img))
    
@bot.command()
async def t(ctx, *, text):
    fraze = text
    translator = Translator()
    output = translator.translate(fraze)
    await ctx.send(output)
bot.run(settings['token'])    