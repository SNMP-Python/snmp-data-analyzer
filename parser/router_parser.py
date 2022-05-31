from abc import ABC, abstractmethod
from parser.value_objects.router import Router
from typing import List


class RouterParser(ABC):
    @abstractmethod
    def get_routers(self) -> List[Router]:
        pass
