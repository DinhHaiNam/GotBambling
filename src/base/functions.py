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