import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "魚魚" in message.content.lower() and "咕嚕咕嚕" in message.content.lower():
        await message.channel.send(f"哈囉 {message.author.display_name}!")
        
    await bot.process_commands(message)
    
bot.run(token)