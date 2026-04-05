from src.base.bot import *
from src.base.random_algo import gb_random_cf

@bot.command(aliases=["cf", "coin"])
async def coinflip(ctx, choices: str):
    if choices[0].lower() != "n" and choices[0].lower() != "s":
        return
    
    else:
        rand = gb_random_cf()

        if (choices.lower() == "s" and rand == 0) or (choices.lower() == "n" and rand == 1):
            await ctx.send(f"You won")
        else:
            await ctx.send(f"You lost")
