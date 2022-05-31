from abc import ABC, abstractmethod
from typing import FrozenSet

from graph.router_node import RouterNode


class GraphCreator(ABC):
    @abstractmethod
    def get_graph(self) -> FrozenSet[RouterNode]:
        pass
