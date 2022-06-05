from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def normal(self, message: str) -> None:
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass
