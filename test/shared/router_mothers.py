from typing import List

from parser.value_objects.interface.interface import Interface
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName
from test.shared.interface_mothers import InterfaceMother
from test.shared.routing_table_mother import RouterTableMother


class RouterMother:

    @staticmethod
    def get(
        sys_name: SysName = SysName("Router-Test"),
        interfaces: List[Interface] = [InterfaceMother.get()],
        routing_table: List[RoutingTableEntry] = [RouterTableMother.get()],
    ) -> Router:
        return Router(
            sys_name=sys_name,
            interfaces=interfaces,
            routing_table=routing_table
        )