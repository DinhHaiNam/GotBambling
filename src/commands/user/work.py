# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.base.functions import GetBonus
from src.database.mongodb import ExistUser, ToSAccepted, Pay, LastAction

with open("src/json/work.json", "r") as f:
    jobs = json.load(f)["part-time-job"]

@bot.command(aliases=["w"])
async def work(ctx):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        now = datetime.now()
        date = str(now.date())

        if LastAction.Check(ctx.author.id, "work") != date:

            rand_job = random.choice(jobs)
            name = rand_job["name"]
            salary = rand_job["salary"] + GetBonus(rand_job["bonus"])

            Pay(ctx.author.id, "increase", salary)
            await ctx.send(f"You worked as a {name} and earned {salary}!")

            LastAction.Update(ctx.author.id, "work", date)

        else:
            await ctx.send("You worked today and cant work more =(")
            return
    
    else:
        if ExistUser(ctx.author.id) == False:
            await ctx.send("You must register first!")
        elif ToSAccepted(ctx.author.id) == False:
            await ctx.send("You must agree with our Term of Serivce")