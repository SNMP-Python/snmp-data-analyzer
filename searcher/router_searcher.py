from abc import ABC, abstractmethod
from typing import List

from searcher.router_primitives import RouterPrimitives


class RouterSearcher(ABC):

    @abstractmethod
    def get_router_primitives(self) -> List[RouterPrimitives]:
        pass
