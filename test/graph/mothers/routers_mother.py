from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.router import Router
from parser.value_objects.sys_name import SysName
from typing import List, Tuple

from netaddr import IPNetwork


class RouterMother:
    @classmethod
    def get_one_router(cls) -> Router:
        interfaces = [
            Interface(
                network=IPNetwork("10.0.0.1/8"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork("12.0.0.1/8"),
                name=InterfaceName("eth1"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
        ]
        router = Router(sys_name=SysName("router-1"), interfaces=interfaces, routing_table=[])
        return router

    @classmethod
    def get_two_routers(cls) -> Tuple[Router, Router]:
        first_router = cls.get_one_router()

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
        return first_router, second_router

    @classmethod
    def get_three_routers(cls) -> Tuple[Router, ...]:
        first_router, second_router = cls.get_two_routers()

        interfaces = [
            Interface(
                network=IPNetwork("11.0.0.1/8"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
            Interface(
                network=IPNetwork("12.0.0.2/8"),
                name=InterfaceName("eth1"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            ),
        ]
        third_router = Router(sys_name=SysName("router-3"), interfaces=interfaces, routing_table=[])
        return first_router, second_router, third_router
