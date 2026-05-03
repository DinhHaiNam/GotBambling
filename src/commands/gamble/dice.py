# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.random_algo import gb_random_dice
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check

@bot.command(aliases=["d"])
async def dice(ctx, choice: int, bet: int = 1):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        bet = abs(bet) #:)))))
        name = ctx.message.author.display_name

        if Check(ctx.author.id, "wallet") < bet:
            await ctx.send("Not enough money!")
            return
        
        else:
            if choice not in [1, 2, 3, 4, 5, 6]:
                choice = random.randrange(1, 6)

            dice = gb_random_dice()
            message = f"{name} choose: {choice} and DICE: {dice}\n"

            if choice == dice:
                bet *= 3
                message += f"{name} Won **{bet}** =)"
                Pay(ctx.author.id, bet)
            
            else:
                message += f"{name} Lost **-{bet}** =("
                Pay(ctx.author.id, -bet)

            await ctx.send(message)

    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")