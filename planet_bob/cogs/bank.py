import discord
from discord.ext import commands, tasks
import json
import os
import datetime

class Bank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.balances = {}

    @commands.command()
    async def balance(self, ctx):
        user = ctx.author
        if user.id not in self.balances:
            self.balances[user.id] = 100
        await ctx.send(f"{user.mention} has {self.balances[user.id]} dollars")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def add(self, ctx, member: discord.Member, amount: int):
        self.balances[member.id] += amount
        await ctx.send(f"{member.mention} now has {self.balances[member.id]} dollars")

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def remove(self, ctx, member: discord.Member, amount: int):
        self.balances[member.id] -= amount
        await ctx.send(f"{member.mention} now has {self.balances[member.id]} dollars")