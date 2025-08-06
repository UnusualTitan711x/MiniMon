class Move:
    """ Base class for all moves """
    def __init__(self, name, power, pp):
        self.name = name
        self.power = power
        self.pp = pp

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Accuracy: {self.accuracy}, PP: {self.pp})"