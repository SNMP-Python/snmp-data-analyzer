from abc import ABC, abstractmethod

from graph.router_graph import RouterGraph


class GraphCreator(ABC):

    @abstractmethod
    def get_graph(self) -> RouterGraph:
        pass
