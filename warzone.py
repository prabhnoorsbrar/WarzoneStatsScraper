import requests
from bs4 import BeautifulSoup
import asyncio
import discord
from discord.ext import commands, tasks
from discord.utils import get
#  find the div tags with class="numbers" then look under them for a span tag with title="Wins" or "K/D Ratio" and then the next tag will be another span tag with class="value"
#https://cod.tracker.gg/warzone/profile/atvi/noor%237336996/overview(activison URL)
#https://cod.tracker.gg/warzone/profile/battlenet/noor209%231618/overview(battlenet URL)
#https://cod.tracker.gg/warzone/profile/psn/noor209/overview (psn url)
#https://cod.tracker.gg/warzone/profile/xbl/NOOR/overview (xbl url)
#<span data-v-01cb423e="" class="value">2.96</span> (element for kd value)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#client.run('NzYxMTExNzAyNTY4ODI4OTQ4.X3V2gg.Rcpe7-R0_MU4_IG2KUC5woQjhIE')




#make variables to create dynamic URL
stats=requests.get("https://cod.tracker.gg/warzone/profile/psn/noor209/overview")
print(stats)

soup=BeautifulSoup(stats.text, 'html.parser') 

Wins=soup.find("div",class_="numbers").find("span",title="Wins",class_="name")
Wins=soup.find("span",class_="value")
Wins=Wins.text
print(Wins)

#have to set a variable to the div and span tags for the K/D ratio aspect of the stats
ratio=soup.find("span",title="K/D Ratio",class_="name").find(class_="value")


print(ratio)

