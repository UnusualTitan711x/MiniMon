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
  
def main():
    game = Game()

    while game.player.active_minimon.current_hp > 0 and game.opponent.active_minimon.current_hp > 0:

        print(f"{game.player.active_minimon.name} HP: {game.player.active_minimon.current_hp}")
        print(f"{game.opponent.active_minimon.name} HP: {game.opponent.active_minimon.current_hp} \n\n")


        if game.turn == "player":
            # move = game.player.choose_move()

            print(f"{game.player.name}'s turn. Choose a move:")
            print(f"{game.player.active_minimon.name}'s moves: {[move.name for move in game.player.active_minimon.moves]}")
            
            while True:
                move_name = input("Enter move name: ")
                if move_name in [m.name for m in game.player.active_minimon.moves]:
                    break
            
            move = next(m for m in game.player.active_minimon.moves if m.name == move_name)

            if move in game.player.active_minimon.moves:
                damage = game.player.active_minimon.use_move(move, game.opponent.active_minimon)
                print(f"{game.player.active_minimon.name} used {move.name}")

            if game.opponent.active_minimon.is_fainted():
                print(f"{game.opponent.active_minimon.name} has fainted!")
                print(f"{game.player.name} wins!")

            game.turn = "opponent"
        else:
            move = random.choice(game.opponent.active_minimon.moves)
            damage = game.opponent.active_minimon.use_move(move, game.player.active_minimon)
            print(f"{game.opponent.name} used {move.name} causing {damage} damage.")

            if game.player.active_minimon.is_fainted():
                print(f"{game.player.active_minimon.name} has fainted!")
                print(f"{game.opponent.name} wins!")
            
            game.turn = "player"


main()
