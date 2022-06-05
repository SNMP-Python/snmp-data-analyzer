from typing import FrozenSet

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from parser.value_objects.router import Router
from test.distance.mothers.graph_interface_mother import GraphInterfaceMother
from test.distance.mothers.graph_router_mother import GraphRouterMother
from test.distance.mothers.graph_routing_entry_mother import GraphRoutingEntryMother


class OneRouterGraphMother:
    @classmethod
    def get_one_router_one_interface_graph(cls) -> FrozenSet[RouterNode]:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('6.0.0.1/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
        ]
        router = GraphRouterMother.get_router_for_graph(interfaces, routing_table)
        return GraphCreatorImp([router]).get_graph()

    @classmethod
    def _get_one_router_three_interfaces(cls) -> Router:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('6.0.0.2/24'),
            GraphInterfaceMother.get_interface_for_graph('8.0.0.5/24'),
            GraphInterfaceMother.get_interface_for_graph('10.0.0.6/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('8.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('10.0.0.0/24'),
        ]
        router = GraphRouterMother.get_router_for_graph(interfaces, routing_table)
        return router

    @classmethod
    def get_one_router_three_interfaces_graph(cls) -> FrozenSet[RouterNode]:
        router = cls._get_one_router_three_interfaces()
        return GraphCreatorImp([router]).get_graph()
