from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives


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

    @staticmethod
    def get_list_of_n_elements(
        ips_addresses: List[str], id_interface_init: int = 0, mask: str = "255.255.255.0"
    ) -> List[InterfacePrimitives]:
        result = []
        for ip_addr in ips_addresses:
            result.append(InterfacePrimitiveMother.get(ip=ip_addr, name=f"eth{id_interface_init}", mask=mask))
            id_interface_init += 1
        return result
