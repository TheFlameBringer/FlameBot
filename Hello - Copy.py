import discord

TOKEN = 'token'

client = discord.Client()

startup_extensions = ["Music"]

startup_extensions = ["Memes"]

startup_extensions = ["Speical Features 1 test"]

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content=='f!hello':
        msg = '**Hello! ** {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
