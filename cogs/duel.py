import asyncio

import discord
from discord.ext import commands

from bot import db

attack = db["attack"]

ginfo = db["ginfo"]

uinfo = db["uinfo"]

duelinv = db["duelinv"]

duelfight = db["duelfight"]


class Duel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx, member: discord.Member = None, arg2: int = None):
        if member is None:
            await ctx.send("Please specify who you would like to duel")
        else:
            user1 = duelinv.find_one({"User1 id": f"{ctx.author.id}"})
            user2 = duelinv.find_one({"User2 id": f"{member.id}"})
            user1Info = uinfo.find_one({"User id": f"{ctx.author.id}"})
            user2Info = uinfo.find_one({"User id": f"{member.id}"})
            if user1:
                await ctx.send("You already challenged someone")
            elif user2:
                await ctx.send("User has already been challenged")
            if user1Info == user2Info:
                await ctx.send("you cant invite yourself silly")
            else:
                if not user1Info:
                    await ctx.send("You must >register to use this command")
                elif not user2Info:
                    await ctx.send(f"{member} must >register")
                else:
                    if arg2 is None:
                        await ctx.send("You must specify the coin bet")
                    else:
                        if user1Info["Pink coins"] < arg2:
                            await ctx.send("You dont have enough coins")
                            print(user1Info["Pink coins"])
                        elif user2Info["Pink coins"] < arg2:
                            await ctx.send(f"{member} dosnt have enough coins")
                        else:
                            things = {"User1 name": f"{ctx.author}", "User1 id": f"{ctx.author.id}",
                                      "User2 name": f"{member}", "User2 id": f"{member.id}",
                                      "Coins": arg2}
                            duelinv.insert_one(things)
                            await ctx.send(f"{member} has been challenged")

    @commands.command()
    async def accept(self, ctx):
        user1 = duelinv.find_one({"User2 id": f"{ctx.author.id}"})
        if not user1:
            await ctx.send("No-one has invite you")
        else:
            u1 = uinfo.find_one({"User id": user1["User1 id"]})
            u2 = uinfo.find_one({"User id": user1["User2 id"]})
            if u1["Active Armor"] == "stone armor":
                health1 = 30
            elif u1["Active Armor"] == "iron armor":
                health1 = 45
            elif u1["Active Armor"] == "diamond armor":
                health1 = 60
            elif u1["Active Armor"] == "crystal armor":
                health1 = 80
            elif u1["Active Armor"] == "crystal armor":
                health1 = 100
            else:
                health1 = 20

            if u2["Active Armor"] == "stone armor":
                health2 = 30
            elif u2["Active Armor"] == "iron armor":
                health2 = 45
            elif u2["Active Armor"] == "diamond armor":
                health2 = 60
            elif u2["Active Armor"] == "crystal armor":
                health2 = 80
            elif u2["Active Armor"] == "crystal armor":
                health2 = 100
            else:
                health2 = 20

            things = {"User1 name": user1["User1 name"], "User1 id": user1["User1 id"], "User1 health": health1,
                      "User2 name": user1["User2 name"], "User2 id": user1["User2 id"], "User2 health": health2,
                      "Coins": user1["Coins"]}
            duelfight.insert_one(things)
            duelinv.delete_one({'User1 id': user1["User1 id"]})
            await ctx.send("You have accepted the duel")

    @commands.command()
    async def cancel(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Please specify whos duel you would like to accept")
        else:
            user1 = duelinv.find_one({"User2 id": f"{ctx.author.id}"})
            if not user1:
                await ctx.send("No-one has invite you")
            else:
                duelinv.delete_one({'User1 id': f'{member.id}'})
                await ctx.send("You have accepted the duel")

    @commands.command()
    async def hit(self, ctx):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        user1 = duelfight.find_one({"User1 id": f"{ctx.author.id}"})
        user2 = duelfight.find_one({"User2 id": f"{ctx.author.id}"})
        if user1:
            if user["Active Weapon"] == "Default Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 1}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Wood Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 2}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Stone Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 3}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Flower Sword":
                attack.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 4}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Strong Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': -5}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Incredible Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 5}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Destruction Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 6}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Soul Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 7}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Light Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 8}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Dark Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 8}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Destruction Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 9}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Illegal Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 10}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Reaper Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 11}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Coin Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 6}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Dragon Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 12}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Rainbow Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 13}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Pink Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 15}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Pride2020 Sword":
                duelfight.update_one({'User2 id': user1["User2 id"]}, {"$inc": {'User2 health': - 4}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            if user1["User2 health"] >= 0:
                await ctx.send(f"{user1['User1 name']} has won the duel")
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + user1["Coins"]}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + user1["Coins"]}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': + user1["Coins"]}})

        elif user2:
            if user["Active Weapon"] == "Default Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 1}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Wood Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 2}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Stone Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 3}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Flower Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 4}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Strong Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 5}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Incredible Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 5}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Destruction Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 6}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Soul Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 7}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Light Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 8}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Dark Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 8}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Destruction Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 9}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Illegal Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 9}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Reaper Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 10}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Coin Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 6}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Dragon Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 11}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Rainbow Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 12}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Pink Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 15}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            elif user["Active Weapon"] == "Pride2020 Sword":
                duelfight.update_one({'User1 id': user2["User1 id"]}, {"$inc": {'User1 health': - 4}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            if user2["User1 health"] >= 0:
                await ctx.send(f"{user1['User1 name']} has won the duel")
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + user2["Coins"]}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + user2["Coins"]}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': + user2["Coins"]}})

                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + user2["Coins"]}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + user2["Coins"]}})
                uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': + user2["Coins"]}})
        else:
            await ctx.send("You are not in a fight")


def setup(bot):
    bot.add_cog(Duel(bot))
