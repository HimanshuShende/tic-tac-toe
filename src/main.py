from src.controller.game_controller import GameController
from src.helper.strategy.winning_strategy.diagonal_winning_strat import DiagonalWinningStrategy
from src.models.bot_difficulty import BotDifficulty
from src.models.bots import Bot
from src.models.game import Game
from src.models.game_status import GameStatus
from src.models.player_type import PlayerType
from src.models.players import Player
from src.models.symbols import Symbol
from src.services.game_service import GameService

if __name__ == "__main__":
    game_service = GameService()
    game_controller = GameController(game_service)

    dimensions = 3

    players = [
        Player(player_id=1, player_name="Rohan", player_type=PlayerType.HUMAN, symbol=Symbol("x")),
        Bot(player_id=1, player_name="Bot", symbol=Symbol("y"), difficulty=BotDifficulty.EASY),
    ]

    winning = [
        DiagonalWinningStrategy(),
    ]

    game: Game = game_controller.start_game(dimensions=dimensions, players=players, winning_strategy=winning)
    # display board
    game_controller.display_board(game)

    # until game in-progress, take input
    while game.game_status == GameStatus.IN_PROGRESSED:
        game_controller.move(game)
        print()
        game_controller.display_board(game)
        undo_answer = input("Do you want to undo? If yes, press 1: ")

        if undo_answer == "1":
            print("Undo...")
            game_controller.undo_move(game)
            game_controller.display_board(game)

    if game.game_status == GameStatus.COMPLETED:
        print("\nWinner : ", game.winner.player_name)
    elif game.game_status == GameStatus.DRAW:
        print("\nDraw!!")


# TODO: 1. Medium and hard bot strategy
#       2. Row and Column winning strategy
#       3. Implement multiple undoes
#       4. undo a snapshot
#       5. try other winning algo
