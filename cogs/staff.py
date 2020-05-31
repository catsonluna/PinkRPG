import datetime

import discord.utils

from discord.ext import commands

from bot import bot, db

uinfo = db["uinfo"]


class PrivateCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, channel_id: int, *, message: str):
        user = uinfo.find_one({'User id': f'{ctx.author.id}'})
        if user["Titles"]['Owner'] == 1:
            channel = bot.get_channel(channel_id)
            await channel.send(message)

    @commands.command()
    async def sayhere(self, ctx, *, message: str):
        user = uinfo.find_one({'User id': f'{ctx.author.id}'})
        if user["Titles"]['Owner'] == 1:
            await ctx.send(message)
            await ctx.message.delete()
        else:
            await ctx.send("Uuw")

    @commands.command()
    async def dmsend(self, ctx, user_id: int, *, message: str):
        user = uinfo.find_one({'User id': f'{ctx.author.id}'})
        if user["Titles"]['Owner'] == 1 or user["Titles"]['Admin'] == 1:
            member = bot.get_user(user_id)
            channel = await member.create_dm()
            channel2 = bot.get_channel(698635545408045087)
            color = ctx.author.color
            embed = discord.Embed(title=f'Dm from PinkBot', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Name of the receiver:", value=f"{member}")
            embed.add_field(name="Message:", value=f"{message}", inline=False)
            embed.add_field(name="Note:",
                            value="If you want to send us a message please use >dm your message here(only works in dms), abuse of this or any other features can get you banned from doing commands in the future",
                            inline=False)
            await channel.send(embed=embed)
            await channel2.send(embed=embed)


def setup(bot):
    bot.add_cog(PrivateCommands(bot))
