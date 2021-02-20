import discord
import os
import requests
import json
import random
from datetime import datetime

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
a=0
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    

  if message.author == client.user:
    return

  msg = message.content
  now = datetime.now()
  current_time1 = now.strftime("%H:%M:%S")
  current_time2 = now.strftime("%H:%M:%S")
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))
  
  if message.content.startswith('seekhealth'):
      await message.channel.send("Here is a list of commands you can use for this bot\n\n!bmi - to calculate you body mass index and tell if its in the acceptable range or not\n\n!diet - to tell you how much should be your daily calorie intake according to your needs\n\n!meditate - to let you meditate and calculate the duration for which you meditated\n  !startmeditation - start meditation\n  !stopmeditation - stop meditation and see the duration for which you meditated\n\n!playmusic - play a playlist to according to your choice for either meditation, yoga or workout\n  !meditationmusic - play music playlist best suitable for meditation\n  !workoutmusic - play music playlist best suitable for workout\n  !yogamusic - play music playlist best suitable for yoga")

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
          await message.channel.send("use command '!startmeditation' and start meditating. When you're done, use command '!stopmeditation' to see how long did you meditate :)")
      }
  elif message.content.startswith('!startmeditation'):
      {
        
        await message.channel.send("current time:" + current_time1 + " \ngoodluck with your meditation")
      }

  elif message.content.startswith('!stopmeditation'):
      {
        
        await message.channel.send("current time:" + current_time2 + " \nyou meditated for a total of " + "*gotta include time difference here*")
      }
  
  elif message.content.startswith('!playmusic'):
      {
        await message.channel.send("'!musicmeditation' - meditative music playlist\n'!musicworkout' - workout music playlist")
      }

  elif message.content.startswith('!facts'):
      {
        
      }

client.run("ODEyNjc3MTIwNTc1Nzk5Mjk4.YDEOjA.3RYIoJbyoTLTnyqVMMf-_nsOhEQ")