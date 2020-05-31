import datetime
import json
import time
from datetime import datetime

import pymongo
from pymongo import MongoClient
import discord
from discord.ext import commands

version = 1.2


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


private = getJSON('./private.json')

BotToken = private.get("BotToken")

dbpass = private.get("DbPass")

token = private.get("token")


def get_prefix(bot, message):
    prefixes = ["pink ", "pinkRPG ", '>']

    return commands.when_mentioned_or(*prefixes)(bot, message)


# test

cluster = MongoClient(dbpass)
db = cluster["discord"]

initial_extensions = [
    "cogs.help",
    "cogs.errorHandler",
    "cogs.important",
    "cogs.info",
    "cogs.shop",
    "cogs.casino",
    "cogs.staff",
    "cogs.attack"
]

bot = commands.Bot(command_prefix=get_prefix, description='yes', case_insensitive=True)
bot.remove_command("help")

for extension in initial_extensions:
    bot.load_extension(extension)

bot.load_extension("jishaku")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Ima be on soon ;)'))
    print(f'Y-you tu-urned mwe on successfully daddy uwu, im looking at')
    print(bot.cogs)
    print("Guilds im in:")
    print(len(bot.guilds))
    print("People im watching over:")
    print(len(bot.users))


bot.run(BotToken, bot=True, reconnect=True)
