from discord.ext import commands

class NewCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def new_command(self, ctx):
        # Define your command code here
        await ctx.send('This is a new command!')

def setup(bot):
    bot.add_cog(NewCommand(bot))
