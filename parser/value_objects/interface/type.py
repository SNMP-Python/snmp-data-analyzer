from enum import Enum


class InterfaceType(Enum):
    NORMAL = 0
    LOOPBACK = 24

    @staticmethod
    def from_string(value: str) -> "InterfaceType":
        try:
            int_value = int(value)
            if int_value == InterfaceType.LOOPBACK.value:
                return InterfaceType.LOOPBACK
            return InterfaceType.NORMAL
        except Exception as error:
            raise ValueError("Interface type has to be a number") from error
