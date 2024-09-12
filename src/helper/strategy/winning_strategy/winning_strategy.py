from abc import ABC, abstractmethod

from src.models.board import Board
from src.models.cell import Cell


class WinningStrategy(ABC):

    @abstractmethod
    def check_winner(self, board: Board, cell: Cell): raise NotImplementedError()

    @abstractmethod
    def handle_undo(self, board: Board, cell: Cell): raise NotImplementedError()
