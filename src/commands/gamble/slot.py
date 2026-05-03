# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.random_algo import gb_random_slot
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check

@bot.command(aliases=["s"])
async def slot(ctx, bet: int = 1):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        bet = abs(bet) #:)))))
        name = ctx.message.author.display_name

        if Check(ctx.author.id, "wallet") < bet:
            await ctx.send("Not enough money!")
            return

        else:
            S1 = gb_random_slot()
            S2 = gb_random_slot()
            S3 = gb_random_slot()
            
            animals = ["<:dog:>", "<:cat:>", "<:chicken:>", "<:fish:>"]

            message = f"SLOT: {animals[S1]}**|**{animals[S2]}**|**{animals[S3]}\n"

            if S1 == S2 and S2 == S3:

                if S1 == 0:
                    bet *= 5
                elif S1 == 1:
                    bet *= 3
                elif S1 == 2:
                    bet *= 2
                
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
