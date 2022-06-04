from netaddr import IPNetwork, IPAddress

from parser.value_objects.route_type import RouteType
from parser.value_objects.routing_table_entry import RoutingTableEntry


class RouterTableMother:

    @staticmethod
    def get(
    ) -> RoutingTableEntry:
        return RoutingTableEntry(
            network = IPNetwork("10.0.0.1/24"),
            next_hop = IPAddress("10.0.0.2"),
            route_type = RouteType.DIRECT
        )
