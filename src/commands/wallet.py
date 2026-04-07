from src.base import *
from src.database.mongodb import CheckWallet, ExistUser, ToSAccepted

@bot.command(aliases=["money", "cash"])
async def wallet(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        await ctx.send(f"Your Balance: {CheckWallet(ctx.author.id)}")
    else:
        await ctx.send("You must register first!")