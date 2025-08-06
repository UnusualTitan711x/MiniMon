from models.minimon import MiniMon

class Player:
    name = "Player"

    def __init__(self, name: str, minimons:MiniMon=None, active_minimon:MiniMon=None, items=None):
        self.name = name
        self.minimons = minimons if minimons is not None else []
        self.active_minimon = active_minimon if active_minimon is not None else None
        self.items = items if items is not None else []
