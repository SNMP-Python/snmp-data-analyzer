from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.router import Router
from parser.value_objects.sys_name import SysName
from typing import List

from netaddr import IPNetwork


class RouterMother:
    @classmethod
    def get_one_router(cls) -> List[Router]:
        interfaces = [
            Interface(
                network=IPNetwork("10.0.0.1/8"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
        ]
        router = Router(sys_name=SysName("router-1"), interfaces=interfaces, routing_table=[])
        return [router]

    @classmethod
    def get_two_routers(cls) -> List[Router]:
        first_router = cls.get_one_router()[0]

        interfaces = [
            Interface(
                network=IPNetwork("10.0.0.2/8"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork("11.0.0.2/8"),
                name=InterfaceName("eth1"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
        ]
        second_router = Router(sys_name=SysName("router-2"), interfaces=interfaces, routing_table=[])
        return [first_router, second_router]
