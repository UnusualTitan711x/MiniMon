class Player:
    name = "Player"

    def __init__(self, name):
        self.name = name
        self.miniMons = []
        self.activeMiniMon = None
        self.items = []