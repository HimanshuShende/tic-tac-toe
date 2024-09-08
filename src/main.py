from src.controller.game_controller import GameController
from src.models.bot_difficulty import BotDifficulty
from src.models.bots import Bot
from src.models.player_type import PlayerType
from src.models.players import Player
from src.models.symbols import Symbol

if __name__ == "__main__":
    gc = GameController()

    dimensions = 3

    players = [
        Player(player_id=1, player_name="Rohan", player_type=PlayerType.HUMAN, symbol=Symbol("x")),
        Bot(player_id=1, player_name="Rohan", symbol=Symbol("y"), difficulty=BotDifficulty.MEDIUM),
    ]

    winning = []

    gc.start_game(dimensions=dimensions, players=players, winning_strategy=winning)
