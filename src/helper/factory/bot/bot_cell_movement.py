from src.helper.factory.bot.bot_factory import BotFactory
from src.helper.strategy.bot.easy_bot_strategy import EasyBotStrategy
from src.models.bot_difficulty import BotDifficulty


class BotCellMovementFactory(BotFactory):

    @staticmethod
    def getBot(difficulty):
        if difficulty == BotDifficulty.EASY:
            return EasyBotStrategy()
