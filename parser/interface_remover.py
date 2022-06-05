from typing import List, Callable, Optional

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType
from parser.value_objects.router import Router
from printer.logger import Logger


class InterfaceRemover:
    @staticmethod
    def remove_down_and_loopback(routers: List[Router], logger: Optional[Logger] = None):
        InterfaceRemover._remove_interfaces(
            routers=routers, filter_strategy=lambda interface: interface.status != InterfaceStatus.DOWN, logger=logger
        )
        InterfaceRemover._remove_interfaces(
            routers=routers,
            filter_strategy=lambda interface: interface.type_interface != InterfaceType.LOOPBACK,
            logger=logger,
        )

    @staticmethod
    def _remove_interfaces(
        filter_strategy: Callable[[Interface], bool], routers: List[Router], logger: Optional[Logger] = None
    ):
        for router in routers:
            new_interfaces: List[Interface] = []
            for interface in router.interfaces:
                if filter_strategy(interface):
                    new_interfaces.append(interface)
                elif logger is not None:
                    logger.debug(f"Pruned interface: {interface} from router: {router.sys_name.name}")
            router.interfaces = new_interfaces
