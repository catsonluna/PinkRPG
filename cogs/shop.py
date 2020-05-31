import datetime

import discord
from discord.ext import commands

from bot import db

uinfo = db["uinfo"]


class Inventory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def shop(self, ctx):
        color = ctx.author.color
        embed = discord.Embed(title='PinkBots shop', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="info",
                        value="This is the PinkBots shop, to buy something do >buy and the number of the item",
                        inline=False)

        embed.add_field(name="Wood sword",
                        value="Description: \nMade from the best wood by the best woodsman will slice your enemies like paper \n "
                              "\nQuality: \nCommon \n "
                              "\nDamage: \n2 \n "
                              "\nPrice: \n200PC \n"
                              "\nCommand: \n>buy 1",
                        inline=True)

        embed.add_field(name="Strong sword",
                        value="Description: \nMade for the strongest and only for the strongest, this sword will slay everyone \n "
                              "\nQuality: \nRare \n "
                              "\nDamage: \n5 \n "
                              "\nPrice: \n1000PC \n"
                              "\nCommand: \n>buy 2",
                        inline=True)

        embed.add_field(name="Soul sword",
                        value="Description: \nCrafted from million dead souls, you will hear their screams \n "
                              "\nQuality: \nEpic \n "
                              "\nDamage: \n7 \n "
                              "\nPrice: \n3500PC \n"
                              "\nCommand: \n>buy 3",
                        inline=True)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def buy(self, ctx, arg1: int = None):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user:
            if arg1 is None:
                await ctx.send("please specify a thing you want to buy")
            elif arg1 == 1:
                if user["Pink coins"] >= 200:
                    if user["Weapons"]["Stone Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": -200}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Wood Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +200}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +200}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Stone sword")
                else:
                    await ctx.send("You dont have enough coins")
            elif arg1 == 2:
                if user["Pink coins"] >= 1000:
                    if user["Weapons"]["Strong Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": - 1000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Strong Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +1000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +1000}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Strong sword")
                else:
                    await ctx.send("You dont have enough coins")
            elif arg1 == 3:
                if user["Pink coins"] >= 3500:
                    if user["Weapons"]["Soul Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": -3500}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Soul Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +3500}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +3500}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Soul sword")
                else:
                    await ctx.send("You dont have enough coins")
            else:
                await ctx.send("To buy something, user >buy 1, 2 or 3")
        else:
            ctx.send("You must >register to do this")

    @commands.command(pass_context=True)
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def bonus(self, ctx):
        user = uinfo.find_one({"User id": f'{ctx.author.id}'})
        if user:
            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": +60}})
            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Pink coins": +60}})
            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Bonuses claimed": +1}})
            uinfo.update_one({"_id": 1}, {"$inc": {"Bonuses claimed": +1}})
            uinfo.update_one({"_id": 1}, {"$inc": {"Lifetime coins": +60}})
            await ctx.send("You have claimed 60 coins")
        else:
            await ctx.send("You must >register to do this command")
            self.bonus.reset_cooldown(ctx)


def setup(bot):
    bot.add_cog(Inventory(bot))
