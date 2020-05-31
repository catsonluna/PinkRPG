
import discord
from discord.ext import commands

from bot import db

attack = db["attack"]

ginfo = db["ginfo"]

uinfo = db["uinfo"]

duel = db["duel"]


class Duel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx, member: discord.Member = None, arg2: int = None):
        if member is None:
            await ctx.send("Please specify who you would like to duel")
        else:
            user1 = duel.find_one({"User1 id": f"{ctx.author.id}"})
            user1Info = uinfo.find_one({"User id": f"{ctx.author.id}"})
            user2Info = uinfo.find_one({"User id": f"{member.id}"})
            if user1:
                await ctx.send("You already challenged someone")
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
                            print(arg2)
                        elif user2Info["Pink coins"] < arg2:
                            await ctx.send(f"{member} dosnt have enough coins")
                        else:
                            things = {"User1 name": f"{ctx.author}", "User1 id": f"{ctx.author.id}",
                                      "User1 health": 20,
                                      "User2 name": f"{member}", "User2 id": f"{member.id}", "User2 health": 20,
                                      "Accept": 0,
                                      "Coins": arg2}
                            duel.insert_one(things)
                            await ctx.send(f"{member} has been challenged")

    @commands.command()
    async def accept(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Please specify whos duel you would like to accept")
        else:
            user1 = duel.find_one({"User2 id": f"{ctx.author.id}"})
            user2 = duel.find_one({"User1 id": f"{member.id}"})
            if not user1:
                await ctx.send("No-one has invite you")
            elif not user2 and user1:
                await ctx.send("This user hasn't invite you")
            else:
                duel.update_one({'User1 id': f'{member.id}'}, {"$set": {'Accept': 1}})
                await ctx.send("You have accepted the duel")

    @commands.command()
    async def hit(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("You have to specify who your hitting")
        else:
            user2 = duel.find_one({"User2 id": f"{ctx.author.id}"})
            user1 = duel.find_one({"User1 id": f"{member.id}"})


def setup(bot):
    bot.add_cog(Duel(bot))
