from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives


class InterfacePrimitiveMother:
    STATUS_UP = "1"
    STATUS_DOWN = "2"
    INCORRECT_STATUS = "5"

    @staticmethod
    def get(
        ip: str = "192.168.2.1",
        name: str = "eth0",
        status: str = STATUS_UP,
        speed: str = "2500000",
        mask: str = "255.255.255.0",
        int_type: str = "6",
    ) -> InterfacePrimitives:
        return InterfacePrimitives(
            interface=name,
            ip_addr=ip,
            mask=mask,
            status=status,
            speed=speed,
            int_type=int_type,
        )

    @staticmethod
    def get_list_of_one_element(
        ip: str = "192.168.2.1",
        name: str = "eth0",
        status: str = STATUS_UP,
        speed: str = "250000000",
        mask: str = "255.255.255.0",
        int_type: str = "6",
    ) -> List[InterfacePrimitives]:
        return [InterfacePrimitiveMother.get(ip, name, status, speed, mask, int_type)]

    @staticmethod
    def get_list_of_n_elements(
        ips_addresses: List[str],
        id_interface_init: int = 0,
        mask: str = "255.255.255.0",
    ) -> List[InterfacePrimitives]:
        result = []
        for ip_addr in ips_addresses:
            result.append(
                InterfacePrimitiveMother.get(
                    ip=ip_addr, name=f"eth{id_interface_init}", mask=mask
                )
            )
            id_interface_init += 1
        return result
