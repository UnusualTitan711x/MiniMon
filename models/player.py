from models.minimon import MiniMon

class Player:
    name = "Player"

    def __init__(self, name: str, minimons:MiniMon=None, active_index:int=None,items=None):
        self.name = name
        self.minimons = minimons if minimons is not None else []
        self.active_index = active_index if active_index is not None else 0
        self.items = items if items is not None else []
    
    def get_active_minimon(self):
        return self.minimons[self.active_index]

    def swap_minimon(self, minimon_name: str):
        """ Swap the current minimon with another one in your list """

        minimon = next(m for m in self.minimons if m.name == minimon_name)

        if minimon and self.active_minimon != minimon:
            self.active_minimon = minimon

