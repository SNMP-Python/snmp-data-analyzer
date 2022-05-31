from typing import List

from searcher.primitives.route_primitives import RoutePrimitives


class RoutePrimitiveMother:
    @staticmethod
    def get(
        network: str = "10.0.0.0",
        mask: str = "255.255.0.0",
        next_hop: str = "10.0.0.2",
        route_type: str = "ospf",
    ) -> RoutePrimitives:
        return RoutePrimitives(network, mask, next_hop, route_type)

    @staticmethod
    def get_list_of_one_route(
        network: str = "10.0.0.0",
        mask: str = "255.255.0.0",
        next_hop: str = "10.0.0.2",
        route_type: str = "ospf",
    ) -> List[RoutePrimitives]:
        return [RoutePrimitiveMother.get(network, mask, next_hop, route_type)]
