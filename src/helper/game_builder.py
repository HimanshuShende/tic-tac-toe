from src.custom_exceptions.invalid_player_exception import InvalidPlayerException


class GameBuilder:
    def __init__(self):
        self.dimensions = None
        self.players = None
        self.winning_strategies = None

    def set_dimensions(self, dimensions):
        self.dimensions = dimensions
        return self

    def set_players(self, players):
        self.players = players
        return self

    def set_winning_strategies(self, winning_strategies):
        self.winning_strategies = winning_strategies
        return self

    def validate(self):
        if len(self.players) != self.dimensions - 1:
            raise InvalidPlayerException(f"No. of player must be {self.dimensions - 1}")

    def build(self):
        from src.models.game import Game
        self.validate()
        return Game(self.dimensions, self.players, self.winning_strategies)
