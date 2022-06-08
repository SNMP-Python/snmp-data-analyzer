from typing import List

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from parser.value_objects.router import Router
from test.distance.mothers.graph_interface_mother import GraphInterfaceMother
from test.distance.mothers.graph_router_mother import GraphRouterMother
from test.distance.mothers.graph_routing_entry_mother import (
    GraphRoutingEntryMother,
)


class TwoRoutersGraphMother:
    @classmethod
    def _get_first_router_second_test(cls) -> Router:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('6.0.0.1/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
        ]
        router = GraphRouterMother.get_router_for_graph(
            interfaces, routing_table
        )
        return router

    @classmethod
    def _get_second_router_second_test(cls) -> Router:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph("6.0.0.2/24"),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
        ]
        router = GraphRouterMother.get_router_for_graph(
            interfaces, routing_table, sys_name='test-router-2'
        )
        return router

    @classmethod
    def get_two_routers_one_interface_graph(cls) -> List[RouterNode]:
        first_router = cls._get_first_router_second_test()
        second_router = cls._get_second_router_second_test()
        return GraphCreatorImp([first_router, second_router]).get_graph()
