from discord.ext import commands
import json
import os
import datetime

class Bank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bank_file = "bank.json"  # name of the file to store bank data
        self.bank = self.load_bank_data()  # load bank data from file

    def load_bank_data(self):
        if os.path.exists(self.bank_file):
            with open(self.bank_file, "r") as f:
                return json.load(f)
        else:
            return {}

    def save_bank_data(self):
        with open(self.bank_file, "w") as f:
            json.dump(self.bank, f)

    def get_balance(self, user_id):
        if user_id not in self.bank:
            self.bank[user_id] = {"balance": 100, "last_daily": str(datetime.date.today())}
            self.save_bank_data()
        elif self.bank[user_id]["last_daily"] != str(datetime.date.today()):
            self.bank[user_id]["balance"] += 25
            self.bank[user_id]["last_daily"] = str(datetime.date.today())
            self.save_bank_data()
        return self.bank[user_id]["balance"]

    @commands.command(name="balance", aliases=["bal"])
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        balance = self.get_balance(user_id)
        await ctx.send(f"{ctx.author.mention}, your current balance is {balance} dollars.")

    @commands.command(name="add")
    @commands.has_permissions(administrator=True)
    async def add(self, ctx, member: commands.MemberConverter, amount: int):
        user_id = str(member.id)
        if user_id not in self.bank:
            self.bank[user_id] = {"balance": amount, "last_daily": str(datetime.date.today())}
        else:
            self.bank[user_id]["balance"] += amount
        self.save_bank_data()
        await ctx.send(f"{ctx.author.mention}, added {amount} dollars to {member.mention}'s balance.")

    @commands.command(name="remove")
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx, member: commands.MemberConverter, amount: int):
        user_id = str(member.id)
        if user_id not in self.bank:
            self.bank[user_id] = {"balance": 0, "last_daily": str(datetime.date.today())}
        else:
            self.bank[user_id]["balance"] -= amount
        self.save_bank_data()
        await ctx.send(f"{ctx.author.mention}, removed {amount} dollars from {member.mention}'s balance.")
