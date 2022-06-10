from abc import ABC, abstractmethod


class Logger(ABC):

    def __init__(self, debug: bool):
        self.debug_enabled = debug

    @abstractmethod
    def normal(self, message: str) -> None:
        pass

    def debug(self, message: str) -> None:
        if self.debug_enabled:
            self._debug_impl(message)

    @abstractmethod
    def _debug_impl(self, message: str):
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass
