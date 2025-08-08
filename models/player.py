from models.minimon import MiniMon

class Player:
    name = "Player"

    def __init__(self, name: str, minimons:MiniMon=None, active_minimon:MiniMon=None, items=None):
        self.name = name
        self.minimons = minimons if minimons is not None else []
        self.active_minimon = active_minimon if active_minimon is not None else None
        self.items = items if items is not None else []
    
    def swap_minimon(self, minimon_name: str):
        """ Swap the current minimon with another one in your list """

        minimon = next(m for m in self.minimons if m.name == minimon_name)

        if minimon and self.active_minimon != minimon:
            self.active_minimon = minimon       

