from src.base.modules import *

def pick(a: int, b: int, choice: int) -> int:
    return a if choice == 1 else b

def bit():
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