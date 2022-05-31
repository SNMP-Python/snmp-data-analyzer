from parser.value_objects.router import Router
from typing import FrozenSet, List

from graph.graph_creator import GraphCreator, RouterNode


class GraphCreatorImp(GraphCreator):
    def __init__(self, routers: List[Router]):
        self.routers_list = routers

    def get_graph(self) -> FrozenSet[RouterNode]:
        """
        Given a router list, returns a graph which represents the connection between routers
        :return: An immutable set that has RouterNodes
        """
