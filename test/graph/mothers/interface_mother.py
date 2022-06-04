from netaddr import IPNetwork

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType


class InterfaceMother:
    @classmethod
    def get(
        cls,
        ip_network: str,
        interface_name: str,
        speed: str = "100000000",
        status: InterfaceStatus = InterfaceStatus.UP,
        type_interface: InterfaceType = InterfaceType.NORMAL,
    ) -> Interface:
        return Interface(
            network=IPNetwork(ip_network),
            name=InterfaceName(interface_name),
            speed=SpeedInterface(speed),
            status=status,
            type_interface=type_interface,
        )
