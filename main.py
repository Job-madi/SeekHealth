import discord
import requests
import json
import random
import youtube_dl
import os
from datetime import datetime
from discord.ext import commands
from data import *
from methods import *

bot = commands.Bot(command_prefix='$')
from discord.ext.commands import Bot

songplayer = 'https://www.youtube.com/watch?v=VIrOfWLYqKI'
songplayerex = 'https://www.youtube.com/watch?v=-Gel0z3lJms'
songplayeryo = 'https://www.youtube.com/watch?v=VIrOfWLYqKI'
songplayermed = 'https://www.youtube.com/watch?v=cI4ryatVkKw'


@bot.command()
async def facts(ctx):
    fact = findfacts()
    await ctx.channel.send(f'>> {fact} <<')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('its woking hombre')


@bot.command()
async def quotes(ctx):
    quote = getQuotes()
    await ctx.channel.send(f'>> {quote} <<')


@bot.command()
async def playmeditation(ctx):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('Wait for the current playing musisc to end or use the Stop command')
        return

    # lets bot join the channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([songplayermed])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def playexercise(ctx):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('Wait for the current playing musisc to end or use the Stop command')
        return

    # lets bot join the channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([songplayerex])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

@bot.command()
async def playyoga(ctx):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
    except PermissionError:
        await ctx.send('Wait for the current playing musisc to end or use the Stop command')
        return

    # lets bot join the channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([songplayeryo])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.channel.send("No bot is connected my dude!")


@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.channel.send('Nothing is playing')


@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.channel.send('Audio is playing')


@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


@bot.command()
async def bmi(ctx, weight: float, height: float):
    rBmi = getBmi(weight, height)
    await ctx.send(rBmi)

@bot.command()
async def meditate(ctx):
    await ctx.channel.send("use command '$startmeditation' and start meditating. When you're done, use command '$stopmeditation' to see how long did you meditate :)")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content
    now = datetime.now()
    current_time1 = now.strftime("%H:%M:%S")
    current_time2 = now.strftime("%H:%M:%S")

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


    elif message.content.startswith('$startmeditation'):
        {

            await message.channel.send("current time:" + current_time1 + " \ngoodluck with your meditation")
        }

    elif message.content.startswith('$stopmeditation'):
        {

            await message.channel.send("current time:" + current_time2)
        }




    await bot.process_commands(message)

#Todo: add other commands
@bot.command(
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel."
)
async def ping(ctx):
    await ctx.channel.send("pong")


# client.run("ODEyNjc3MTIwNTc1Nzk5Mjk4.YDEOjA.Y6HjkMF_rekDX6Ur01CwLxOznPY")
bot.run("ODEyNjc3MTIwNTc1Nzk5Mjk4.YDEOjA.lS5QoXWn40lBy5KOgruwFRIqwkQ")