import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Pong!")
    async def ping(self, ctx):
      await ctx.send("Pong!")
    

  
