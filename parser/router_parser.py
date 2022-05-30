from abc import ABC, abstractmethod
from typing import List

from common.router import Router


class RouterParser(ABC):

    @abstractmethod
    def get_routers(self) -> List[Router]:
        pass
