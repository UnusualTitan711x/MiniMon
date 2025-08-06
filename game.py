from models.player import Player
from models.example_minimons import BUBBLE, FLAMO, GROG
import random

class Game:
    def __init__(self):
        self.player = Player(
            name="Player1",
            minimons=[BUBBLE, FLAMO, GROG],
            current_minimon=BUBBLE
        )
        self.opponent = Player(
            name="Opponent",
            minimons=[FLAMO, GROG],
            current_minimon=FLAMO
        )

        self.turn = "player"
        self.battle_log = []
    
def main():
    game = Game()

    while game.player.current_minimon.currentHp > 0 and game.opponent.current_minimon.currentHp > 0:
        if game.turn == "player":
            # move = game.player.choose_move()

            print(f"{game.player.name}'s turn. Choose a move:")
            print(f"{game.player.current_minimon.name}'s moves: {[move.name for move in game.player.current_minimon.moves]}")
            
            while True:
                move_name = input("Enter move name: ")
                if move_name in [m.name for m in game.player.current_minimon.moves]:
                    break
            
            move = next(m for m in game.player.current_minimon.moves if m.name == move_name)

            if move in game.player.current_minimon.moves:
                damage = game.player.current_minimon.use_move(move, game.opponent.current_minimon)
                game.battle_log.append(f"{game.player.current_minimon.name} used {move.name}")
                game.turn = "opponent"
        else:
            move = game.opponent.current_minimon.random.choice(game.opponent.current_minimon.moves)
            damage = game.player.current_minimon.use_mpve(move, game.player.current_minimon)
            game.battle_log.append(f"{game.opponent.name} used {move.name} causing {damage} damage.")
            game.turn = "player"
        
        print(f"{game.player.current_minimon.name} HP: {game.player.current_minimon.currentHp}")
        print(f"{game.opponent.current_minimon.name} HP: {game.opponent.current_minimon.currentHp}")


main()
