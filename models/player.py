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

    def switch_minimon(self, new_index:int=None):
        """ Swap the current minimon with another one in your list """
        self.active_index = new_index
        return f"{self.name} sent out {self.get_active_minimon().name}"
    
    def auto_switch_minimon(self):
        """ Swap the current minimon with another one in your list """
        if not self.has_alive_minimons():
            return None
        
        for i, m in enumerate(self.minimons):
            if not m.is_fainted():
                self.active_index = i
        
        return f"{self.name} sent out {self.get_active_minimon().name}"
    
    def has_alive_minimons(self):
        """ Checks if the player still has MinoMons that are alive """
        return any(not m.is_fainted() for m in self.minimons)

