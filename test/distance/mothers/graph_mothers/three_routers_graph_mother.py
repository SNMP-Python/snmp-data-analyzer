from typing import FrozenSet

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from parser.value_objects.router import Router
from test.distance.mothers.graph_interface_mother import GraphInterfaceMother
from test.distance.mothers.graph_router_mother import GraphRouterMother
from test.distance.mothers.graph_routing_entry_mother import GraphRoutingEntryMother


class ThreeRoutersGraphMother:
    @classmethod
    def _get_first_router_third_test(cls):
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('6.0.0.2/24'),
            GraphInterfaceMother.get_interface_for_graph('8.0.0.4/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('8.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('10.0.0.0/24', '6.0.0.4'),
        ]
        router = GraphRouterMother.get_router_for_graph(interfaces, routing_table)
        return router

    @classmethod
    def _get_second_router_third_test(cls) -> Router:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('6.0.0.4/24'),
            GraphInterfaceMother.get_interface_for_graph('10.0.0.8/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('10.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('8.0.0.0/24', '10.0.0.10'),
        ]
        router = GraphRouterMother.get_router_for_graph(interfaces, routing_table, sys_name='test-router-2')
        return router

    @classmethod
    def _get_third_router_third_test(cls) -> Router:
        interfaces = [
            GraphInterfaceMother.get_interface_for_graph('8.0.0.6/24'),
            GraphInterfaceMother.get_interface_for_graph('10.0.0.10/24'),
        ]
        routing_table = [
            GraphRoutingEntryMother.get_routing_entry_for_graph('8.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('10.0.0.0/24'),
            GraphRoutingEntryMother.get_routing_entry_for_graph('6.0.0.0/24', '8.0.0.4'),
        ]
        router = GraphRouterMother.get_router_for_graph(interfaces, routing_table, sys_name='test-router-3')
        return router

    @classmethod
    def get_three_routers_one_interface_graph(cls) -> FrozenSet[RouterNode]:
        first_router = cls._get_first_router_third_test()
        second_router = cls._get_second_router_third_test()
        third_router = cls._get_third_router_third_test()
        return GraphCreatorImp([first_router, second_router, third_router]).get_graph()
