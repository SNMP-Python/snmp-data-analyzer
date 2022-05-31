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
    ):
        self.sys_name = sys_name
        self.interfaces = interfaces
        self.routing_table = routing_table
