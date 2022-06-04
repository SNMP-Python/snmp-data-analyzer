from typing import List, Tuple

from netaddr import IPNetwork

from parser.value_objects.interface.interface import Interface
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from parser.value_objects.sys_name import SysName
from test.shared.interface_mothers import InterfaceMother


class RouterMother:
    @classmethod
    def get(cls, sys_name, interfaces: List[Interface] = None, routing_table: List[RoutingTableEntry] = None) -> Router:
        interfaces = interfaces or []
        routing_table = routing_table or []
        return Router(sys_name=sys_name, interfaces=interfaces, routing_table=routing_table)

    @classmethod
    def get_one_router(cls) -> Router:
        interfaces = [
            InterfaceMother.get(network=IPNetwork("10.0.0.1/8")),
            InterfaceMother.get(network=IPNetwork("12.0.0.1/8")),
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
            InterfaceMother.get(network=IPNetwork("10.0.0.2/8")),
            InterfaceMother.get(network=IPNetwork("11.0.0.2/8")),
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
            InterfaceMother.get(network=IPNetwork("11.0.0.1/8")),
            InterfaceMother.get(network=IPNetwork("12.0.0.2/8")),
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

        interfaces = [InterfaceMother.get(network=IPNetwork("11.0.0.1/8"))]
        third_router = Router(sys_name=SysName("router-3"), interfaces=interfaces, routing_table=[])
        return first_router, second_router, third_router

    @classmethod
    def get_four_routers_in_cycle(cls) -> Tuple[Router, ...]:
        first_router, second_router, third_router = cls.get_three_routers_in_cycle()

        interfaces = [
            InterfaceMother.get(network=IPNetwork("13.0.0.2/8")),
            InterfaceMother.get(network=IPNetwork("14.0.0.2/8")),
        ]
        second_router.interfaces.append(InterfaceMother.get(network=IPNetwork("13.0.0.1/8")))
        third_router.interfaces.append(InterfaceMother.get(network=IPNetwork("14.0.0.1/8")))
        fourth_router = Router(sys_name=SysName("router-4"), interfaces=interfaces, routing_table=[])
        return first_router, second_router, third_router, fourth_router

    @classmethod
    def get_four_routers_in_three_networks(cls) -> Tuple[Router, ...]:
        first_router, second_router, third_router = cls.get_three_routers_in_cycle()

        interfaces = [InterfaceMother.get(network=IPNetwork("10.0.0.3/8"))]

        fourth_router = Router(sys_name=SysName("router-4"), interfaces=interfaces, routing_table=[])
        return first_router, second_router, third_router, fourth_router
