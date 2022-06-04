from typing import List, Callable

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType
from parser.value_objects.router import Router


class InterfaceRemover:

    @staticmethod
    def remove_down_and_loopback(routers: List[Router]):
        InterfaceRemover._remove_interfaces(routers=routers,
                                            filter_strategy=lambda interface: interface.status != InterfaceStatus.DOWN)
        InterfaceRemover._remove_interfaces(routers=routers,
                                            filter_strategy=lambda
                                                interface: interface.type_interface != InterfaceType.LOOPBACK)

    @staticmethod
    def _remove_interfaces(filter_strategy: Callable[[Interface], bool], routers):
        for router in routers:
            new_interfaces: List[Interface] = []
            for interface in router.interfaces:
                if filter_strategy(interface):
                    new_interfaces.append(interface)
            router.interfaces = new_interfaces