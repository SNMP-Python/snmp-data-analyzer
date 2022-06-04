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


class OneRouterGraphMother:
    @classmethod
    def get_one_router_one_interface_graph(cls) -> FrozenSet[RouterNode]:
        interfaces = [
            Interface(
                network=IPNetwork("6.0.0.1/24"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            )
        ]
        routing_table = [
            RoutingTableEntry(
                network=IPNetwork('6.0.0.0/24'),
                next_hop=IPAddress('0.0.0.0'),
            ),
        ]
        router = Router(sys_name=SysName("router-1"), interfaces=interfaces, routing_table=routing_table)
        return GraphCreatorImp([router]).get_graph()

    @classmethod
    def _get_one_router_three_interfaces(cls) -> Router:
        interfaces = [
            Interface(
                network=IPNetwork('6.0.0.2/24'),
                name=InterfaceName('eth0'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork('8.0.0.5/24'),
                name=InterfaceName('eth1'),
                speed=SpeedInterface('25.2'),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork('10.0.0.6/24'),
                name=InterfaceName('eth2'),
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
                next_hop=IPAddress('0.0.0.0'),
            ),
        ]
        router = Router(sys_name=SysName("router-1"), interfaces=interfaces, routing_table=routing_table)
        return router

    @classmethod
    def get_one_router_three_interfaces_graph(cls) -> FrozenSet[RouterNode]:
        router = cls._get_one_router_three_interfaces()
        return GraphCreatorImp([router]).get_graph()
