from src.models.game import Game
from src.services.game_service import GameService


# GameController only passed the data to GameService
class GameController:

    def __init__(self, service: GameService):
        self.game_service = service

    def start_game(self, dimensions, players, winning_strategy):
        return self.game_service.start_game(dimensions, players, winning_strategy)

    def display_board(self, game: Game):
        self.game_service.display_game(game)

    def move(self, game: Game):
        self.game_service.move(game)

    def undo_move(self, game: Game):
        self.game_service.undo(game)

# start the game
# status of the game is IN_PROGRESS
# IN LOOP...
# display the board
# player makes a move on the board
# check for winner
# if no winner or not all cells filled:
# change next_turn index
# other player plays
# if yes winner found or match draw
# end the game
