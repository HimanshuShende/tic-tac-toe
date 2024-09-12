from src.models.cell import Cell
from src.models.cell_status import CellStatus
from src.models.game import Game
from src.models.game_status import GameStatus
from src.models.players import Player


class GameService:

    def start_game(self, size, players, winning_strategies):
        GBuilder = Game.game_builder() \
            .set_players(players) \
            .set_dimensions(size) \
            .set_winning_strategies(winning_strategies)\
            .build()
        return GBuilder

    def display_game(self, game: Game) -> None:
        game.board.print_board()

    def move(self, game: Game):
        current_player: Player = game.players[game.next_player_turn]

        cell = current_player.decide_cell_to_move(game.board)
        cell.player = current_player
        cell.status = CellStatus.FILLED

        game.moves.append(cell)

        if self.check_winner(game, cell):
            game.game_status = GameStatus.COMPLETED
            game.winner = current_player

        elif len(game.moves) == game.board.board_size * game.board.board_size:
            game.game_status = GameStatus.DRAW

        game.next_player_turn += 1
        game.next_player_turn %= len(game.players)

    def check_winner(self, game: Game, cell: Cell):
        return any(
            ws.check_winner(game.board, cell) for ws in game.winning_strategies
        )

    def undo(self, game: Game):
        if not game.moves:
            print("No moves left to undo")
            return

        cell = game.moves.pop()

        # handling undo for all winning strategy
        for ws in game.winning_strategies:
            ws.handle_undo(game.board, cell)

        cell.status = CellStatus.EMPTY
        cell.player = None

        game.winner = None
        game.game_status = GameStatus.IN_PROGRESSED
        game.next_player_turn -= 1
        game.next_player_turn %= len(game.players)
