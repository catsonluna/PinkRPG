import datetime
import random

import discord
from discord.ext import commands

from bot import db

attack = db["attack"]

ginfo = db["ginfo"]

uinfo = db["uinfo"]


def LevelUp(ctx):
    guild = ginfo.find_one({'guild id': f'{ctx.guild.id}'})
    cur_xp = guild['Guild Xp']
    cur_lvl = guild['Boss level']
    if cur_xp >= round(8 * (cur_lvl ** 2) / 4):
        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Boss level': + 1}})
        return True
    else:
        return False


class Attack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, 900, commands.BucketType.user)
    @commands.command(name='spawn')
    async def spawn(self, ctx, arg1: str = None):
        guild_id = str(ctx.guild.id)
        guild_name = str(ctx.guild)
        channel_id = str(ctx.channel.id)
        guild = attack.find_one({'guild id': f'{guild_id}'})
        channel = ginfo.find_one({'guild id': f'{guild_id}', 'Bot Channel': f'{channel_id}'})
        guildInfo = ginfo.find_one({"guild id": f"{ctx.guild.id}"})
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        if channel:
            if user:
                if arg1 is None:
                    await ctx.send("Please enter a number")
                    self.spawn.reset_cooldown(ctx)
                elif guild:
                    await ctx.send("Boss is already spawned, to spawn a new one, please kill the first one")
                elif arg1 == "lvl1" or arg1 == "1" or arg1 == "level1":
                    dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 1, "health": 20}
                    attack.insert_one(dmg)
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                    embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                    embed.add_field(name="Boss level:", value="1", inline=False)
                    embed.add_field(name="Boss hp:", value="20", inline=False)
                    embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                    ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})

                elif arg1 == "lvl5" or arg1 == "5" or arg1 == "level5":
                    if guildInfo['Boss level'] >= 5:
                        dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 5, "health": 50}
                        attack.insert_one(dmg)
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                        embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                        embed.add_field(name="Boss level:", value="5", inline=False)
                        embed.add_field(name="Boss hp:", value="50", inline=False)
                        embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                        ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="The guild hasnt reached this level.")
                        await ctx.send(embed=embed)
                        self.spawn.reset_cooldown(ctx)

                elif arg1 == "lvl10" or arg1 == "10" or arg1 == "level10":
                    if guildInfo['Boss level'] >= 10:
                        dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 10,
                               "health": 100}
                        attack.insert_one(dmg)
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                        embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                        embed.add_field(name="Boss level:", value="10", inline=False)
                        embed.add_field(name="Boss hp:", value="100", inline=False)
                        embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                        ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="The guild hasnt reached this level.")
                        await ctx.send(embed=embed)
                        self.spawn.reset_cooldown(ctx)

                elif arg1 == "lvl15" or arg1 == "15" or arg1 == "level15":
                    if guildInfo['Boss level'] >= 15:
                        dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 15,
                               "health": 250}
                        attack.insert_one(dmg)
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                        embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                        embed.add_field(name="Boss level:", value="15", inline=False)
                        embed.add_field(name="Boss hp:", value="250", inline=False)
                        embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                        ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="The guild hasnt reached this level.")
                        await ctx.send(embed=embed)
                        self.spawn.reset_cooldown(ctx)

                elif arg1 == "lvl20" or arg1 == "20" or arg1 == "level20":
                    if guildInfo['Boss level'] >= 20:
                        dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 20,
                               "health": 500}
                        attack.insert_one(dmg)
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                        embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                        embed.add_field(name="Boss level:", value="20", inline=False)
                        embed.add_field(name="Boss hp:", value="500", inline=False)
                        embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                        ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="The guild hasnt reached this level.")
                        await ctx.send(embed=embed)
                        self.spawn.reset_cooldown(ctx)

                elif arg1 == "lvl25" or arg1 == "25" or arg1 == "level25":
                    if guildInfo['Boss level'] >= 25:
                        dmg = {"guild id": f"{guild_id}", "guild name": f"{guild_name}", "Boss level": 25,
                               "health": 1000}
                        attack.insert_one(dmg)
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/698923359362220042/704011843039133768/Kirby.jpg")
                        embed.add_field(name="Boss spawned by:", value=ctx.message.author.mention, inline=False)
                        embed.add_field(name="Boss level:", value="25", inline=False)
                        embed.add_field(name="Boss hp:", value="1000", inline=False)
                        embed.add_field(name="Boss id:", value="#" + str(dmg["_id"]), inline=False)
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.bosses spawned": + 1}})
                        ginfo.update_one({'_id': 1}, {'$inc': {'bosses spawned': +1}})
                    else:
                        color = ctx.author.color
                        embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Error:", value="The guild hasnt reached this level.")
                        await ctx.send(embed=embed)
                        self.spawn.reset_cooldown(ctx)

                else:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="That is not a valid boss number.")
                    await ctx.send(embed=embed)
                    self.spawn.reset_cooldown(ctx)
            else:
                color = ctx.author.color
                embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Error:", value="Please do >register to do this command.")
                await ctx.send(embed=embed)
                self.spawn.reset_cooldown(ctx)
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="This isnt the set channel, do >setChannel to set the bots channel.")
            await ctx.send(embed=embed)
            self.spawn.reset_cooldown(ctx)

    @commands.command(name='attack')
    async def attack(self, ctx):
        channel_id = str(ctx.channel.id)
        gid = attack.find({'guild id': f'{ctx.guild.id}'})
        boss = attack.find_one({'guild id': f'{ctx.guild.id}'})
        channel = ginfo.find_one({'guild id': f'{ctx.guild.id}', 'Bot Channel': f'{channel_id}'})
        guild = ginfo.find_one({'guild id': f'{ctx.guild.id}'})
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})

        health = attack.find(
            {"guild id": f"{ctx.guild.id}"})
        if channel:
            for x in gid:
                if not user:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="Please do >register to do this command.")
                    await ctx.send(embed=embed)
                elif user["Active Weapon"] == "Default Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Wood Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 2}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Stone Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 3}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Flower Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 4}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Strong Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 5}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Incredible Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 5}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Destruction Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 6}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Soul Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 7}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                elif user["Active Weapon"] == "Light Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 8}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Dark Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 8}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Destruction Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 9}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Illegal Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 9}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Reaper Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 10}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                elif user["Active Weapon"] == "Coin Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 6}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 5}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 5}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +5}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                elif user["Active Weapon"] == "Dragon Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 11}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Rainbow Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 12}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

                elif user["Active Weapon"] == "Pink Sword":
                    attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 15}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Lifetime coins": + 1}})
                    uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Stats.Times attacked": + 1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                    uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})

            if not boss:
                await ctx.send("Boss is not spawned")
            elif health[0]["health"] <= 0:
                if boss["Boss level"] == 1:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 5}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 5 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl1 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl1 killed": + 1}})
                elif boss["Boss level"] == 5:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 15}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 15 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl5 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl5 killed": + 1}})
                elif boss["Boss level"] == 10:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 20}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 20 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl10 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl10 killed": + 1}})
                elif boss["Boss level"] == 15:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 30}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 30 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl15 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl15 killed": + 1}})
                elif boss["Boss level"] == 20:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 40}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 40 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl20 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl20 killed": + 1}})
                elif boss["Boss level"] == 25:
                    ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 70}})
                    embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                          timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Xp:", value="The guild gained 70 xp")
                    await ctx.send(embed=embed)
                    ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stat.Lvl25 killed": + 1}})
                    ginfo.update_one({"_id": 1}, {"$inc": {"Lvl25 killed": + 1}})
                attack.delete_one({'guild id': f'{ctx.guild.id}'})

                if LevelUp(ctx):
                    embed = discord.Embed(title="Level Up ^^", color=0xe386ee, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="LvL:",
                                    value=f"The guild just leveled up and is now level {guild['Boss level'] + 1} ^^")
                    await ctx.send(embed=embed)
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:", value="This isnt the set channel, do >setChannel to set the bots channel.")
            await ctx.send(embed=embed)

    @commands.command(name='crit')
    async def crit(self, ctx):
        channel_id = str(ctx.channel.id)
        gid = attack.find({'guild id': f'{ctx.guild.id}'})
        boss = attack.find_one({'guild id': f'{ctx.guild.id}'})
        channel = ginfo.find_one({'guild id': f'{ctx.guild.id}', 'Bot Channel': f'{channel_id}'})
        guild = ginfo.find_one({'guild id': f'{ctx.guild.id}'})
        user = uinfo.find_one({"User id": f"{ctx.author.id}"})
        hit = random.randint(1, 2)
        health = attack.find(
            {"guild id": f"{ctx.guild.id}"})
        if channel:
            for x in gid:
                if not user:
                    color = ctx.author.color
                    embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
                    embed.add_field(name="Error:", value="Please do >register to do this command.")
                    await ctx.send(embed=embed)
                else:
                    if hit == 1:
                        if user["Active Weapon"] == "Default Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 2}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Wood Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 4}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Stone Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 6}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Flower Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 8}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Strong Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 10}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Incredible Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 10}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Destruction Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 12}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Soul Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 14}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Light Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 16}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Dark Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 16}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Destruction Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 18}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Illegal Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 18}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Reaper Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 20}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Coin Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 12}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 5}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 5}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +5}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Dragon Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 22}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Rainbow Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 22}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")

                        elif user["Active Weapon"] == "Pink Sword":
                            attack.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'health': - 30}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"}, {"$inc": {"Pink coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Lifetime coins": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.Times attacked": + 1}})
                            uinfo.update_one({"User id": f"{ctx.author.id}"},
                                             {"$inc": {"Stats.crits successful": +1}})
                            uinfo.update_one({"_id": 1}, {"$inc": {"crits successful": +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Lifetime coins': +1}})
                            uinfo.update_one({'_id': 1}, {'$inc': {'Times attacked': +1}})
                            await ctx.send(f"`{ctx.author}` hit the crit attack")
                    else:
                        await ctx.send("You missed the crit")

                if not boss:
                    await ctx.send("Boss is not spawned")
                elif health[0]["health"] <= 0:
                    if boss["Boss level"] == 1:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 5}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 5 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl1 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl1 killed": + 1}})
                    elif boss["Boss level"] == 5:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 15}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 15 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl5 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl5 killed": + 1}})
                    elif boss["Boss level"] == 10:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 20}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 20 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl10 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl10 killed": + 1}})
                    elif boss["Boss level"] == 15:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 30}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 30 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl15 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl15 killed": + 1}})
                    elif boss["Boss level"] == 20:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 40}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 40 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stats.Lvl20 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl20 killed": + 1}})
                    elif boss["Boss level"] == 25:
                        ginfo.update_one({'guild id': f'{ctx.guild.id}'}, {"$inc": {'Guild Xp': + 70}})
                        embed = discord.Embed(title="The boss has been killed", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="Xp:", value="The guild gained 70 xp")
                        await ctx.send(embed=embed)
                        ginfo.update_one({"guild id": f"{ctx.guild.id}"}, {"$inc": {"Stat.Lvl25 killed": + 1}})
                        ginfo.update_one({"_id": 1}, {"$inc": {"Lvl25 killed": + 1}})
                    attack.delete_one({'guild id': f'{ctx.guild.id}'})

                    if LevelUp(ctx):
                        embed = discord.Embed(title="Level Up ^^", color=0xe386ee,
                                              timestamp=datetime.datetime.utcnow())
                        embed.add_field(name="LvL:",
                                        value=f"The guild just leveled up and is now level {guild['Boss level'] + 1} ^^")
                        await ctx.send(embed=embed)
        else:
            color = ctx.author.color
            embed = discord.Embed(colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Error:",
                            value="This isnt the set channel, do >setChannel to set the bots channel.")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Attack(bot))
