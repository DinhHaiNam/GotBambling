# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.database.mongodb import usr

@bot.command(aliases=["agree"])
async def confirm(ctx):
    user = usr.find_one({"_id": ctx.author.id})
    if user["tos"] == 0:
        id = {"_id": ctx.author.id}
        new_tos = {"$set": {"tos": True}}
        usr.update_one(id, new_tos)
        await ctx.send("Register successfully!")