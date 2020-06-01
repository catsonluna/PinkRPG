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

        embed.add_field(name="Flower sword",
                        value="Description: \nFound in the rarest flower, in a unknown location, the smell of this sword is fantastic \n "
                              "\nQuality: \nRare  \n "
                              "\nDamage: \n4 \n "
                              "\nPrice: \n600PC"
                              "\nCommand: \n>buy 1",
                        inline=True)

        embed.add_field(name="Destruction sword",
                        value="Description: \nThis sword will destroy everyone and everything, it will destroy worlds if its in the wrong arms, so be safe \n "
                              "\nQuality: \nRare  \n "
                              "\nDamage: \n6 \n "
                              "\nPrice: \n2000PC"
                              "\nCommand: \n>buy 2",
                        inline=True)

        embed.add_field(name="Dark sword",
                        value="Description: \nThe sword of the dark, taken from the darkest part of the multi-verse, the power this sword gives is imaginable \n "
                              "\nQuality: \nEpic  \n "
                              "\nDamage: \n8 \n "
                              "\nPrice: \n4000PC"
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
                if user["Pink coins"] >= 600:
                    if user["Weapons"]["Flower Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": -600}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Flower Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +600}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +600}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Flower sword")
                else:
                    await ctx.send("You dont have enough coins")
            elif arg1 == 2:
                if user["Pink coins"] >= 2000:
                    if user["Weapons"]["Strong Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": - 2000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Strong Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +2000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +2000}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Strong sword")
                else:
                    await ctx.send("You dont have enough coins")
            elif arg1 == 3:
                if user["Pink coins"] >= 4000:
                    if user["Weapons"]["Dark Sword"] == 1:
                        await ctx.send("You already have this weapon")
                    else:
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": -4000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Weapons.Dark Sword": 1}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Coins used": +4000}})
                        uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Things purchased": +1}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Coins used": +4000}})
                        uinfo.update_one({"_id": 1}, {"$inc": {"Things purchased": +1}})
                        await ctx.send("You have bought Dark sword")
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
