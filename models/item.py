class Item:
    def __init__(self, name:str):
        self.name = name

class HealthPotion(Item):
    def __init__(self, name, health_amount):
        super().__init__(name)
        self.health = health_amount

class PowerBoost(Item):
    def __init__(self, name, boost_amount):
        super().__init__(name)
        self.boost = boost_amount