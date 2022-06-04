from typing import List

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType
from parser.value_objects.router import Router


class InterfaceRemover:

    @staticmethod
    def remove_down_and_loopback(routers: List[Router]):
        InterfaceRemover._remove_down_interfaces(routers)
        InterfaceRemover._remove_loopback_interfaces(routers)


    @staticmethod
    def _remove_down_interfaces(routers: List[Router]):
        for router in routers:
            new_interfaces: List[Interface] = []
            for interface in router.interfaces:
                if interface.status != InterfaceStatus.DOWN:
                    new_interfaces.append(interface)
            router.interfaces = new_interfaces

    @staticmethod
    def _remove_loopback_interfaces(routers: List[Router]):
        for router in routers:
            new_interfaces: List[Interface] = []
            for interface in router.interfaces:
                if interface.type_interface != InterfaceType.LOOPBACK:
                    new_interfaces.append(interface)
            router.interfaces = new_interfaces
