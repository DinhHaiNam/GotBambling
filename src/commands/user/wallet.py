# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import shorthand
from src.database.mongodb import CheckWallet, ExistUser, ToSAccepted

@bot.command(aliases=["money", "cash"])
async def wallet(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        await ctx.send(f"Your Balance: {shorthand(CheckWallet(ctx.author.id))}")
    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")