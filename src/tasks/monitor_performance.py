# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base import *

@tasks.loop(minutes=2)
async def monitor_performance():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"CPU: {cpu}%, Memory: {memory}%")