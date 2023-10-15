import discord
import random 
import os 
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix='/', intents = intents)


def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'Bot Hazır KAPTAN!!!{bot.user}')
    print(os.listdir('img'))
@bot.command()
async def mem(ctx):
    
    meme_rastgele = random.choice(os.listdir('img'))
    with open(f'img/{meme_rastgele}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(name='köpek')
async def dog(ctx):
   
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("<token>")
