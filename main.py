# bot.py
import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = ";")

extensions = [
    'app.trivia'
    ]

# Load and reload bot
def check_if_me(ctx):
    return ctx.message.author.id == 321484610821423116

@client.command()
@commands.check(check_if_me)
async def load(ctx, extension):
    try:
        client.load_extension(extension)
        await ctx.send(f'{extension} successfully loaded')
        print(f'{extension} successfully loaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be loaded. [{exception}]')
        print(f'{extension} cannot be loaded. [{exception}]')

@client.command()
@commands.check(check_if_me)
async def unload(ctx, extension):
    try:
        client.unload_extension(extension)
        await ctx.send(f'{extension} successfully unloaded')
        print(f'{extension} successfully unloaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be unloaded. [{exception}]')
        print(f'{extension} cannot be unloaded. [{exception}]')

@client.command()
@commands.check(check_if_me)
async def reload(ctx, extension):
    try:
        client.reload_extension(extension)
        await ctx.send(f'{extension} successfully reloaded')
        print(f'{extension} successfully reloaded')
    except Exception as exception:
        await ctx.send(f'{extension} cannot be reloaded. [{exception}]')
        print(f'{extension} cannot be reloaded. [{exception}]')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    game = discord.Game('Trivia Heist')
    await client.change_presence(activity = game)

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} fully loaded')
        except:
            print(f'{extension} failed to load')
    client.run(TOKEN)
