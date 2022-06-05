from netaddr import IPNetwork

from parser.value_objects.interface.interface import Interface
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.interface.type import InterfaceType


class GraphInterfaceMother:
    @staticmethod
    def get_interface_for_graph(
        network_str: str,
    ) -> Interface:
        return Interface(
            network=IPNetwork(network_str),
            name=InterfaceName('eth0'),
            speed=SpeedInterface('100000'),
            status=InterfaceStatus.UP,
            type_interface=InterfaceType.NORMAL,
        )
