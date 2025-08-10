from models.player import Player
from models.minimon import MiniMon
from models.example_minimons import BUBBLE, FLAMO, GROG, MITE
from models.item import HealthPotion, PowerBoost 
from utils.data_loader import all_minimons, moves_dict
import random
import copy


class Game:
    def __init__(self):
        self.player = Player(
            name="Player1",
            minimons=[],
            active_index=0,
            items=[HealthPotion(5), PowerBoost(10), HealthPotion(10)] 
        )
        self.opponent = Player(
            name="Opponent",
            minimons=copy.deepcopy([all_minimons[2], all_minimons[5], all_minimons[0], all_minimons[8]]),
            active_index=1
        )

        self.turn = "player"
        self.battle_log = []
        self.result = "ND"
    
    def player_turn(self, move_name: str):
        if self.turn != "player": return

        move = next(m for m in self.player.get_active_minimon().moves if m.name == move_name)

        if move in self.player.get_active_minimon().moves:
            damage = self.player.get_active_minimon().use_move(move, self.opponent.get_active_minimon())
            self.battle_log.append(f"Your {self.player.get_active_minimon().name} used {move.name} for {damage} damage.")

        if self.opponent.get_active_minimon().is_fainted():
            self.battle_log.append(f"{self.opponent.name}'s {self.opponent.get_active_minimon().name} has fainted!")

            message = self.opponent.auto_switch_minimon()
            if message: self.battle_log.append(message)
            self.check_battle_end()
        
        self.turn = "opponent"

        if self.result == "win":
            return "win"
        else:
            return None
    
    def opponent_turn(self):
        if self.turn != "opponent": return

        move = random.choice(self.opponent.get_active_minimon().moves)
        damage = self.opponent.get_active_minimon().use_move(move, self.player.get_active_minimon())
        self.battle_log.append(f"{self.opponent.name}'s {self.opponent.get_active_minimon().name} used {move.name} causing {damage} damage.")

        if self.player.get_active_minimon().is_fainted():
            self.battle_log.append(f"{self.player.name}'s {self.player.get_active_minimon().name} has fainted!")
        
        self.turn = "player"
        self.check_battle_end()
    
    def check_battle_end(self):
        if not self.player.has_alive_minimons():
            self.battle_log.append(f"{self.player.name} has no more MiniMons.")
            self.battle_log.append("You lose!")
            self.result = "lose"
            return True
        elif not self.opponent.has_alive_minimons():
            self.battle_log.append(f"{self.opponent.name} has no more MiniMons.")
            self.battle_log.append("You win!")
            self.result = "win"
            return True
        return False


    def get_state(self):
        return{
            "turn": self.turn,
            "player": {
                "name": self.player.name,
                "active": self.player.get_active_minimon()
            },
            "opponent": {
                "name": self.opponent.name,
                "active": self.opponent.get_active_minimon()
            },
            "log": self.battle_log,
            "result": self.result
        }