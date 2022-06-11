from typing import Dict, Set, List

from netaddr import IPAddress, IPNetwork

from distance.distance_calculator import DistanceCalculator
from distance.path import Path
from distance.point import Point
from graph.router_node import RouterNode
from parser.value_objects.router import Router

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
        if entry.network != IPNetwork("0.0.0.0/0") and point.destination in entry.network:
            return entry.next_hop
    raise Exception(f"Couldn't find point {point} on router: {current_router.sys_name}")


def _search_adjacent_for_ip(
        destination: IPAddress, node: RouterNode
) -> Router:
    for adjacent in node.adjacents:
        if _destination_in_router(destination, adjacent.router):
            return adjacent.router
    raise Exception(f"Couldn't find destination {destination} inside adjacents of {node.router.sys_name}")


class DistanceCalculatorImp(DistanceCalculator):
    def __init__(self, graph: List[RouterNode], first_hop: str):
        self.first_hop = first_hop
        self.graph = self._sort_graph(graph.copy())
        self.distances: Dict[Point, Path] = {}
        self.destinations = self._get_destinations()

    def _sort_graph(self, graph: List[RouterNode]) -> List[RouterNode]:
        first_hop_addr = IPAddress(self.first_hop)
        first_router = self._get_first_router(first_hop_addr, graph)
        graph.remove(first_router)
        new_graph = [first_router]
        while graph:
            current_router = graph.pop(0)
            new_graph.append(current_router)
        return new_graph

    @staticmethod
    def _get_first_router(first_hop: IPAddress, graph: List[RouterNode]) -> RouterNode:
        for node in graph:
            for interface in node.router.interfaces:
                if interface.network.ip == first_hop:
                    return node

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
            self, point: Point, current_router: Router
    ) -> None:
        """
        Calculates the shortest path between two ip's.
        :param point: Point to calculate the distance for
        :param current_router: Router being currently calculated
        :return: If recursive call has finished
        """
        self.distances[point].add_router(current_router)
        if _destination_in_router(point.destination, current_router):
            return
        next_hop: IPAddress = _get_next_hop_for_destination(point, current_router)
        current_node: RouterNode = self._get_node_for_router(current_router)
        if next_hop == DIRECTLY_CONNECTED_IP_NH:
            next_router = _search_adjacent_for_ip(
                point.destination, current_node
            )
        else:
            next_router = _search_adjacent_for_ip(next_hop, current_node)
        self._get_distance_for_point(
            point, next_router
        )  # Recursive call with the next router

    def _get_node_for_router(self, router: Router) -> RouterNode:
        for node in self.graph:
            if node.router == router:
                return node
        raise Exception(f"Couldn't find router {router.sys_name} on graph. References error")
