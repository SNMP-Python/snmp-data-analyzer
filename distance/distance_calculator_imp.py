from parser.value_objects.router import Router
from typing import Dict, FrozenSet, Optional, Set, List

from netaddr import IPAddress

from distance.distance_calculator import DistanceCalculator
from distance.path import Path
from distance.point import Point
from graph.router_node import RouterNode

DIRECTLY_CONNECTED_IP_NH = IPAddress('0.0.0.0')


def _discard_point(point: Point) -> bool:
    return point.source == point.destination


def _destination_in_router(destination: IPAddress, router: Router) -> bool:
    for interface in router.interfaces:
        if interface.network.ip == destination:
            return True
    return False


def _get_next_hop_for_destination(
    point: Point, current_router: Router
) -> IPAddress:
    for entry in current_router.routing_table:
        if (point.destination & entry.network.netmask) == entry.network.network:
            return entry.next_hop


def _search_adjacent_for_ip(
    destination: IPAddress, node: Optional[RouterNode]
) -> Optional[Router]:
    if node is None:
        return None
    for adjacent in node.adjacents:
        if _destination_in_router(destination, adjacent.router):
            return adjacent.router
    return None


class DistanceCalculatorImp(DistanceCalculator):
    def __init__(self, graph: List[RouterNode]):
        self.graph = graph
        self.distances: Dict[Point, Path] = {}
        self.destinations = self._get_destinations()

    def _get_destinations(self) -> Set[IPAddress]:
        """
        Calculates all the ip's from the network, which will serve as destinations for the points.
        :return: Set of all the ip's from the network
        """
        destinations = set()
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                destinations.add(interface.network.ip)
        return destinations

    def get_distances(self) -> Dict[Point, Path]:
        """
        For every pair of ip's calculates the shortest path between them.
        :return: Dict of points with the shortest paths between these two points
        """
        for (
            router_node,
            interface,
            destination,
        ) in self._get_interfaces_with_destination():
            point = Point(interface.network.ip, destination)
            if _discard_point(point) or point in self.distances:
                continue
            self.distances[point] = Path()
            self._get_distance_for_point(point, router_node.router)

        return self.distances

    def _get_interfaces_with_destination(self):
        """
        Iterates over all the routers, interfaces and possible destinations and yields them.
        :return: Generator of tuples of the form (router_node, interface, destination)
        """
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                for destination in self.destinations:
                    yield router_node, interface, destination

    def _get_distance_for_point(
        self, point: Point, current_router: Optional[Router]
    ) -> None:
        """
        Calculates the shortest path between two ip's.
        :param point: Point to calculate the distance for
        :param current_router: Router being currently calculated
        :return: If recursive call has finished
        """
        if current_router is None:
            return
        self.distances[point].add_router(current_router)
        if _destination_in_router(point.destination, current_router):
            return
        next_hop = _get_next_hop_for_destination(point, current_router)
        current_node = self._get_node_for_router(current_router)
        if next_hop == DIRECTLY_CONNECTED_IP_NH:
            next_router = _search_adjacent_for_ip(
                point.destination, current_node
            )
        else:
            next_router = _search_adjacent_for_ip(next_hop, current_node)
        self._get_distance_for_point(
            point, next_router
        )  # Recursive call with the next router

    def _get_node_for_router(self, router: Router) -> Optional[RouterNode]:
        for node in self.graph:
            if node.router == router:
                return node
        return None
