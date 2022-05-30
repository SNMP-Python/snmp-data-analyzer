from typing import List

from searcher.interface_primitives import InterfacePrimitives
from searcher.route_primitive import RoutePrimitive


class RouterPrimitives:
    def __init__(
        self,
        sys_name: str,
        interfaces: List[InterfacePrimitives],
        routing_table: List[RoutePrimitive],
    ):
        self.sys_name = sys_name
        self.interfaces = interfaces
        self.routing_table = routing_table
