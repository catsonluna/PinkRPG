import datetime
from datetime import date
import discord
from discord.ext import commands

from bot import db, version

ginfo = db["ginfo"]
uinfo = db["uinfo"]


class Info(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(pass_context=True)
    async def setChannel(self, ctx):
        guild_id = str(ctx.guild.id)
        guild_name = str(ctx.guild)
        channel_id = str(ctx.channel.id)
        guild = ginfo.find_one({'guild id': f'{guild_id}'})
        link = await ctx.channel.create_invite(max_age=0)
        info = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Guild owner": f"{ctx.guild.owner}",
                "Boss level": 1,
                "Guild Xp": 0,
                "Stats": {
                    "bosses spawned": 0,
                    "Lvl1 killed": 0,
                    "Lvl5 killed": 0,
                    "Lvl10 killed": 0,
                    "Lvl15 killed": 0,
                    "Lvl20 killed": 0,
                    "Lvl25 killed": 0
                },
                "Bot Channel": channel_id,
                "Invite Link": f'{link}'}
        if not guild:
            ginfo.insert_one(info)
            ginfo.update_one({'_id': 1}, {'$inc': {'Guilds': +1}})
            await ctx.send("channel successfully added")
        else:
            ginfo.update_one({"guild id": f"{guild_id}"}, {"$set": {"Bot Channel": channel_id}})
            await ctx.send("channel successfully updated")

    @commands.command(pass_context=True, aliases=['setWeapon'])
    async def useSword(self, ctx, arg1: str = None):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if arg1 is None:
            await ctx.send("Please specify which weapon wou would like to use")
        elif arg1 == "Default" or arg1 == "default":
            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Default Sword"}})
            await ctx.send("Weapon equipped")
        elif arg1 == "Wood" or arg1 == "wood":
            if user["Weapons"]["Wood Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Wood Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Stone" or arg1 == "stone":
            if user["Weapons"]["Stone Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Stone Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Flower" or arg1 == "flower":
            if user["Weapons"]["Flower Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Flower Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Strong" or arg1 == "strong":
            if user["Weapons"]["Strong Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Strong Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Incredible" or arg1 == "incredible":
            if user["Weapons"]["Incredible Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Incredible Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Destruction" or arg1 == "destruction":
            if user["Weapons"]["Destruction Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Destruction Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Soul" or arg1 == "soul":
            if user["Weapons"]["Soul Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Soul Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Light" or arg1 == "light":
            if user["Weapons"]["Light Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Light Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Dark" or arg1 == "dark":
            if user["Weapons"]["Dark Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Dark Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Illegal" or arg1 == "illegal":
            if user["Weapons"]["Illegal Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Illegal Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Reaper" or arg1 == "reaper":
            if user["Weapons"]["Reaper Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Reaper Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Coin" or arg1 == "coin":
            if user["Weapons"]["Coin Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Coin Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Pink" or arg1 == "pink":
            if user["Weapons"]["Pink Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Pink Sword"}})
                await ctx.send("Weapon equipped")

            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Rainbow" or arg1 == "rainbow":
            if user["Weapons"]["Rainbow Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Rainbow Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        elif arg1 == "Pride2020" or arg1 == "pride2020":
            if user["Weapons"]["Pride2020 Sword"] == 1:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Active Weapon": "Pride2020 Sword"}})
                await ctx.send("Weapon equipped")
            else:
                await ctx.send("You dont have this weapon")
        else:
            await ctx.send("That weapon dosnt exist")

    @commands.command(pass_context=True)
    async def register(self, ctx, arg1: str = None):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user:
            await ctx.send("You are already registered")
            return
        if arg1 is None:
            await ctx.send("Please choose a username you would like to use")
            return
        numbers = len(arg1)
        if numbers < 3:
            await ctx.send("Your username must be 3-16 characters")
        elif numbers > 16:
            await ctx.send("Your username must be 3-16 characters")
        else:
            userN = uinfo.find_one({"Name": f"{arg1}"})
            if userN:
                await ctx.send("This username is already taken")
            else:
                dateT = date.today()
                info = {"Name": f"{arg1}", "Discord name": f"{ctx.author}", "User id": f"{ctx.author.id}",
                        "Pink coins": 0,
                        "Weapons": {
                            # common rarity
                            "Default Sword": 1,
                            "Wood Sword": 0,
                            "Stone Sword": 0,
                            # rare rarity
                            "Flower Sword": 0,
                            "Strong Sword": 0,
                            "Incredible Sword": 0,
                            "Destruction Sword": 0,
                            # epic rarity
                            "Soul Sword": 0,
                            "Light Sword": 0,
                            "Dark Sword": 0,
                            "Illegal Sword": 0,
                            "Reaper Sword": 0,
                            # legendary rarity
                            "Coin Sword": 0,
                            "Dragon Sword": 0,
                            "Rainbow Sword": 0,
                            "Pink Sword": 0,
                            # Special rarity
                            "Pride2020 Sword": 0},
                        "Armor": {
                            "Helmet": {
                                "Stone": 0,
                                "Iron": 0,
                                "Diamond": 0,
                                "Crystal": 0,
                                "Pink": 0},
                            "ChestPlate": {
                                "Stone": 0,
                                "Iron": 0,
                                "Diamond": 0,
                                "Crystal": 0,
                                "Pink": 0},
                            "Leggings": {
                                "Stone": 0,
                                "Iron": 0,
                                "Diamond": 0,
                                "Crystal": 0,
                                "Pink": 0},
                            "Boots": {
                                "Stone": 0,
                                "Iron": 0,
                                "Diamond": 0,
                                "Crystal": 0,
                                "Pink": 0}
                        },
                        "Titles": {"Owner": 0,
                                   "Admin": 0,
                                   "Staff": 0,
                                   "Beta tester": 0,
                                   "Bug reporter": 0,
                                   "Banned": 0,
                                   "Soft ban": 0,
                                   "Some title": 0},
                        "Stats": {"Lifetime coins": 0,
                                  "Coins used": 0,
                                  "Times attacked": 0,
                                  "Things purchased": 0,
                                  "Casino games played": 0,
                                  "Casino games won": 0,
                                  "Casino games lost": 0,
                                  "Dice games played": 0,
                                  "Dice games won": 0,
                                  "Dice games lost": 0,
                                  "Coin games played": 0,
                                  "Coin games won": 0,
                                  "Coin games lost": 0,
                                  "Bonuses claimed": 0,
                                  "Duels played": 0,
                                  "Duels won": 0,
                                  "Duels lost": 0,
                                  "crits made": 0,
                                  "crits successful": 0
                                  },
                        "Active Weapon": "Default Sword",
                        "Active Armor": "None",
                        "Items": {"Coin Booster": 0,
                                  "Damage Booster": 0},
                        "Registration date": f"{dateT}",
                        "version": version}
                user = uinfo.find_one({'User id': f'{ctx.author.id}'})
                if not user:
                    uinfo.insert_one(info)
                    uinfo.update_one({'_id': 1}, {'$inc': {'Users': +1}})
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Yay:", value="You are now registered!")
                    await ctx.send(embed=embed)
                else:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="You are already registered")
                    await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def sync(self, ctx):
        guild = ginfo.find_one({'guild id': f'{ctx.guild.id}'})
        if guild:
            cur_xp = guild['Guild Xp']
            cur_lvl = guild['Boss level']
            if cur_xp >= round(8 * (cur_lvl ** 2) / 4):
                ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Boss level': + 1}})
                embed = discord.Embed(title="Level Up ^^", color=0xe386ee, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="LvL:",
                                value=f"The guild just leveled up and is now level {guild['Boss level'] + 1} ^^")
                await ctx.send(embed=embed)
            else:
                await ctx.send("You are the max level you could be")
        else:
            await ctx.send("do >setChannel to do this")

    @commands.command()
    async def update(self, ctx):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user is None:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="Please do >register to do this command.")
            await ctx.send(embed=embed)
        else:
            if user["version"] < 0.2:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Stats.crits made": 0}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Stats.crits successful": 0}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"version": 0.2}})
                await ctx.send("You have updated to `version 0.2`")
            if user["version"] < 0.3:
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"pride2020": 0}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Weapons.Pride2020 Sword": 0}})
                uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"version": 0.3}})
                await ctx.send("You have updated to `version 0.3`")
            else:
                await ctx.send("You already are on the latest version")

    @commands.command()
    async def pride(self, ctx):
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if user:
            if user["version"] < 0.3:
                await ctx.send("Please >update, as you need to have version 0.3 or higher to use this command")
            else:
                if user["pride2020"] == 0:
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": +2000}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Pink coins": +2000}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"Weapons.Pride2020 Sword": 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$set": {"pride2020": 1}})
                    uinfo.update_one({"_id": 1}, {"$inc": {"pride2020": +1}})
                    uinfo.update_one({"_id": 1}, {"$inc": {"Lifetime coins": +2000}})
                    await ctx.send("You have claimed your pride month gift")
                else:
                    await ctx.send("You have already claimed the gift")
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="Please do >register to do this command.")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
