class MiniMon:
    def __init__(self, name, damage, level, maxHp, attack, defense):
        self.name = name
        self.damage = damage
        self.level = level
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.attack = attack
        self.defense = defense
        self.status = None # for paralyzed or collapsed etc