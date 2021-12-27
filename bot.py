import json 

import discord
from discord.ext import commands

# Token読み込み
json_open = open("Token.json", "r")
json_load = json.load(json_open)
TOKEN = json_load["Token"]

bot = commands.Bot(command_prefix="?")

# 起動時メッセージ
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}(ID:{bot.user.id})")
    print("=====")


bot.run(TOKEN)