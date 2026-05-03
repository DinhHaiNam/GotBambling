# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted, Check

@bot.command()
async def health(ctx):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        await ctx.send(f"{ctx.message.author.display_name}'s health: {int(Check(ctx.author.id, "healthy")) * 10}%")

    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")