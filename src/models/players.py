from src.models.symbols import Symbol


class Player:
    def __init__(self, player_id: int, player_name: str, player_type: str, symbol: Symbol):
        self.player_id = player_id
        self.player_name = player_name
        self.player_type = player_type
        self.symbol = symbol
