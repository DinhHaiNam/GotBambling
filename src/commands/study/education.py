# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted
from src.database.mongodb import Education as edu

@bot.command(aliases=["edu"])
async def education(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        level = edu.CheckLevel(ctx.author.id)
        current_point = edu.CheckPoints(ctx.author.id)
        next_level = (level + 1) * 10 - current_point
        embed = discord.Embed(
            title=f"{ctx.message.author.display_name}'s education level",
            description=(
                        f"**Current level:** Level {level}\n"
                        f"**[{"■" * (current_point % 10)}{"-" * int(next_level)}] {current_point % 10 * 10}%**\n"
                        f"{next_level} point(s) -> Level {level + 1}"
            )
        )
        await ctx.send(embed=embed)
    
    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")