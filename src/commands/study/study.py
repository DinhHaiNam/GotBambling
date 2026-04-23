# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import load_json
from src.database.mongodb import ExistUser, ToSAccepted, Pay, Check, LastAction, Education

study_json = load_json("src/json/study.json") 
lessons = study_json["lessons"]

@bot.command()
async def study(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        now = datetime.now()
        date = str(now.date())

        if Check(ctx.author.id, "wallet") < 5:
            await ctx.send("Not enough money!")

        if LastAction.Check(ctx.author.id, "study") != date:
            lesson = random.choice(lessons)
            name = lesson["name"]
            point = lesson["point"]

            Education.Update(ctx.author.id, point)
            Pay(ctx.author.id, -5)
            await ctx.send(f"{ctx.message.author.display_name} learned {name} and gained {point} study point(s)!")

            LastAction.Update(ctx.author.id, "study", date)
        
        else:
            await ctx.send(f"{ctx.message.author.display_name} learned today and cant learn more =(")

    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")