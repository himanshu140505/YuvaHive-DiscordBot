import discord

# Read the API key from private.txt
with open('private.txt', 'r') as f:
    line = f.readline()
    api_key = line.split('=')[1].strip().strip("'")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'hello':
        await message.channel.send('Hello! I am online.')

client.run(api_key)