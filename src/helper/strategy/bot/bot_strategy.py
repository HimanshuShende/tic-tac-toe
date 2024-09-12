from abc import ABC, abstractmethod

from src.models.board import Board


class BotStrategy(ABC):
    @abstractmethod
    def decide_cell_to_move(self, board: Board):
        raise NotImplementedError()