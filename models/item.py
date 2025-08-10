class Item:
    def __init__(self, name:str):
        self.name = name

class HealthPotion(Item):
    def __init__(self, health_amount):
        self.name = f"Health Potion +{health_amount}"
        self.health = health_amount
    
    def use(self, minimon):
        minimon.heal(self.health)

class PowerBoost(Item):
    def __init__(self, boost_amount):
        self.name = f"Power Boost +{boost_amount}"
        self.boost = boost_amount
    
    def use(self, minimon):
        minimon.boost(self.boost)