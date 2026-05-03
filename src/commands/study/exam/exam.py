# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted, Check
from src.database.mongodb import LastAction
from src.base.data import study_json

tests = study_json["exam"]

@bot.command()
async def exam(ctx):
    exist = bool(ExistUser(ctx.author.id))
    tos = bool(ToSAccepted(ctx.author.id))

    if exist and tos:
        now = datetime.now()
        date = now.date()

        player_last_exam = LastAction.Check(ctx.author.id, "exam")
        last_date = player_last_exam["date"]

        if date != last_date:
            player_level = Check(ctx.author.id, "level")
            test = random.choice(tests[player_level + 1]["tests"])
            

    else:
        if not exist:
            await ctx.send("You must register first!")
        elif not tos:
            await ctx.send("You must agree with our Term of Serivce")