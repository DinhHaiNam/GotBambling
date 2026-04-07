# -------------------------------------------------------
# Got BamBling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.random_algo import gb_random_cf
from src.database.mongodb import ExistUser, ToSAccepted, Pay, CheckWallet

@bot.command(aliases=["cf", "coin"])
async def coinflip(ctx, choices: str, bet: int = 1):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        if CheckWallet(ctx.author.id) < bet:
            await ctx.send("Not enough money!")

        else:
            if choices.lower() != "n" and choices.lower() != "s":
                return
            
            else:
                rand = gb_random_cf()

                if (choices.lower() == "s" and rand == 0) or (choices.lower() == "n" and rand == 1):
                    await ctx.send(f"You won **{bet}** =)")
                    Pay(ctx.author.id, "increase", bet)
                else:
                    await ctx.send(f"You lost **-{bet}** =(")
                    Pay(ctx.author.id, "decrease", bet)
    
    else:
        await ctx.send("You must register first!")
