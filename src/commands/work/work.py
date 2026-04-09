# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import GetBonus, GetPunish, load_json
from src.database.mongodb import ExistUser, ToSAccepted, Pay, LastAction

work_json = load_json("src/json/work.json")
jobs = work_json["part-time-job"]
punishes = work_json["punish"]

@bot.command(aliases=["w"])
async def work(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        now = datetime.now()
        date = str(now.date())

        if LastAction.Check(ctx.author.id, "work") != date:
            message = f"You worked as a"
            salary = 0

            rand_job = random.choice(jobs)
            job_name = rand_job["name"]
            message += f" {job_name}"
            salary += (rand_job["salary"] + GetBonus(rand_job["bonus"]))

            rand_punish = random.choice(punishes)
            punish_name = rand_punish["name"]
            forfeit = GetPunish(rand_punish["forfeit"])
            if forfeit != 0:
                salary -= forfeit
                message += f" and {punish_name}"

            message += f", so you earned {salary}!"

            Pay(ctx.author.id, salary)
            await ctx.send(message)

            LastAction.Update(ctx.author.id, "work", date)

        else:
            await ctx.send("You worked today and cant work more =(")
            return
    
    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")