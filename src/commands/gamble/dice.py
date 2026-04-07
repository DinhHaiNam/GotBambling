from src.base import *
from src.base.random_algo import gb_random_dice
from src.database.mongodb import ExistUser, ToSAccepted, Pay, CheckWallet

@bot.command(aliases=["d"])
async def dice(ctx, choice: int, bet: int = 1):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        if CheckWallet(ctx.author.id) < bet:
            await ctx.send("Not enough money!")
        
        else:
            dice = gb_random_dice()
            message = f"DICE: {dice}]\n"

            if choice == dice:
                bet *= 3
                message += f"You Won **{bet}** =)"
                Pay(ctx.author.id, "increase", bet)
            
            else:
                message += f"You Lost **-{bet}** =("
                Pay(ctx.author.id, "decrease", bet)

            await ctx.send(message)

    else:
        await ctx.send("You must register first!")