# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord

# IMPORT THE OS MODULE.

import discord
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands
client = discord.Client()

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.command()
async def ping(ctx):
        await ctx.channel.send('pong')


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run('ODEyNjc3MTIwNTc1Nzk5Mjk4.YDEOjA.Y6HjkMF_rekDX6Ur01CwLxOznPY')