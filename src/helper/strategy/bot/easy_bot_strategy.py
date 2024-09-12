from src.helper.strategy.bot.bot_strategy import BotStrategy
from src.models.board import Board
from src.models.cell_status import CellStatus


class EasyBotStrategy(BotStrategy):
    def decide_cell_to_move(self, board: Board):
        for row in board.grid:
            for cell in row:
                if cell.status == CellStatus.EMPTY:
                    return cell
        return None
