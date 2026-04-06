from src.base import *

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")