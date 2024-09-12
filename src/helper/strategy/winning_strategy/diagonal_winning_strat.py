from src.helper.strategy.winning_strategy.winning_strategy import WinningStrategy
from src.models.board import Board
from src.models.cell import Cell


class DiagonalWinningStrategy(WinningStrategy):

    def __init__(self):
        self.diagonal1_count = {}
        self.diagonal2_count = {}

    def check_winner(self, board: Board, cell: Cell):
        row = cell.row
        col = cell.column
        symbol = cell.player.symbol

        if row == col:  # left diagonal
            if symbol not in self.diagonal1_count:
                self.diagonal1_count[symbol] = 0
            self.diagonal1_count[symbol] += 1

            if self.diagonal1_count[symbol] == board.board_size:
                return True

        if row + col == board.board_size - 1:  # right diagonal
            if symbol not in self.diagonal2_count:
                self.diagonal2_count[symbol] = 0
            self.diagonal2_count[symbol] += 1

            if self.diagonal2_count[symbol] == board.board_size:
                return True

        return False

    def handle_undo(self, board: Board, cell: Cell):
        row = cell.row
        col = cell.column
        symbol = cell.player.symbol

        if row == col:  # left diagonal
            self.diagonal1_count[symbol] -= 1

        if row + col == board.board_size - 1:  # right diagonal
            self.diagonal2_count[symbol] -= 1
