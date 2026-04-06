from src.base import *
from src.database.mongodb import UserRegister

@bot.command()
async def register(ctx):
    UserRegister(ctx.author.id)
    await ctx.send("Register Sucessfully!")