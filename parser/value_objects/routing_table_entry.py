from netaddr import IPAddress, IPNetwork


class RoutingTableEntry:
    def __init__(self, network: IPNetwork, next_hop: IPAddress):
        self.network = network
        self.next_hop = next_hop

    def __eq__(self, other) -> bool:
        if not isinstance(other, RoutingTableEntry):
            return NotImplemented
        return self.network == other.network and self.next_hop == other.next_hop

    def __hash__(self):
        return hash(self.network) + hash(self.next_hop)
