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

from searcher.interface_primitives import InterfacePrimitives
from searcher.route_primitive import RoutePrimitive
from searcher.router_primitives import RouterPrimitives


class RouterParserImp(RouterParser):
    def __init__(self, primitives: List[RouterPrimitives]):
        self.primitives = primitives

    def get_routers(self) -> List[Router]:
        return self._parse_from_primitives()

    def _parse_from_primitives(self) -> List[Router]:
        result = []
        for router_primitive in self.primitives:
            sys_name = SysName(router_primitive.sys_name)
            interfaces = RouterParserImp._get_interfaces_from(
                router_primitive.interfaces
            )
            routing_table = RouterParserImp._get_routing_table_from(
                router_primitive.routing_table
            )
            result.append(
                Router(
                    sys_name=sys_name,
                    interfaces=interfaces,
                    routing_table=routing_table,
                )
            )
        return result

    @staticmethod
    def _get_interfaces_from(interfaces_primitives: List[InterfacePrimitives]):
        interfaces: List[Interface] = []
        for interface in interfaces_primitives:
            network = IPParser.get_network_from(interface.ip_addr, interface.mask)
            interfaces.append(
                Interface(
                    network=network,
                    name=InterfaceName(interface.name),
                    speed=SpeedInterface(interface.speed),
                    status=InterfaceStatus.from_str(interface.status),
                )
            )
        return interfaces

    @staticmethod
    def _get_routing_table_from(
        router_primitives: List[RoutePrimitive],
    ) -> List[RoutingTableEntry]:
        result = []
        for route in router_primitives:
            network = IPParser.get_network_from(route.network, route.mask)
            next_hop = IPParser.get_ip_address_from(route.next_hop)
            result.append(RoutingTableEntry(network=network, next_hop=next_hop))
        return result
