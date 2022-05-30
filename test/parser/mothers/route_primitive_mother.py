from typing import List

from searcher.route_primitive import RoutePrimitive


class RoutePrimitiveMother:
    @staticmethod
    def get(
        network: str = "10.0.0.0",
        mask: str = "255.255.0.0",
        next_hop: str = "10.0.0.2",
        route_type: str = "ospf",
    ) -> RoutePrimitive:
        return RoutePrimitive(network, mask, next_hop, route_type)

    @staticmethod
    def get_list_of_one_route() -> List[RoutePrimitive]:
        return [RoutePrimitiveMother.get()]
