from __future__ import absolute_import

from parser.ip_objects_converter import IPParser
from parser.router_parser import RouterParser
from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName
from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives
from searcher.primitives.router_primitives import RouterPrimitives


class RouterParserImp(RouterParser):
    def __init__(self, primitives: List[RouterPrimitives]):
        self.primitives = primitives

    def get_routers(self) -> List[Router]:
        return list(map(RouterParserImp._get_router_from, self.primitives))

    @staticmethod
    def _get_router_from(router: RouterPrimitives) -> Router:
        return Router(
            sys_name=SysName(router.sys_name),
            interfaces=RouterParserImp._get_interfaces_from(router.interfaces),
            routing_table=RouterParserImp._get_routing_table_from(router.routing_table),
        )

    @staticmethod
    def _get_interfaces_from(
        interfaces_primitives: List[InterfacePrimitives],
    ) -> List[Interface]:
        return list(map(RouterParserImp._get_interface_from_primitive, interfaces_primitives))

    @staticmethod
    def _get_routing_table_from(
        router_primitives: List[RoutePrimitives],
    ) -> List[RoutingTableEntry]:
        return list(
            map(
                RouterParserImp._get_routing_table_entry_from_primitive,
                router_primitives,
            )
        )

    @staticmethod
    def _get_interface_from_primitive(interface: InterfacePrimitives) -> Interface:
        network = IPParser.get_network_from(interface.ip_addr, interface.mask)
        return Interface(
            network=network,
            name=InterfaceName(interface.interface),
            speed=SpeedInterface(interface.speed),
            status=InterfaceStatus.from_str(interface.status),
        )

    @staticmethod
    def _get_routing_table_entry_from_primitive(
        route_primitive: RoutePrimitives,
    ) -> RoutingTableEntry:
        network = IPParser.get_network_from(route_primitive.network, route_primitive.mask)
        next_hop = IPParser.get_ip_address_from(route_primitive.next_hop)
        return RoutingTableEntry(network=network, next_hop=next_hop)
