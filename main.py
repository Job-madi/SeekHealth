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

songplayer = 'https://www.youtube.com/watch?v=eWLVBP3VrO4'


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
async def play(ctx):
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
        ydl.download([songplayer])
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


"""@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content
    now = datetime.now()
    current_time1 = now.strftime("%H:%M:%S")
    current_time2 = now.strftime("%H:%M:%S")

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if message.content.startswith('seekhealth'):
        await message.channel.send(
            "Here is a list of commands you can use for this bot\n\n!bmi - to calculate you body mass index and tell if its in the acceptable range or not\n\n!diet - to tell you how much should be your daily calorie intake according to your needs\n\n!meditate - to let you meditate and calculate the duration for which you meditated\n  !startmeditation - start meditation\n  !stopmeditation - stop meditation and see the duration for which you meditated\n\n!playmusic - play a playlist to according to your choice for either meditation, yoga or workout\n  !meditationmusic - play music playlist best suitable for meditation\n  !workoutmusic - play music playlist best suitable for workout\n  !yogamusic - play music playlist best suitable for yoga")

    elif message.content.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    elif message.content.startswith('!hello'):
        await message.channel.send("Hey")

    elif message.content.startswith('!bmi'):
        {
            await message.channel.send("Now I'll calculate your bmi.")
        }
    elif message.content.startswith('!diet'):
        {
            await message.channel.send("Let me know few things and I'll tell you how much should you eat in a day")
        }

    elif message.content.startswith('!meditate'):
        {
            await message.channel.send(
                "use command '!startmeditation' and start meditating. When you're done, use command '!stopmeditation' to see how long did you meditate :)")
        }
    elif message.content.startswith('!startmeditation'):
        {

            await message.channel.send("current time:" + current_time1 + " \ngoodluck with your meditation")
        }

    elif message.content.startswith('!stopmeditation'):
        {

            await message.channel.send(
                "current time:" + current_time2 + " \nyou meditated for a total of " + "*gotta include time difference here*")
        }

    elif message.content.startswith('!playmusic'):
        {
            await message.channel.send(
                "'!musicmeditation' - meditative music playlist\n'!musicworkout' - workout music playlist")
        }

    elif message.content.startswith('!facts'):
        {

        }

        await bot.process_commands(message)"""

#Todo: add other commands
@bot.command(
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    brief="Prints pong back to the channel."
)
async def ping(ctx):
    await ctx.channel.send("pong")


# client.run("ODEyNjc3MTIwNTc1Nzk5Mjk4.YDEOjA.Y6HjkMF_rekDX6Ur01CwLxOznPY")
bot.run("")
