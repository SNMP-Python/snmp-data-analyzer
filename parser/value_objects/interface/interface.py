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
    ) -> None:
        self.network = network
        self.name = name
        self.speed = speed
        self.status = status

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(network={self.network}, name={self.name}, "
            f"speed={self.speed}, status={self.status})"
        )

    def __eq__(self, other):
        if not isinstance(other, Interface):
            return False

        return (
            self.network == other.network
            and self.name == other.name
            and self.speed == other.speed
            and self.status == other.status
        )

    def __hash__(self) -> int:
        return hash(self.network) + hash(self.name) + hash(self.speed) + hash(self.status)
