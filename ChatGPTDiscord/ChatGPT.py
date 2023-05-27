import openai
import discord
from discord.ext import commands

# Initialize ChatGPT
API_KEY = open('API_KEY', 'r').read().strip()
openai.api_key = API_KEY

log = []

def getResponse(message):
    log.append({"role": "user", "content": message})
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=log
        )

        reply = response['choices'][0]['message']['content']
        return reply

    except Exception as e:
        print(f"Error in getResponse function: {e}")
        return "An error occurred while processing the message."

# Initialize Discord bot

DISCORD_TOKEN = open('DISCORD_TOKEN', 'r').read().strip()

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is logged on as {bot.user.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$chatgpt'):
        msg = message.content[8:]
        reply = getResponse(msg)
        await message.channel.send(reply)

    await bot.process_commands(message)

bot.run(DISCORD_TOKEN)