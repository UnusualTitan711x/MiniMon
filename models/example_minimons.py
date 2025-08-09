from models.minimon import MiniMon
from models.moves import Move

# Example Move instances
TACKLE = Move(
    name="Tackle",
    power=4,
    pp=35
)

BITE = Move(
    name="Bite",
    power=5,
    pp=25
)

AVALANCHE = Move(
    name="Avalanche",
    power=4,
    pp=15
)

WATER_GUN = Move(
    name="Water-Gun",
    power=5,
    pp=30
)

# Example MiniMon instances -----------------------------------
BUBBLE = MiniMon(
    name="Bubble",
    maxHp=20,
    attack=3,
    defense=2,
    moves=[TACKLE, WATER_GUN]
)

FLAMO = MiniMon(
    name="Flamo",
    maxHp=22,
    attack=4,
    defense=2,
    moves=[TACKLE, BITE]
)

GROG = MiniMon(
    name="Grog",
    maxHp=20,
    attack=2,
    defense=3,
    moves=[TACKLE, AVALANCHE]
)

MITE = MiniMon(
    name="Mite",
    maxHp=20,
    attack=2,
    defense=3,
    moves=[TACKLE, AVALANCHE, BITE]
)