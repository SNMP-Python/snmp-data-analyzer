from abc import ABC, abstractmethod
from typing import List

from graph.router_node import RouterNode


class GraphCreator(ABC):
    @abstractmethod
    def get_graph(self) -> List[RouterNode]:
        pass
