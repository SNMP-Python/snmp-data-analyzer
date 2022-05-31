from enum import Enum
from parser.exceptions.status_value_exception import StatusValueException


class InterfaceStatus(Enum):
    UP = 1
    DOWN = 2

    @staticmethod
    def from_str(value: str) -> "InterfaceStatus":
        try:
            integer_value = int(value)
            if integer_value == InterfaceStatus.UP.value:
                return InterfaceStatus.UP
            if integer_value == InterfaceStatus.DOWN.value:
                return InterfaceStatus.DOWN
            raise StatusValueException(
                f"Value {value} cannot be converted to Interface Status"
            )
        except Exception as error:
            raise StatusValueException(
                f"Value {value} cannot be converted to integer"
            ) from error
