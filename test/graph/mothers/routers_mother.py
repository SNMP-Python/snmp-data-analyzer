from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.router import Router
from parser.value_objects.sys_name import SysName
from typing import Tuple

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
    def get_two_routers_in_cycle(cls) -> Tuple[Router, Router]:
        """
                (eth0) .1     *10.0.0.0/8*    .2 (eth0)
                     R1 ----------------------- R2
        *12.0.0.1/8*  |                          | *11.0.0.2/8*
            (eth1)    |                          |   (eth1)


        """
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
    def get_three_routers_in_cycle(cls) -> Tuple[Router, ...]:
        """
                           *10.0.0.0/8*
                (eth0) .1               .2 (eth0)
                     R1 ----------------- R2
           (eth1) .1 |                     | .2  (eth1)
                     |                     |
        *12.0.0.0/8* --------  R3 ----------  *11.0.0.0/8*
                   (eth1)  .2     .1  (eth0)
        """
        first_router, second_router = cls.get_two_routers_in_cycle()

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

    @classmethod
    def get_three_routers_without_cycle(cls) -> Tuple[Router, ...]:
        """
        .1   *10.0.0.0/8*   .2   .2   *11.0.0.0/8*    .1
        R1 ------------------- R2 ------------------- R3
        """
        first_router, second_router = cls.get_two_routers_in_cycle()

        interfaces = [
            Interface(
                network=IPNetwork("11.0.0.1/8"),
                name=InterfaceName("eth0"),
                speed=SpeedInterface("25.2"),
                status=InterfaceStatus.UP,
            )
        ]
        third_router = Router(sys_name=SysName("router-3"), interfaces=interfaces, routing_table=[])
        return first_router, second_router, third_router
