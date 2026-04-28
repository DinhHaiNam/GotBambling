# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *
from src.tasks import tasks_starter
from src.base.functions import clrscr

@bot.event
async def on_ready():
    await bot.tree.sync()
    tasks_starter()

    print(f"{bot.user} is online!")
    time.sleep(1)
    clrscr()
    print(" -------------------------------------------------------\n Got Bambling Discord Bot\n Copyright (C) Dinh Hai Nam 2026\n License: GPL 3.0\n https://github.com/DinhHaiNam/GotBambling\n -------------------------------------------------------")