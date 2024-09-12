# add ABC class
from abc import ABC, abstractmethod


class BotFactory(ABC):

    @staticmethod
    @abstractmethod
    def getBot(difficulty): raise NotImplementedError()
