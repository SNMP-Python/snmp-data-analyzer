from typing import Dict, FrozenSet, List, Optional

from netaddr import IPAddress, IPNetwork

from distance.distance_calculator import DistanceCalculator
from distance.path import Path
from distance.points import Points
from graph.router_node import RouterNode
from parser.value_objects.router import Router


class DistanceCalculatorImp(DistanceCalculator):
    def __init__(self, graph: FrozenSet[RouterNode]):
        self.graph = graph
        self.distances: Dict[Points, Path] = {}
        self.destinations = self._get_destinations()

    def _get_destinations(self) -> set[IPAddress]:
        """
        Calculates all the ip's from the network.
        :return: Set of all the ip's from the network
        """
        destinations = set()
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                destinations.add(interface.network.ip)
        return destinations

    def get_distances(self) -> Dict[Points, Path]:
        """
        For every pair of ip's calculates the shortest path between them.
        :return: Dict of points with the shortest paths between these two points
        """
        for router_node, interface, destination in self._get_interfaces_with_destination():
            point = Points(interface.network.ip, destination)
            if self._discard_point(point):
                continue
            path = self._get_distance_for_point(point, router_node.router, Path())
            if self.distances.get(point) is None or self.distances[point] > path:
                self.distances[point] = path

        return self.distances

    @staticmethod
    def _discard_point(point: Points) -> bool:  # TODO: Test method
        """
        Determines whether a point should be discarded or not.
        :param point: Point to be determine if it should be discarded or not
        :return: True if the point should be discarded, False otherwise
        """
        return point.source == point.destination

    def _get_interfaces_with_destination(self):
        """
        Iterates over all the routers, interfaces and possible destinations
        :return: Generator of tuples of the form (router_node, interface, destination)
        """
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                for destination in self.destinations:
                    yield router_node, interface, destination

    def _get_distance_for_point(self, point: Points, current_router: Router, path: Path) -> Path:
        """
        Fills the distances dict with the shortest path between the two points
        :param point: Points to fill the dict with
        """
        path.add_router(current_router)
        for interface in current_router.interfaces:
            if interface.network.ip == point.destination:
                return path
        next_router = self._get_next_router(point, current_router)
        return self._get_distance_for_point(point, next_router, path)

    def _get_next_router(self, point: Points, current_router: Router) -> Router:
        next_hop = DistanceCalculatorImp._find_next_hop_for_destination(point, current_router)
        if next_hop == IPAddress('0.0.0.0'):
            return self._search_adjancent_router(point, current_router)
        router = self._find_router_for_next_hop(next_hop)
        return router

    @staticmethod
    def _find_next_hop_for_destination(point: Points, current_router: Router) -> IPAddress:
        for entry in current_router.routing_table:
            if (point.destination & entry.network.netmask) == entry.network.network:
                return entry.next_hop

    def _search_adjancent_router(self, point: Points, current_router: Router) -> Router:
        current_router_node = self._find_router_node_for_router(current_router)
        for adjacent_router in current_router_node.adjacents:
            for interface in adjacent_router.router.interfaces:
                if point.destination == interface.network.ip:
                    return adjacent_router.router

    def _find_router_node_for_router(self, router: Router) -> RouterNode:
        for router_node in self.graph:
            if router_node.router == router:
                return router_node

    def _find_router_for_next_hop(self, next_hop: IPAddress) -> Optional[Router]:
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                if next_hop == interface.network.ip:
                    return router_node.router
        return None
