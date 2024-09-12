from src.models.cell import Cell


class Board:
    def __init__(self, size: int):
        self.board_size = size
        self.grid = [[Cell(i, j) for j in range(size)] for i in range(size)]

    def print_board(self):
        for row in self.grid:
            for cell in row:
                cell.display()
            print()
