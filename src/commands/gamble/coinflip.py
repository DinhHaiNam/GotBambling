# -------------------------------------------------------
# Got BamBling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.random_algo import gb_random_cf
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check

@bot.command(aliases=["cf", "coin"])
async def coinflip(ctx, choices: str, bet: int = 1):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        bet = abs(bet) #:)))))
        name = ctx.message.author.display_name

        if Check(ctx.author.id, "wallet") < bet:
            await ctx.send("Not enough money!")
            return

        else:
            if choices.lower() != "n" and choices.lower() != "s":
                choices = "n"
        
            rand = gb_random_cf()

            if (choices.lower() == "s" and rand == 0) or (choices.lower() == "n" and rand == 1):
                await ctx.send(f"{name} won **{bet}** =)")
                Pay(ctx.author.id, bet)
            else:
                await ctx.send(f"{name} lost **-{bet}** =(")
                Pay(ctx.author.id, -bet)
    
    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")
