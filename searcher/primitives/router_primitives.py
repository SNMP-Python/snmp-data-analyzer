from __future__ import absolute_import

from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives


class RouterPrimitives:
    # pylint: disable=R0913
    def __init__(
        self,
        sys_name: str,
        interfaces: List[InterfacePrimitives],
        routing_table: List[RoutePrimitives],
        ospf_id: str,
        # pylint: disable W0102
        neighbors: List[str] = [],
    ):
        self.sys_name = sys_name
        self.interfaces = interfaces
        self.routing_table = routing_table
        self.neighbors = neighbors
        self.ospf_id = ospf_id

    def __eq__(self, other) -> bool:
        if not isinstance(other, RouterPrimitives):
            return NotImplemented
        return self.sys_name == other.sys_name

    def __str__(self) -> str:
        return f"Name: {self.sys_name} with id of ospf: {self.ospf_id}"

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self):
        return self.ospf_id.__hash__() * self.sys_name.__hash__()
