import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.typing = False  # Optionally disable the typing intent
intents.messages = True  # Add the messages intent

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    forbidden_words = ["kirat bhaiya", "kirat sir"]
    variations = ["baia", "bhaaiyaaa"]

    lower_content = message.content.lower()
    found_forbidden_word = False

    for word in forbidden_words:
        if word in lower_content:
            found_forbidden_word = True
            break

    if not found_forbidden_word:
        for word in variations:
            if word in lower_content:
                found_forbidden_word = True
                break

    if found_forbidden_word:
        try:
            scold_message = "Zindagi Me Kuch Accha karo meri Jaan, Bar Bar Bhaiya Bhaiya Mat Karo. Thank you!"
            await message.author.send(scold_message)
        except discord.Forbidden:
            print(f"Could not send DM to {message.author.name}: Missing permissions or blocked DMs")

    await bot.process_commands(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    # Handle other command errors here


@bot.event
async def on_disconnect():
    print("Bot disconnected from Discord")


bot.run("MTExNTY1NjEyOTgyMTgwNjYzMg.GIJfNr.tk2SoXE_czGortYzhQo1USVG2Pzn6kF13FKJSw")