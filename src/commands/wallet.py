from src.base import *
from src.database.mongodb import CheckWallet, FirstCommand

@bot.command(aliases=["money", "cash"])
async def wallet(ctx):
    await ctx.send(f"Your Balance: {CheckWallet(ctx.author.id)}")