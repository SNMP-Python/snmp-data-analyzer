from itertools import chain
from parser.value_objects.router import Router
from typing import Dict, FrozenSet, List, Set

from netaddr import IPAddress

from graph.graph_creator import GraphCreator, RouterNode


class GraphCreatorImp(GraphCreator):
    def __init__(self, routers: List[Router]) -> None:
        self._routers = routers

    def get_graph(self) -> FrozenSet[RouterNode]:
        """
        Given a router list, returns a graph which represents the connection between routers
        :return: An immutable set that has RouterNodes
        """
        networks = self._build_networks()
        router_nodes = {router: RouterNode(router) for router in self._routers}
        for router in self._routers:

            adjacent_routers = set(
                chain.from_iterable(
                    network_routers - {router}
                    for network, network_routers in networks.items()
                    if router.is_connected(network)
                )
            )
            for adjacent in adjacent_routers:
                router_nodes[router].add_adjacent(router_nodes[adjacent])

        return frozenset(router_nodes.values())

    def _build_networks(self) -> Dict[IPAddress, Set[Router]]:
        """
        Builds a dictionary with the routers with the network as the key, and a set with the routers
        that belong to that network as values
        """
        networks: Dict[IPAddress, Set[Router]] = {}
        for router in self._routers:
            for interface in router.interfaces:
                network = interface.network.network
                if network not in networks:
                    networks[network] = set()
                networks[network].add(router)
        return networks
