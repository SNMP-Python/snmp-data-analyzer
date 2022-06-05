import random
from typing import List

from parser.value_objects.interface.interface import Interface
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName


class GraphRouterMother:
    @staticmethod
    def get_router_for_graph(
            interfaces: List[Interface],
            routing_table: List[RoutingTableEntry],
            sys_name: str = 'router-test') -> Router:
        return Router(
            sys_name=SysName(sys_name),
            interfaces=interfaces,
            routing_table=routing_table,
        )
