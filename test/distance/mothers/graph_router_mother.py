from typing import List

from parser.value_objects.interface.interface import Interface
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName


class GraphRouterMother:
    @staticmethod
    def get_router_for_graph(
            interfaces: List[Interface],
            routing_table: List[RoutingTableEntry]) -> Router:
        return Router(
            sys_name=SysName("test-router"),
            interfaces=interfaces,
            routing_table=routing_table,
        )
