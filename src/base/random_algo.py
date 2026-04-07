# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

from src.base.modules import *

def pick(a: int, b: int, choice: int) -> int:
    return a if choice == 1 else b

def bit() -> int:
    return random.choice([1, 0])

def gb_random_cf() -> int:
    rand1 = bit()
    rand2 = bit()
    rand3 = bit()
    rand4 = bit()

    Qround1 = pick(rand1, rand2, bit())
    Qround2 = pick(rand2, rand3, bit())
    Qround3 = pick(rand3, rand4, bit())

    Sround1 = pick(Qround1, Qround2, bit())
    Sround2 = pick(Qround2, Qround3, bit())

    return pick(Sround1, Sround2, bit())

def gb_random_slot() -> int:
    rand1 = bit() + bit() + bit()
    rand2 = bit() + bit() + bit()
    rand3 = bit() + bit() + bit()

    randA = pick(rand1, rand2, bit())
    randB = pick(rand2, rand3, bit())

    return pick(randA, randB, bit())

def gb_random_dice() -> int:
    dice1 = 1 + bit() + bit() + bit() + bit() + bit()
    dice2 = 1 + bit() + bit() + bit() + bit() + bit()
    dice3 = 1 + bit() + bit() + bit() + bit() + bit()
    dice4 = 1 + bit() + bit() + bit() + bit() + bit()
    dice5 = 1 + bit() + bit() + bit() + bit() + bit()
    dice6 = 1 + bit() + bit() + bit() + bit() + bit()

    rand1 = pick(dice1, dice2, bit())
    rand2 = pick(dice2, dice3, bit())
    rand3 = pick(dice3, dice4, bit())
    rand4 = pick(dice4, dice5, bit())
    rand5 = pick(dice5, dice6, bit())

    randA = pick(rand1, rand2, bit())
    randB = pick(rand2, rand3, bit())
    randC = pick(rand3, rand4, bit())
    randD = pick(rand4, rand5, bit())

    randX = pick(randA, randB, bit())
    randY = pick(randB, randC, bit())
    randZ = pick(randC, randD, bit())

    randL = pick(randX, randY, bit())
    randR = pick(randY, randZ, bit())

    return pick(randL, randR, )