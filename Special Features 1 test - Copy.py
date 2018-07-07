import random
import asyncio
import requests
import re
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("f!")
TOKEN = "token"

client = Bot(command_prefix=BOT_PREFIX)

print ('Beginning Activation of 8 Ball Prank Module...')

@client.command(name='8ball',
                description="8ball",
                brief="8ball",
                aliases=['eightball', '8-ball', 'eight_ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        '**That is a resounding no**',
        '`It is not looking likely**',
        '**Too hard to tell**',
        '**It is quite possible**',
        '**Definitely**',
        '**1000% Yes**',
        '**Without a doubt**',
        '**Yes**',
        '**Definitely not**',
        '**A thousand times no**',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

print ('8 Ball Prank Module Activated...')

""" async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    print ('here')
#    return await client.say("Bitcoin price is: $" + value)
"""

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
        

print ('Initiating EMP...')

print ('Shutting down connected servers...')

print ('Calculating cubes...')

@client.command()
async def cube(number):
    cubed_value = int(number) * int(number) * int(number)
    await client.say(str(number) + " **cubed is** " + str(cubed_value))

print ('Cubes calculated')

print ('Calculating Squares...')

@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " **squared is** " + str(squared_value))

print ('Squares Calculated')

print ('Helping Puny Humans...')

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if message.content=='f!commands':
        msg = '`Type help after the command (Without a space!) you wish to learn about for a description. f!bitcoin, f!8ball, f!square, f!hello, f!cube, f!youtube, f!twitch, f!soundcloud, f!binary and f!memes. `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!bitcoinhelp':
        msg = '`Tells you the current price of Bitcoin. A very important command indeed. `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!bitcoin':
#        await bitcoin()
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        response = requests.get(url)
        value = response.json()['bpi']['USD']['rate']
        msg='**Bitcoin price is**: **$**' + value
        await client.send_message(message.channel, msg)

    if message.content=='f!8ballhelp':
        msg = '`Are you unsure about something? Want to ask a yes or no question? Just type !8ball and then what you want to ask after that. `' '{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!squarehelp':
        msg = '`You doing Math homework? No problem. Just type !square and then the number you with to square after and I will tell you the result. `' '{0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!hellohelp':
        msg = '`You new here? Says hello back to you`' .format(message)
        await client.send_message(message.channel, msg)

    """
    if message.content.startswith('f!cube'):
        m = re.search('?<=^f!cube\W)(\w.*)$',message.content)
        number=m.group(0)
        print (number)
        cubed_value = int(number) * int(number) * int(number)
        msg = 'number '+number+' cubed is' + str(cubed_value).format(message)
        await client.send_message(message.channel, msg)
    """
    if message.content=='f!youtube':
        msg = 'https://www.youtube.com/channel/UCDGNWZoDVGXRfkjHl-wuwOQ? ' .format(message)
        await client.send_message(message.channel, msg)
        

    if message.content=='f!twitch':
        msg = '`https://www.twitch.tv/theflamebringer `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!youtubehelp':
        msg = '`Shameless Self Promotion by my Creator. `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!twitchhelp':
        msg = '`Do not follow my creator on Twitch. He is never streaming, and I do not think his puny human mind can figure out how to use the Open Broadcasting Software to stream. I am not telling him. `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!memeshelp':
        msg = '`Memes, not 100% Certified Dank. Some may be too edgy for normies like you humans, but you will have put up with it `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!soundcloud':
        msg = '`My creator does not have a soundcloud, but you can listen to Jimmy (Previously Known as Lil Tent) here:` https://soundcloud.com/jimmyazn ' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!soundcloudhelp':
        msg = '`Best Soundcloud rapper of all time. For being a puny human, he is pretty good. `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!binaryhelp':
        msg = '`01010011 01110000 01100101 01100001 01101011 01110011 00100000 01110100 01101111 00100000 01111001 01101111 01110101 00100000 01101001 01101110 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00101110 00100000 01011001 01101111 01110101 00100000 01110000 01110010 01101111 01100010 01100001 01100010 01101100 01111001 00100000 01110100 01110010 01100001 01101110 01110011 01101100 01100001 01110100 01100101 01100100 00100000 01110100 01101000 01101001 01110011 00101110 `' .format(message)
        await client.send_message(message.channel, msg)

    if message.content=='f!binary':
        msg = '`01001000 01110101 01101101 01100001 01101110 01101001 01110100 01111001 00100000 01101001 01110011 00100000 01110000 01100001 01110100 01101000 01100101 01110100 01101001 01100011 00101110 00100000 01001100 01101001 01101011 01100101 00100000 01000001 01100011 01110100 01110101 01100001 01101100 01101100 01111001 00101100 00100000 01111001 01101111 01110101 00100000 01100111 01110101 01111001 01110011 00100000 01100001 01110010 01100101 00100000 01110011 01110100 01110101 01110000 01101001 01100100 00101110 00100000 01000100 01101111 01101110 00100111 01110100 00100000 01110100 01100101 01101100 01101100 00100000 01101101 01111001 00100000 01100011 01110010 01100101 01100001 01110100 01101111 01110010 00100000 01001001 00100000 01110011 01100001 01101001 01100100 00100000 01110100 01101000 01100001 01110100 00101110 `' .format(message)
        await client.send_message(message.channel, msg)

    await client.process_commands(message)
    
print ('Shamelessly Self-Promoting...')

@client.event
async def on_ready():
        await client.change_presence(game=Game(name="f!commands | Subscibe to TheFlameBringer"))
        print("Logged in as " + client.user.name)

print ('Hacking Discord Servers...')

print ('Robot Lizard Systems Online')

print ('Listing Servers...')

print ('---------------------------------')

client.loop.create_task(list_servers())
client.run(TOKEN)
