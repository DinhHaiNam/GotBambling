# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base.bot import *
from src.commands import *
from src.events import *
from src.base.functions import clrscr

def GotBambling():
    clrscr()
    bot.run(TOKEN)