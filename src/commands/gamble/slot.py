from src.base import *
from src.base.random_algo import gb_random_slot
from src.database.mongodb import ExistUser, ToSAccepted, Pay, CheckWallet

@bot.command(aliases=["s"])
async def slot(ctx, bet: int = 1):
    if ExistUser(ctx.author.id) and ToSAccepted(ctx.author.id):
        if CheckWallet(ctx.author.id) < bet:
            await ctx.send("Not enough money!")

        else:
            S1 = gb_random_slot()
            S2 = gb_random_slot()
            S3 = gb_random_slot()
            
            animals = ["<:dog:>", "<:cat:>", "<:chicken:>", "<:fish:>"]

            message = f"SLOT: {animals[S1]}**|**{animals[S2]}**|**{animals[S3]}\n"

            if S1 == S2 and S2 == S3:

                if S1 == 0:
                    bet *= 5
                elif S1 == 1:
                    bet *= 3
                elif S1 == 2:
                    bet *= 2
                
                message += f"You Won **{bet}** =)"
                Pay(ctx.author.id, "increase", bet)
            
            else:
                message += f"You Lost **-{bet}** =("
                Pay(ctx.author.id, "decrease", bet)

            await ctx.send(message)
            
    else:
        await ctx.send("You must register first!")
