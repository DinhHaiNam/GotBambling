from src.base import *
from src.database.mongodb import *

@bot.command()
async def confirm(ctx):
    user = col.find_one({"_id": ctx.author.id})
    if user["tos"] == 0:
        id = {"_id": ctx.author.id}
        new_tos = {"$set": {"tos": 1}}
        col.update_one(id, new_tos)
        await ctx.send("Register successfully!")