# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base.modules import *

def shorthand(num: int) -> str:
    if num >= 1000000:
        return f"{num / 1000000000}M"
    if num >= 1000000000:
        return f"{num / 1000000000000}B"
    else:
        return num
    
def GetBonus(bonus: int) -> int:
    rand1 = random.choice([1, 2, 3])
    rand2 = random.choice([1, 2, 3])
    if rand1 == rand2:
        return random.randrange(1, bonus)
    else:
        return 0
    
def GetPunish(forfeit: int) -> int:
    rand1 = random.choice([1, 2, 3, 4, 5])
    rand2 = random.choice([1, 2, 3, 4, 5])
    if rand1 == rand2:
        return forfeit
    else:
        return 0
    
def load_json(path: str):
    with open(path, "r") as f:
        return json.load(f)