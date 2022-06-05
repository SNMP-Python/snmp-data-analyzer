from netaddr import IPNetwork, IPAddress

from parser.value_objects.route_type import RouteType
from parser.value_objects.routing_table_entry import RoutingTableEntry


class GraphRoutingEntryMother:
    @staticmethod
    def get_routing_entry_for_graph(network_str: str, next_hop_str: str = '0.0.0.0') -> RoutingTableEntry:
        return RoutingTableEntry(
            network=IPNetwork(network_str),
            next_hop=IPAddress(next_hop_str),
            route_type=RouteType.DIRECT,
        )
