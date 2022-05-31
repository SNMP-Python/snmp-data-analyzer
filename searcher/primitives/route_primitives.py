class RoutePrimitives:
    def __init__(self, network: str, mask: str, next_hop: str, route_type: str):
        self.network = network
        self.mask = mask
        self.next_hop = next_hop
        self.route_type = route_type
