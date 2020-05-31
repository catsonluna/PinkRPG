import datetime
import random

import discord
from discord.ext import commands

from bot import db

attack = db["attack"]

ginfo = db["ginfo"]

uinfo = db["uinfo"]


class Duel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, ctx, arg1: int = None, arg2: int = None):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user:
            if arg1 is None:
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Error:", value="Please choose a number from 1-6")
                await ctx.send(embed=embed)
            elif arg2 is None:
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Error:", value="Please choose the amount of coins you want to bet.")
                await ctx.send(embed=embed)
            else:
                user = uinfo.find_one({"User id": f"{ctx.author.id}"})
                if arg1 > 6:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="You can only choose numbers from 1-6.")
                    await ctx.send(embed=embed)
                elif arg2 < 50:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="You must bet 50 coins or more.")
                    await ctx.send(embed=embed)
                else:
                    if user["Pink coins"] < arg2:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="You dont have enough coins.")
                        await ctx.send(embed=embed)
                    else:
                        number = random.randint(1, 6)
                        if arg1 == number:
                            color = ctx.author.color
                            embed = discord.Embed(title=f'Dice game', colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="Your number:", value=f"{arg1}", inline=False)
                            embed.add_field(name="Dice number", value=number, inline=False)
                            embed.add_field(name="You won:", value=f"{arg2} Coins", inline=False)
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + arg2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + arg2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Casino games played": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Casino games won": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Dice games played": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Dice games won": +1}})

                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games won": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Dice games won": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Dice games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Lifetime coins": + arg2}})

                            await ctx.send(embed=embed)
                        else:
                            color = ctx.author.color
                            embed = discord.Embed(title=f'Dice game', colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="Your number:", value=f"{arg1}", inline=False)
                            embed.add_field(name="Dice number", value=number, inline=False)
                            embed.add_field(name="You lost:", value=f"{arg2} Coins", inline=False)
                            uinfo.update_one({'User id': f'{ctx.author.id}'}, {"$inc": {'Pink coins': - arg2}})
                            uinfo.update_one({'User id': f'{ctx.author.id}'}, {"$inc": {'Stats.Coins used': + arg2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Casino games lost": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Dice games lost": +1}})

                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games lost": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Dice games lost": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": + arg2}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Dice games played": +1}})

                            await ctx.send(embed=embed)
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="Please do >register to do this command.")
            await ctx.send(embed=embed)

    @commands.command(name="coinFlip", aliases=["flip", "coin"])
    async def coinFlip(self, ctx, arg1: str = None, arg2: int = None):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user:
            if arg1 is None:
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Error:", value="Please choose heads or tails.")
                await ctx.send(embed=embed)
            elif arg2 is None:
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Error:", value="Please choose the amount of coins you want to bet.")
                await ctx.send(embed=embed)
            else:
                user = uinfo.find_one({"User id": f"{ctx.author.id}"})
                if user["Pink coins"] < arg2:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="You dont have enough coins.")
                    await ctx.send(embed=embed)
                    await ctx.send("You dont have enough coins")
                elif arg2 < 100:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="You must bet 100 coins or more.")
                    await ctx.send(embed=embed)
                else:
                    if arg1 == "Tails":
                        arg1 = "tails"
                    if arg1 == "Heads":
                        arg1 = "heads"
                    if arg1 == "Tails":
                        arg1 = "tails"
                    if arg1 == "Heads":
                        arg1 = "heads"

                    if arg1 == "Tail":
                        arg1 = "tails"
                    if arg1 == "Head":
                        arg1 = "heads"
                    if arg1 == "tail":
                        arg1 = "tails"
                    if arg1 == "head":
                        arg1 = "heads"
                    choices = ('heads', 'tails')
                    coin = random.choice(choices)
                    if arg1 == "tails" or arg1 == "heads":
                        if arg1 == coin:
                            color = ctx.author.color
                            embed = discord.Embed(title=f'CoinFlip game', colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="You picked:", value=f"{arg1}", inline=False)
                            embed.add_field(name="Coin:", value=coin, inline=False)
                            embed.add_field(name="You won:", value=f"{arg2 / 2} Coins", inline=False)
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + arg2 / 2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + arg2 / 2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Casino games played": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Casino games won": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coin games won": +1}})

                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games won": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coin games won": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coin games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Lifetime coins": + arg2 / 2}})

                            await ctx.send(embed=embed)
                        else:
                            color = ctx.author.color
                            embed = discord.Embed(title=f'CoinFlip game', colour=color,
                                                  timestamp=datetime.datetime.utcnow())
                            embed.add_field(name="You Picked:", value=f"{arg1}", inline=False)
                            embed.add_field(name="Coin", value=coin, inline=False)
                            embed.add_field(name="You lost:", value=f"{arg2} Coins", inline=False)
                            uinfo.update_one({'User id': f'{ctx.author.id}'}, {"$inc": {'Pink coins': - arg2}})
                            uinfo.update_one({'User id': f'{ctx.author.id}'}, {"$inc": {'Stats.Coins used': + arg2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Casino games played": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Casino games lost": +1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coin games lost": +1}})

                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games played": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Casino games lost": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coin games lost": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": + arg2}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"Coin games played": +1}})

                            await ctx.send(embed=embed)
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="Not a valid choice, please choose either heads or tails.")
                        await ctx.send(embed=embed)
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="Please do >register to do this command.")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Duel(bot))
