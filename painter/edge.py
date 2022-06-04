class Edge:
    def __init__(self, router: str, network: str, ip_host: str):
        self.router = router
        self.network = network
        self.ip_host = ip_host

    def __eq__(self, other) -> bool:
        if not isinstance(other, Edge):
            return False
        return self.router == other.router and other.network == self.network

    def __hash__(self):
        return hash(self.router) + hash(self.network)
