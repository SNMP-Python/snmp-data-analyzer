class RoutePrimitives:
    def __init__(self, network: str, mask: str, next_hop: str, route_type: str):
        self.network = network
        self.mask = mask
        self.next_hop = next_hop
        self.route_type = route_type

    def __eq__(self, other):
        if not isinstance(other, RoutePrimitives):
            return NotImplemented
        # pylint: disable=C0301
        return (
            self.network == other.network
            and self.mask == other.mask
            and self.next_hop == other.next_hop
        )

    def __str__(self):
        return (
            self.network + " " + self.mask + " " + self.next_hop + " " + self.route_type
        )

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.network) * hash(self.mask) * hash(self.next_hop)
