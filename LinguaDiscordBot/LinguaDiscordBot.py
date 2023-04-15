import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'LinguaConsoleBot')))

# Import Lingua functions from Lingua.py
from Lingua import get_language_code, get_ai_response, get_feedback, save_conversation_and_feedback

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create a new instance of the Intents class
intents = discord.Intents.all()
intents.members = True

# Create a new instance of the Bot class with the intents parameter
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='start', help='Start a conversation with Lingua')
async def start(ctx):
    await ctx.send("Hello! It is so nice to meet you! My name is Lingua, your language learning assistant. Please start speaking to me in your target learning language of choice. Use !speak before your message to talk with me, !feedback to get feedback on our conversation so far, and !start to start a new conversation after the current one ends.")

@bot.command(name='speak', help='Send a message to Lingua')
async def speak(ctx, *, message):
    user_text = message
    language_code = get_language_code(user_text)

    if language_code == "Unknown":
        await ctx.send("I'm sorry, but I currently do not understand this language enough to provide feedback in a respectful way.")
    else:
        conversation = [f"User: {user_text}"]
        ai_response = get_ai_response('\n'.join(conversation), language_code)
        conversation.append(f"AI: {ai_response}")
        await ctx.send(f"{ctx.author.mention}, {ai_response}")

@bot.command(name='feedback', help='Get feedback from Lingua')
async def feedback(ctx):
    channel = ctx.channel
    messages = await channel.history(limit=100).flatten()

    conversation = []
    for msg in reversed(messages):
        if msg.author == bot.user:
            conversation.append(f"AI: {msg.content}")
        elif msg.author == ctx.author:
            conversation.append(f"User: {msg.content}")

    language_code = get_language_code(conversation[-1].split(":", 1)[1].strip())
    feedback_text = get_feedback(conversation, language_code)

    await ctx.send(f"{ctx.author.mention}, here's your feedback:\n\n{feedback_text}")

bot.run(TOKEN)
