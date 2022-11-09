import os
from dotenv import load_dotenv

import discord
import logging
from discord.ext import commands as cmd

import datetime, time

class Basic(cmd.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @cmd.Cog.listener()
    async def on_ready(self):
        print(f'{self} has been loaded') 
        global startTime 
        startTime = time.time()

    @cmd.command()
    async def ping(self, interaction: discord.Interaction):
        server = interaction.guild
        await interaction.send("Ping statistics for server: {} \n"
        "Ping: {}ms".format(server, round(self.bot.latency * 1000)))

    @cmd.command()
    async def uptime(self, interaction: discord.Interaction):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        await interaction.send(uptime)

    @cmd.command()
    async def help(self, interaction: discord.Interaction):
        await interaction.send("```Witaj! \n"
        "Komendy: \n"
        "<ping - sprawdź ping \n"
        "<help - pomoc```")

async def setup(bot):
    await bot.add_cog(Basic(bot))
