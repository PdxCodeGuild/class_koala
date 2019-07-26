#sadGeb.py
import discord
import random
import datetime

TOKEN = "NjA0MDkxMzcwNDkxMDg0ODAw.XTstNA.A51TwVTCpFtZGlE3ibWB0CVBYXY"

client = discord.Client()

#replies = ["Give Khepri a gun","They don't think it be like it is, but it do", "Sobek is a lizard", "What are you gonna do, kill me?", "Did you know that Petey is gay?"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send(f"Hello {message.author.mention}")

    #if message.content.startswith('sad'):
    #    await message.channel.send(random.choice(replies))

    if message.content.startswith('!remind'):
        try:
            info = message.content.split(' ')
            currentDate = datetime.datetime.now()
            remindDate = datetime.datetime.strptime(info[1], '%m/%d/%Y')
            time = info[2].split(':')
            remindDate = remindDate.replace(hour=int(time[0]), minute=int(time[1]))
            await message.channel.send(f"I will remind you on {remindDate}")
            msg = ''
            i = 3
            while i < len(info):
                msg += info[i]
                msg+= ' '
                i += 1
            message.content = msg
            while remindDate > currentDate:
                currentDate = datetime.datetime.now()
            await message.channel.send(message.content)
        except:
            await message.channel.send("Something went wrong. Make sure you format your request correctly")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
