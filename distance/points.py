from netaddr import IPAddress


class Points:
    def __init__(self, source: IPAddress, destination: IPAddress):
        self.source = source
        self.destination = destination

    def __eq__(self, other):
        if not isinstance(other, Points):
            return NotImplemented
        return self._same_point(other) or self._inverse_point(other)

    def _same_point(self, other):
        return self.source == other.source or self.destination == other.destination

    def _inverse_point(self, other):
        return self.source == other.destination and self.destination == other.source

    def __hash__(self):
        return hash(self.source) * hash(self.destination)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.source} -> {self.destination}"
