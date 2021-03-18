import discord
from discord.ext import commands
import nasapy
from datetime import datetime
import discordtoken from token
import nasatoken from token

client = commands.Bot(command_prefix='.')
token = discordtoken #this is where your bot token would go.

#
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.command()
# async def download():
     
@client.command()
async def nasa(message):
    channel = message.channel
    
    k = nasatoken

    # Creates object to store apikey
    nasa = nasapy.Nasa(key=k)

    # Gets today's date
    d = datetime.today().strftime('%Y-%m-%d')

    # requests to get image
    apod = nasa.picture_of_the_day(date=d, hd=True)

    url = 0

    if ("hdurl" in apod.keys()):
        url = apod["hdurl"]
            
    await channel.send(f'{url}')


    
client.run(token)

