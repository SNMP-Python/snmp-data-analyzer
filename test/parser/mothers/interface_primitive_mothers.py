from typing import List

from searcher.interface_primitives import InterfacePrimitives


class InterfacePrimitiveMother:

    STATUS_UP = "up"
    STATUS_DOWN = "down"
    INCORRECT_STATUS = "incorrect status"

    @staticmethod
    def get(
        ip: str = "192.168.2.1",
        name: str = "eth0",
        status: str = STATUS_UP,
        speed: str = "25.2",
        mask: str = "255.255.255.0",
    ) -> InterfacePrimitives:
        return InterfacePrimitives(interface=name, ip_addr=ip, mask=mask, status=status, speed=speed)

    @staticmethod
    def get_list_of_one_element(
        ip: str = "192.168.2.1",
        name: str = "eth0",
        status: str = STATUS_UP,
        speed: str = "25.2",
        mask: str = "255.255.255.0",
    ) -> List[InterfacePrimitives]:
        return [InterfacePrimitiveMother.get(ip, name, status, speed, mask)]
