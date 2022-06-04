from __future__ import absolute_import

from typing import FrozenSet, Set, Iterable, Tuple

from graph.router_node import RouterNode
from painter.edge import Edge
from parser.value_objects.router import Router


class GraphFacade:
    def __init__(self, graph: FrozenSet[RouterNode]):
        self.graph = graph

    def get_nodes_router(self) -> FrozenSet[str]:
        nodes = set()
        nodes.update([node.router.sys_name.name for node in self.graph])
        return frozenset(nodes)

    def get_nodes_networks(self) -> FrozenSet[str]:
        nodes = set()
        iterable = self._get_networks()
        nodes.update([network for network, _ in iterable])
        return frozenset(nodes)

    def _get_networks(self) -> Iterable[Tuple[str, str]]:
        for node in self.graph:
            yield from GraphFacade._get_networks_for_router(node.router)

    @staticmethod
    def _get_networks_for_router(router: Router) -> Iterable[Tuple[str, str]]:
        for interface in router.interfaces:
            yield f"{str(interface.network.network)}/{str(interface.network.netmask)}", f"{str(interface.network).split('/', maxsplit=1)[0]}"

    def get_edges(self) -> FrozenSet[Edge]:
        all_edges: Set[Edge] = set()
        for node in self.graph:
            for network, ip_router in GraphFacade._get_networks_for_router(node.router):
                edge = Edge(node.router.sys_name.name, network, ip_router)
                all_edges.add(edge)
        return frozenset(all_edges)
