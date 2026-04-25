# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import ExistUser, ToSAccepted, Check
from src.database.mongodb import LastAction
from src.commands.study import study_json

tests = study_json["exam"]

@bot.command()
async def exam(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        player_level = int(Check(ctx.author.id, "level"))
        level_tests = tests[player_level + 1]
        random_test = random.choice(level_tests)

    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")