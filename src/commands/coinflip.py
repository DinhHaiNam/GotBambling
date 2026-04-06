from src.base import *
from src.base.random_algo import gb_random_cf
from src.database.mongodb import FirstCommand, Pay

@bot.command(aliases=["cf", "coin"])
async def coinflip(ctx, choices: str, bet: int):
    if choices[0].lower() != "n" and choices[0].lower() != "s":
        return
    
    else:
        rand = gb_random_cf()

        if (choices.lower() == "s" and rand == 0) or (choices.lower() == "n" and rand == 1):
            await ctx.send(f"You won {bet}")
            Pay(ctx.author.id, "increase", bet)
        else:
            await ctx.send(f"You lost -{bet}")
            Pay(ctx.author.id, "decrease", bet)
