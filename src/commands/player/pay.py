# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check

@bot.command(aliases=["give"])
async def pay(ctx, player: discord.User, amount: int):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        if amount > 0:
            if Check(ctx.author.id, "wallet") < amount:
                await ctx.send("Not enough money!")
                return
            
            if ExistUser(player.id) and player.id != ctx.author.id:
                Pay(ctx.author.id, -amount)
                Pay(player.id, amount)
                await ctx.send(f"{ctx.message.author.display_name} sended {amount} to {player.mention}")

            else:
                await ctx.send(f"{player.mention} not exist!")
        
        else:
            await ctx.send(f"{ctx.message.author.display_name} cant stole money!")
    
    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")