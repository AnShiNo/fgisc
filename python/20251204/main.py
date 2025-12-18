#把需要的Library匯入
import discord
import asyncio
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

#權限打開
load_dotenv()
token = os.getenv("TOKEN")

# Feature flag: Enable Claude Haiku 4.5 for all clients
enable_claude_haiku_4_5 = os.getenv("ENABLE_CLAUDE_HAIKU_4_5", "false").strip().lower() in ("1", "true", "yes")
bot_enable_msg = f"Enable Claude Haiku 4.5: {enable_claude_haiku_4_5}"
print(bot_enable_msg)

intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

#load cogs 資料夾裡面的東西，然後 log in
async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
#跑一個迴圈把 cogs 資料夾裡面的 .py 都抓出來，然後變成 cogs

@bot.command()
async def sync(ctx):
    bot.tree.copy_gllobal_to(guild = ctx.guild)
    synced = await bot.tree.symc(guild = ctx.guild)
    await ctx.send("synced")

@bot.event
async def on_ready():
    print(f"{bot.user} logged in!")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())



#async 是什麼？
#asynchronous (非同步）就是讓 discord 在等待連線時，可以先去做別的事
#@bot.event
#async def on_ready():
    #print(f'We have logged in as {bot.user}')

#event 是什麼？
#就是事件，有很多種不同的event 可以用
#關鍵字偵測
#@bot.event
#async def on_message(message):
    #if message.author.bot:
        #return

    #if "小蝸牛" in message.content.lower() and "咕嚕咕嚕" in message.content.lower():
        #await message.channel.send(f"哈囉 {message.author.display_name}!")
        
    #await bot.process_commands(message)

#讓bot跑
#bot.run(token)