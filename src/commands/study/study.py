# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check, LastAction, Education
from src.base.data import lessons

@bot.command()
async def study(ctx):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        name = ctx.message.author.display_name

        now = datetime.now()
        date = str(now.date())

        if Check(ctx.author.id, "wallet") < 5:
            await ctx.send("Not enough money!")
            return

        if LastAction.Check(ctx.author.id, "study") != date:
            lesson = random.choice(lessons)
            name = lesson["name"]
            point = lesson["point"]

            Education.Update(ctx.author.id, point)
            Pay(ctx.author.id, -5)
            await ctx.send(f"{name} learned {name} and gained {point} study point(s)!")

            LastAction.Update(ctx.author.id, "study", date)
        
        else:
            await ctx.send(f"{name} learned today and cant learn more =(")

    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")