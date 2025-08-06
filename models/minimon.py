class MiniMon:
    def __init__(self, name, level, maxHp, attack, defense):
        self.name = name
        self.level = level
        self.max_hp = maxHp
        self.current_hp = maxHp
        self.attack = attack
        self.defense = defense
        self.moves = []
        self.status = None # for paralyzed or collapsed etc
    
    def take_damage(self, damage):
        effective_damage = max(0, damage - self.defense)
        self.current_hp -= effective_damage
        if self.current_hp < 0:
            self.current_hp = 0
        return effective_damage
    
    def use_move(self, move, target):
        if move in self.moves:
            damage = move.power + self.attack - target.defense
            target.take_damage(damage)
            return damage
        else:
            raise ValueError(f"{self.name} does not know the move {move.name}")