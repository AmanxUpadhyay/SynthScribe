import discord
from discord.ext import commands
import asyncio
import re

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

forbiddenWords = [
        'Kirat Bhai',
        'Kirat bhai',
        'Kirat Bhaiya',
        'Kirat bhaiya',
        'Kirat Bhaiya',
        'Kirat sir',
        'Kirat Baia',
        'Kirat bhaaiyaa',
        'Kirat bhaaiya',
        'Kirat bhaaiyaa'
    ]
pattern = re.compile(r'\b(?:%s)\b' % '|'.join(map(re.escape, forbiddenWords)), re.IGNORECASE)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if re.search(pattern, message.content):
        await message.author.send(f"Zindagi me Kuch accha karo meri jaan, ye {message.content} mat karo.")

    await bot.process_commands(message)

@bot.event
async def on_error(event, *args, **kwargs):
    print(f'Error in event {event}: {args[0]}')

@bot.event
async def on_disconnect():
    print('Disconnected from Discord!')

bot.run('TOKEN')
