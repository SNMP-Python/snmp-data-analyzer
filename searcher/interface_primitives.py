class InterfacePrimitives:
    # pylint: disable=R0913
    def __init__(self, interface: str, ip_addr: str, mask: str, status: str, speed: str):
        self.interface = interface
        self.ip_addr = ip_addr
        self.mask = mask
        self.status = status
        self.speed = speed
