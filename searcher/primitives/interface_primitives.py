class InterfacePrimitives:
    # pylint: disable=R0913 disable=C0301
    def __init__(
        self,
        interface: str,
        ip_addr: str,
        mask: str,
        status: str,
        speed: str,
        int_type: str,
    ):
        self.interface = interface
        self.ip_addr = ip_addr
        self.mask = mask
        self.status = status
        self.speed = speed
        self.int_type = int_type

    def __eq__(self, other):
        if not isinstance(other, InterfacePrimitives):
            return NotImplemented
        return (
            self.interface == other.interface
            and self.ip_addr == other.ip_addr
            and self.mask == other.mask
        )

    def __str__(self):
        return self.interface

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.interface) * hash(self.ip_addr) * hash(self.mask)
