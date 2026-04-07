from src.base import *
from src.database.mongodb import UserRegister, ExistUser, ToSAccepted

@bot.command()
async def register(ctx):
    if ExistUser(ctx.author.id) == False or ToSAccepted(ctx.author.id) == False:
        await ctx.send("To register, you must agree with out Term of Service:\n-\n-\nBy using `gb confirm` you accepted with our ToS.")
        if ExistUser(ctx.author.id) == False:
            UserRegister(ctx.author.id)
    else:
        await ctx.send("You already registered!")