from src.helper.game_builder import GameBuilder
from src.models.board import Board
from src.models.game_status import GameStatus


class Game:
    def __init__(self, dimensions, players, winning_strategies):
        self.board = Board(dimensions)
        self.players = players
        self.winning_strategies = winning_strategies
        self.moves = []
        self.next_player_turn = 0
        self.winner = None
        self.game_status = GameStatus.IN_PROGRESSED

    # We are creating game_builder() here because we dont want to expose GameBuilder class to the client
    # typical example of encapsulation
    @staticmethod
    def game_builder() -> GameBuilder: return GameBuilder()
