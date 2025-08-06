class MiniMon:
    def __init__(self, name, level, maxHp, attack, defense):
        self.name = name
        self.level = level
        self.maxHp = maxHp
        self.currentHp = maxHp
        self.attack = attack
        self.defense = defense
        self.moves = []
        self.status = None # for paralyzed or collapsed etc
    
    def take_damage(self, damage):
        effective_damage = max(0, damage - self.defense)
        self.currentHp -= effective_damage
        if self.currentHp < 0:
            self.currentHp = 0
        return effective_damage