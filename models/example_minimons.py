from models.minimon import MiniMon
from models.moves import Move

# Example Move instances
TACKLE = Move(
    name="Tackle",
    power=4,
    pp=5
)

BITE = Move(
    name="Bite",
    power=5,
    pp=5
)

AVALANCHE = Move(
    name="Avalanche",
    power=4,
    pp=2
)

WATER_GUN = Move(
    name="Water-Gun",
    power=5,
    pp=4
)

# Example MiniMon instances -----------------------------------
BUBBLE = MiniMon(
    name="Bubble",
    max_hp=20,
    attack=3,
    defense=2,
    moves=[TACKLE, WATER_GUN],
    image_text=""" 
  (\\_/)
  (o o)
  /   \\
 (  v  )
  ^^ ^^"""
)

FLAMO = MiniMon(
    name="Flamo",
    max_hp=22,
    attack=4,
    defense=2,
    moves=[TACKLE, BITE],
    image_text="""
  /\\_/\\
 ( o.o )
  > ^ <"""
)

GROG = MiniMon(
    name="Grog",
    max_hp=20,
    attack=2,
    defense=3,
    moves=[TACKLE, AVALANCHE],
    image_text="""
   ____
  (    )
 (  o o )
 /   V   \\
 \\  ---  /
  \\_____/"""
)

MITE = MiniMon(
    name="Mite",
    max_hp=20,
    attack=2,
    defense=3,
    moves=[TACKLE, AVALANCHE, BITE],
    image_text="""
  ( 'o' )
  (  -  )
  (  U  )
   "" "" 
"""
)

ex_minimons = [BUBBLE, MITE, GROG, FLAMO]