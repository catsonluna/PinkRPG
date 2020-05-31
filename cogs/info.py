import datetime

import discord
from discord.ext import commands

from bot import db

uinfo = db["uinfo"]
attack = db["attack"]
ginfo = db["ginfo"]


class UserInfo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def userInfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        user = uinfo.find_one({"Discord name": f"{member}"})

        if user:
            color = ctx.author.color
            pfp = member.avatar_url
            embed = discord.Embed(title=f'{member} Stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=pfp)
            embed.add_field(name="Name:", value=f"{user['Name']}", inline=False)
            embed.add_field(name="Pink coins:", value=user["Pink coins"], inline=False)
            embed.add_field(name="Times attacked", value=user['Stats']["Times attacked"], inline=False)
            embed.add_field(name="Registration date:", value=user['Registration date'], inline=False)
            embed.add_field(name="Weapons:", value=f"all {member} weapons:", inline=False)
            if user["Weapons"]['Default Sword'] == 1:
                embed.add_field(name="Default Sword:", value="1 dmg", inline=True)

            if user["Weapons"]['Wood Sword'] == 1:
                embed.add_field(name="Wood Sword:", value="2 dmg", inline=True)

            if user["Weapons"]['Stone Sword'] == 1:
                embed.add_field(name="Stone Sword:", value="3 dmg", inline=True)

            if user["Weapons"]['Flower Sword'] == 1:
                embed.add_field(name="Flower Sword:", value="4 dmg", inline=True)

            if user["Weapons"]['Strong Sword'] == 1:
                embed.add_field(name="Strong Sword:", value="5 dmg", inline=True)

            if user["Weapons"]['Incredible Sword'] == 1:
                embed.add_field(name="Incredible Sword:", value="5 dmg", inline=True)

            if user["Weapons"]['Destruction Sword'] == 1:
                embed.add_field(name="Destruction Sword:", value="6 dmg", inline=True)

            if user["Weapons"]['Soul Sword'] == 1:
                embed.add_field(name="Soul Sword:", value="7 dmg", inline=True)

            if user["Weapons"]['Light Sword'] == 1:
                embed.add_field(name="Light Sword:", value="8 dmg", inline=True)

            if user["Weapons"]['Dark Sword'] == 1:
                embed.add_field(name="Dark Sword:", value="8 dmg", inline=True)

            if user["Weapons"]['Destruction Sword'] == 1:
                embed.add_field(name="Destruction Sword:", value="9 dmg", inline=True)

            if user["Weapons"]['Illegal Sword'] == 1:
                embed.add_field(name="Illegal Sword:", value="9 dmg", inline=True)

            if user["Weapons"]['Reaper Sword'] == 1:
                embed.add_field(name="Reaper Sword:", value="10 dmg", inline=True)

            if user["Weapons"]['Coin Sword'] == 1:
                embed.add_field(name="Coin Sword:", value="6 dmg + 5 coin for attack", inline=True)

            if user["Weapons"]['Dragon Sword'] == 1:
                embed.add_field(name="Dragon Sword:", value="11 dmg", inline=True)

            if user["Weapons"]['Rainbow Sword'] == 1:
                embed.add_field(name="Rainbow Sword:", value="12 dmg", inline=True)

            if user["Weapons"]['Pink Sword'] == 1:
                embed.add_field(name="PinkSword Sword:", value="15 dmg", inline=True)

            embed.add_field(name="Equipped weapon:", value=user["Active Weapon"], inline=False)

            if user["Titles"]['Some title'] == 1:
                embed.add_field(name="Titles:", value="All titles:", inline=False)
                if user["Titles"]['Owner'] == 1:
                    embed.add_field(name="Owner:", value="PinkBot owner", inline=True)

                if user["Titles"]['Admin'] == 1:
                    embed.add_field(name="Admin:", value="PinkBot admin", inline=True)

                if user["Titles"]['Staff'] == 1:
                    embed.add_field(name="Admin:", value="PinkBot staff", inline=True)

                if user["Titles"]['Beta tester'] == 1:
                    embed.add_field(name="Bate tester:", value="Bot tester while the bot was being made", inline=True)

                if user["Titles"]['Bug reporter'] == 1:
                    embed.add_field(name="Bug reporter:", value="This user reported a big bug", inline=True)

                if user["Titles"]['Banned'] == 1:
                    embed.add_field(name="Banned:", value="This user is banned on PinkBot", inline=True)
            embed.add_field(name="User version", value=user["version"], inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(f"`{member}` has not registered")

    @commands.command(pass_context=True)
    async def guildInfo(self, ctx, guild: discord.Guild = None):
        guild = ctx.guild if not guild else guild
        user = ginfo.find_one({"guild id": f"{guild.id}"})
        cur_lvl = user['Boss level']
        lvl = round(8 * (cur_lvl ** 2) / 4)
        if user:
            color = ctx.author.color
            embed = discord.Embed(title=f'{guild} Stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Boss level:", value=f"{user['Boss level']}", inline=False)
            embed.add_field(name="Xp", value=user["Guild Xp"], inline=False)
            embed.add_field(name="Xp required for next level:", value=f"{lvl}", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Please do >setChannel to view this")

    @commands.command(pass_context=True)
    async def bossInfo(self, ctx):
        guild = ctx.guild
        guildI = attack.find_one({"guild id": f"{guild.id}"})
        if guildI:
            color = ctx.author.color
            embed = discord.Embed(title='Boss stats', colour=color, timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Boss level:", value=f"{guildI['Boss level']}", inline=False)
            embed.add_field(name="Health", value=guildI["health"], inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("A boss isnt spawned")

    @commands.command(pass_context=True)
    async def botInfo(self, ctx):
        user = uinfo.find_one({"_id": 1})
        server = ginfo.find_one({"_id": 1})
        color = ctx.author.color
        embed = discord.Embed(title='Bot stats', colour=color, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="Registered users:", value=f"{user['Users']}", inline=False)
        embed.add_field(name="Registered servers", value=server["Guilds"], inline=False)
        embed.add_field(name="Bosses spawned", value=server["bosses spawned"], inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(UserInfo(bot))
