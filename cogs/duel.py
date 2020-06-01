
import discord
from discord.ext import commands

from bot import db

attack = db["attack"]

ginfo = db["ginfo"]

uinfo = db["uinfo"]

duelinv = db["duelinv"]


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
                                      "User2 name": f"{member}", "User2 id": f"{member.id}",
                                      "Coins": arg2}
                            duelinv.insert_one(things)
                            await ctx.send(f"{member} has been challenged")

    @commands.command()
    async def accept(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Please specify whos duel you would like to accept")
        else:
            user1 = duelinv.find_one({"User2 id": f"{ctx.author.id}"})
            user2 = duelinv.find_one({"User1 id": f"{member.id}"})
            if not user1:
                await ctx.send("No-one has invite you")
            elif not user2 and user1:
                await ctx.send("This user hasn't invite you")
            else:
                duelinv.update_one({'User1 id': f'{member.id}'}, {"$set": {'Accept': 1}})
                await ctx.send("You have accepted the duel")

    @commands.command()
    async def hit(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("You have to specify who your hitting")
        else:
            duelinv.find_one({"User2 id": f"{ctx.author.id}"})
            duelinv.find_one({"User1 id": f"{member.id}"})


def setup(bot):
    bot.add_cog(Duel(bot))
