import os
import discord
from discord.ext import commands
from cogs.handler import Bank

# Define the prefix as a variable
PREFIX = "!"

# Create the intents object and enable the members intent
intents = discord.Intents.default()
intents.members = True

# Create the bot instance with the specified prefix
bot = commands.Bot(command_prefix=PREFIX, description='Planet BoB Discord Bot', intents=intents)

# Load all cogs from the cogs directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Instantiate the Bank cog and add it to the bot
bot.add_cog(Bank(bot))

# Run the bot with the specified token
bot.run('MTA5MjY1MDI3NDIwMTU0MjczNw.GOaiYU.nm4xFLUqPCgzC-zPLQvbMwQ8IeHMhaf2vDlLw0')
