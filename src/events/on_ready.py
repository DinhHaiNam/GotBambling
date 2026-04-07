# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is online!")