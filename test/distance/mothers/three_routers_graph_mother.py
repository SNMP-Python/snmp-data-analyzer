from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName
from typing import FrozenSet

from netaddr import IPAddress, IPNetwork

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode


class ThreeRoutersGraphMother:
    @classmethod
    def _get_first_router_third_test(cls):
        interfaces = [
            Interface(
                network=IPNetwork('6.0.0.2/24'),
                name=InterfaceName('eth0'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork('8.0.0.4/24'),
                name=InterfaceName('eth1'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
        ]
        routing_table = [
            RoutingTableEntry(
                network=IPNetwork('6.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('8.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('10.0.0.0/24'),
                next_hop=IPAddress('6.0.0.4'),
            ),
        ]
        router = Router(sys_name=SysName("router-1"), interfaces=interfaces, routing_table=routing_table)
        return router

    @classmethod
    def _get_second_router_third_test(cls) -> Router:
        interfaces = [
            Interface(
                network=IPNetwork('6.0.0.4/24'),
                name=InterfaceName('eth0'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork('10.0.0.8/24'),
                name=InterfaceName('eth1'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
        ]
        routing_table = [
            RoutingTableEntry(
                network=IPNetwork('6.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('10.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('8.0.0.0/24'),
                next_hop=IPAddress('10.0.0.10'),
            ),
        ]
        router = Router(sys_name=SysName("router-2"), interfaces=interfaces, routing_table=routing_table)
        return router

    @classmethod
    def _get_third_router_third_test(cls) -> Router:
        interfaces = [
            Interface(
                network=IPNetwork('10.0.0.10/24'),
                name=InterfaceName('eth0'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork('8.0.0.6/24'),
                name=InterfaceName('eth1'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
        ]
        routing_table = [
            RoutingTableEntry(
                network=IPNetwork('10.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('8.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
            RoutingTableEntry(
                network=IPNetwork('6.0.0.0/24'),
                next_hop=IPAddress('8.0.0.4'),
            ),
        ]
        router = Router(sys_name=SysName("router-3"), interfaces=interfaces, routing_table=routing_table)
        return router

    @classmethod
    def get_three_routers_one_interface_graph(cls) -> FrozenSet[RouterNode]:
        first_router = cls._get_first_router_third_test()
        second_router = cls._get_second_router_third_test()
        third_router = cls._get_third_router_third_test()
        return GraphCreatorImp([first_router, second_router, third_router]).get_graph()
