from src.models.board import Board
from src.models.cell import Cell
from src.models.cell_status import CellStatus
from src.models.symbols import Symbol


class Player:
    def __init__(self, player_id: int, player_name: str, player_type: str, symbol: Symbol):
        self.player_id = player_id
        self.player_name = player_name
        self.player_type = player_type
        self.symbol = symbol

    def decide_cell_to_move(self, board: Board) -> Cell:
        while True:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if 0 <= row < board.board_size and 0 <= col < board.board_size:
                if board.grid[row][col].status == CellStatus.EMPTY:
                    return board.grid[row][col]

            print("Invalid row or column or cell is filled")
