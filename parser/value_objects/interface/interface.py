from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus

from netaddr import IPNetwork


class Interface:
    def __init__(
        self,
        network: IPNetwork,
        name: InterfaceName,
        speed: SpeedInterface,
        status: InterfaceStatus,
    ):
        self.network = network
        self.name = name
        self.speed = speed
        self.status = status
