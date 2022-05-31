from parser.value_objects.router import Router
from typing import Dict, FrozenSet, List

from distance.distance_calculator import DistanceCalculator
from distance.points import Points
from graph.router_node import RouterNode


class DistanceCalculatorImp(DistanceCalculator):
    def __init__(self, graph: FrozenSet[RouterNode]):
        self.graph = graph

    def get_distances(self) -> Dict[Points, List[Router]]:
        """
        Given a graph of router nodes, returns a dictionary which represents:
        {Point: routers}
        where:
            point: is a source router and a destination router
            routers: are a list that has the routers that you had to go through
            to get to your destination

        Be aware that the points should be bidirectional. For example:
        R1 -> R2 is the same as R2 -> R1 (you can redefine equals on Points), be
        aware that this redefinition to equals implies the redefinition of equals
        in the Router object too! (And maybe more objects)
        """
