from parser.value_objects.router import Router
from typing import Dict, FrozenSet, Optional, Set

from netaddr import IPAddress

from distance.distance_calculator import DistanceCalculator
from distance.path import Path
from distance.points import Points
from graph.router_node import RouterNode


def _discard_point(point: Points) -> bool:
    """
    Determines whether a point should be discarded because it has the same source and destination or not.
    :param point: Point to be determine if it should be discarded or not
    :return: True if the point should be discarded, False otherwise
    """
    return point.source == point.destination


def _destination_in_router(point: Points, current_router: Optional[Router]) -> bool:
    """
    Determines whether a point's destination is in the current router or not.
    :param point: Point to be determine if it's destination is in the current router or not
    :param current_router: Current router to be determine if the point's destination is in the current router or not
    :return: True if the point's destination is in the current router, False otherwise
    """
    if current_router is not None:
        for interface in current_router.interfaces:
            if interface.network.ip == point.destination:
                return True
    return False


def _find_next_hop_for_destination(point: Points, current_router: Optional[Router]) -> Optional[IPAddress]:
    """
    Finds the next hop for a point's destination in the current router.
        :param point: Point to be determine the next hop for its destination
        :param current_router: Current router being processed
        :return: Next hop for the point if found, None otherwise
    """
    if current_router is not None:
        for entry in current_router.routing_table:
            if (point.destination & entry.network.netmask) == entry.network.network:
                return entry.next_hop
    return None


class DistanceCalculatorImp(DistanceCalculator):
    def __init__(self, graph: FrozenSet[RouterNode]):
        self.graph = graph
        self.distances: Dict[Points, Path] = {}
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

    def get_distances(self) -> Dict[Points, Path]:
        """
        For every pair of ip's calculates the shortest path between them.
        :return: Dict of points with the shortest paths between these two points
        """
        for router_node, interface, destination in self._get_interfaces_with_destination():
            point = Points(interface.network.ip, destination)
            if _discard_point(point):
                continue
            path = self._get_distance_for_point(point, router_node.router, Path())
            self._update_path(point, path)

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

    def _update_path(self, point: Points, path: Path):
        """
        If the path is shorter than the one already in the dictionary, updates the dictionary with the new path.
        :param point: Points to be updated
        :param path: New path found for the point
        """
        if self.distances.get(point) is None or self.distances[point] > path:
            self.distances[point] = path

    def _get_distance_for_point(self, point: Points, current_router: Optional[Router], path: Path) -> Path:
        """
        Given a certain point, returns one possible path between the point's source and destination.
        :param point: Points to calculate the path for
        """
        path.add_router(current_router)
        if _destination_in_router(point, current_router):
            return path
        next_router = self._get_next_router(point, current_router)
        return self._get_distance_for_point(point, next_router, path)  # Recursive call with the next router found

    def _get_next_router(self, point: Points, current_router: Optional[Router]) -> Optional[Router]:
        """
        Given a certain point, returns the next router to get to the destination network.
        :param point: Points to calculate the next router for
        :param current_router:  Current router to be used to find the next router
        :return: Next router to get to the destination network
        """
        next_hop = _find_next_hop_for_destination(point, current_router)
        if next_hop == IPAddress('0.0.0.0'):
            return self._search_adjancent_router(point, current_router)
        router = self._find_router_for_next_hop(next_hop)
        return router

    def _search_adjancent_router(self, point: Points, current_router: Optional[Router]) -> Optional[Router]:
        """
        Looks in the adjacent routers for the router that has the destination network.
        :param point: Points whose destination network is being searched
        :param current_router: Current router to be used to find the next router
        :return: Router that has the destination network, None otherwise
        """
        current_router_node = self._find_router_node_for_router(current_router)
        if current_router_node is None:
            return None
        for adjacent_router in current_router_node.adjacents:
            for interface in adjacent_router.router.interfaces:
                if point.destination == interface.network.ip:
                    return adjacent_router.router
        return None

    def _find_router_node_for_router(self, router: Optional[Router]) -> Optional[RouterNode]:
        """
        Finds the router node for a router.
        :param router: Router to be find the router node for
        :return: Corresponding router node
        """
        for router_node in self.graph:
            if router_node.router == router:
                return router_node
        return None

    def _find_router_for_next_hop(self, next_hop: IPAddress) -> Optional[Router]:
        """
        Finds the router for a next hop.
        :param next_hop: Next hop to find the router for
        :return: Router if found, None otherwise
        """
        for router_node in self.graph:
            for interface in router_node.router.interfaces:
                if next_hop == interface.network.ip:
                    return router_node.router
        return None
