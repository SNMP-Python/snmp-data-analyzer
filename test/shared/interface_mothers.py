from netaddr import IPNetwork

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType


class InterfaceMother:

    @staticmethod
    def get_interface_with_status(status: InterfaceStatus) -> Interface:
        return InterfaceMother.get(status=status)

    @staticmethod
    def get_interface_with_type(type: InterfaceType) -> Interface:
        return InterfaceMother.get(type_interface=type)

    @staticmethod
    def get(
            network=IPNetwork("10.0.0.0/24"),
            name=InterfaceName("Test-Router"),
            speed=SpeedInterface("1000000"),
            status=InterfaceStatus.UP,
            type_interface=InterfaceType.NORMAL
    ) -> Interface:
        return Interface(
            network=network,
            name=name,
            speed=speed,
            status=status,
            type_interface=type_interface
        )
