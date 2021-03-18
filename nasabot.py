import discord
from discord.ext import commands
import nasapy
from datetime import datetime

client = commands.Bot(command_prefix='.')
token = 'ODIyMTc5MDgzMDg1NDE0NDAw.YFOf8A.Tm2_hJX14h9OG4EGXDAkfsg2Zx8' #this is where your bot token would go.

#
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client.command()
# async def download():
     
@client.command()
async def nasa(message):
    channel = message.channel
    
    k = 'mduhkZOlZ6f0zlTFRuAffqbfJ3wYICBcc6M9VKes'

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

