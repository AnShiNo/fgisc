import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
# 中間塞主程式
        
async def setup(bot):
    await bot.add_cog(Moderation(bot))