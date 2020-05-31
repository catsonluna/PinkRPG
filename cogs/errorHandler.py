import traceback
import sys
from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return

        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)

        if isinstance(error, ignored):
            return

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.MissingPermissions):
            return await ctx.send(f"You are missing `{error.missing_perms}` permission(s)")

        elif isinstance(error, commands.CommandOnCooldown):
            if error.retry_after / 3600 >= 60:
                return await ctx.send(
                    f'you can do `{ctx.command}` in {error.retry_after / 3600:.0f} hrs ')
            else:
                return await ctx.send(
                    f'you can do `{ctx.command}` in {error.retry_after / 60:.0f} mins {error.retry_after % 60:.0f} secs ')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send('I could not find that member. Please try again.')

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
