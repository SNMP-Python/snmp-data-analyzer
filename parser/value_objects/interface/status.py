from enum import Enum, auto
from parser.exceptions.status_value_exception import StatusValueException


class InterfaceStatus(Enum):
    UP = auto()
    DOWN = auto()

    @staticmethod
    def from_str(value: str) -> "InterfaceStatus":
        if value == "up":
            return InterfaceStatus.UP
        if value == "down":
            return InterfaceStatus.DOWN
        raise StatusValueException(
            f"Value {value} cannot be converted to Interface Status"
        )
