from models.player import Player
from models.minimon import MiniMon
from models.example_minimons import BUBBLE, FLAMO, GROG
import random

class Game:
    def __init__(self):
        self.player = Player(
            name="Player1",
            minimons=[BUBBLE, FLAMO, GROG],
            active_minimon=BUBBLE
        )
        self.opponent = Player(
            name="Opponent",
            minimons=[FLAMO, GROG],
            active_minimon=FLAMO
        )

        self.turn = "player"
        self.battle_log = []
        self.result = "ND"
    
    def player_turn(self, move_name: str):
        move = next(m for m in self.player.active_minimon.moves if m.name == move_name)

        if move in self.player.active_minimon.moves:
            damage = self.player.active_minimon.use_move(move, self.opponent.active_minimon)
            self.battle_log.append(f"{self.player.active_minimon.name} used {move.name} for {damage} damage.")

        if self.opponent.active_minimon.is_fainted():
            self.battle_log.append(f"{self.opponent.active_minimon.name} has fainted! {self.player.name} wins!")
            self.result = "win"
            return "win"

        self.turn = "opponent"
        return "ok"
    
    def opponent_turn(self):
        move = random.choice(self.opponent.active_minimon.moves)
        damage = self.opponent.active_minimon.use_move(move, self.player.active_minimon)
        self.battle_log.append(f"{self.opponent.name} used {move.name} causing {damage} damage.")

        if self.player.active_minimon.is_fainted():
            self.battle_log.append(f"{self.player.active_minimon.name} has fainted! {self.opponent.name} wins!")
            self.result = "lose"
            return "lose"
        
        self.turn = "player"
        return "ok"
    
    def get_state(self):
        return{
            "turn": self.turn,
            "player": {
                "name": self.player.name,
                "active": self.player.active_minimon
            },
            "opponent": {
                "name": self.opponent.name,
                "active": self.opponent.active_minimon
            },
            "log": self.battle_log,
            "result": self.result
        }