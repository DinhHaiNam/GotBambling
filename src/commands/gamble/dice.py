# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.random_algo import gb_random_dice
from src.database.mongodb import ExistUser, ToSAccepted, Pay, CheckWallet

@bot.command(aliases=["d"])
async def dice(ctx, choice: int = 1, bet: int = 1):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        if CheckWallet(ctx.author.id) < bet:
            await ctx.send("Not enough money!")
        
        else:
            dice = gb_random_dice()
            message = f"DICE: {dice}\n"

            if choice == dice:
                bet *= 3
                message += f"You Won **{bet}** =)"
                Pay(ctx.author.id, "increase", bet)
            
            else:
                message += f"You Lost **-{bet}** =("
                Pay(ctx.author.id, "decrease", bet)

            await ctx.send(message)

    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")