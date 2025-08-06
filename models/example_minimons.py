from models.minimon import MiniMon
from models.moves import Move

# Example Move instances
TACKLE = Move(
    name="Tackle",
    power=40,
    pp=35
)

BITE = Move(
    name="Bite",
    power=60,
    pp=25
)

AVALANCHE = Move(
    name="Avalanche",
    power=80,
    pp=15
)

WATER_GUN = Move(
    name="Water Gun",
    power=50,
    pp=30
)

# Example MiniMon instances
BUBBLE = MiniMon(
    name="Bubble",
    level=3,
    maxHp=100,
    attack=25,
    defense=15,
    moves=[TACKLE, WATER_GUN]
)

FLAMO = MiniMon(
    name="Flamo",
    level=5,
    maxHp=100,
    attack=30,
    defense=20,
    moves=[TACKLE, BITE]
)

GROG = MiniMon(
    name="Grog",
    level=4,
    maxHp=100,
    attack=35,
    defense=20,
    moves=[TACKLE, AVALANCHE]
)
