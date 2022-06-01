from parser.value_objects.interface.interface import Interface
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName
from typing import List


class Router:
    def __init__(
        self,
        sys_name: SysName,
        interfaces: List[Interface],
        routing_table: List[RoutingTableEntry],
    ) -> None:
        self.sys_name = sys_name
        self.interfaces = interfaces
        self.routing_table = routing_table

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(sys_name={self.sys_name}, "
            f"interfaces={self.interfaces}, routing_table={self.routing_table})"
        )

    def __eq__(self, other):
        if not isinstance(other, Router):
            return False
        return (
            self.sys_name == other.sys_name
            and self.interfaces == other.interfaces
            and self.routing_table == other.routing_table
        )

    def __hash__(self) -> int:
        return hash(self.sys_name) + sum(hash(interface) for interface in self.interfaces)
