class MiniMon:
    def __init__(self, name: str, maxHp: int, attack: int, defense: int, image_text:str=None, moves=None):
        self.name = name
        self.max_hp = maxHp
        self.current_hp = maxHp
        self.attack = attack if attack is not None else 5
        self.defense = defense
        self.moves = moves if moves is not None else []
        self.status = "Alive" if not self.is_fainted() else "Fainted" # for paralyzed or collapsed etc
        self.image = image_text
    
    def take_damage(self, damage):
        effective_damage = max(0, damage)
        self.current_hp -= effective_damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_fainted(self) -> bool:
        return self.current_hp <= 0
    
    def use_move(self, move, target):
        if move in self.moves:
            damage = max(1, move.power + self.attack - target.defense)
            target.take_damage(damage)
            return damage
        else:
            raise ValueError(f"{self.name} does not know the move {move.name}")