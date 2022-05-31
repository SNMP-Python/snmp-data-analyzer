from __future__ import absolute_import

from abc import ABC, abstractmethod
from typing import FrozenSet

from searcher.primitives.router_primitives import RouterPrimitives


class RouterSearcher(ABC):
    @abstractmethod
    def get_router_primitives(self) -> FrozenSet[RouterPrimitives]:
        pass
