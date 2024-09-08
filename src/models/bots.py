from src.models.player_type import PlayerType
from src.models.players import Player
from src.models.symbols import Symbol


class Bot(Player):
    def __init__(self, player_id: int, player_name: str, symbol: Symbol, difficulty: str):
        super().__init__(player_id, player_name, PlayerType.BOT, symbol)
        self.difficulty = difficulty