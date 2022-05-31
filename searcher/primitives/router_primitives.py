from __future__ import absolute_import

from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives


class RouterPrimitives:
    def __init__(
        self,
        sys_name: str,
        interfaces: List[InterfacePrimitives],
        routing_table: List[RoutePrimitives],
    ):
        self.sys_name = sys_name
        self.interfaces = interfaces
        self.routing_table = routing_table
