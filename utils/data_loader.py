import json
from models.minimon import MiniMon
from models.item import Item
from models.moves import Move
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

json_path = resource_path("data/minimon_data.json")

with open(json_path, encoding="utf-8") as f:
    data = json.load(f)

# Load moves into dictionary
moves_dict = {
    m["name"]: Move(m["name"], m["power"], m["pp"]) for m in data["moves"]
}

# load minimons
all_minimons = []

for m_data in data["minimons"]:
    minimon_moves = [moves_dict[move_name] for move_name in m_data["moves"]]

    m = MiniMon(
        name=m_data["name"],
        max_hp=m_data["max_hp"],
        attack=m_data["attack"],
        defense=m_data["defense"],
        image_text=m_data.get("image_text"),
        moves=minimon_moves
    )

    all_minimons.append(m)