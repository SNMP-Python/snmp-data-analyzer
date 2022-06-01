from parser.exceptions.empty_speed_value import SpeedValueException


class SpeedInterface:
    """
    Encapsulates the speed of the interface in MBytes/second
    """

    def __init__(self, value: str):
        if len(value) == 0:
            raise SpeedValueException("Speed Value is empty!")
        try:
            self.speed = float(value)
            if self.speed < 0:
                raise SpeedValueException("Value cannot be negative!")
        except Exception as error:
            raise SpeedValueException(f"Value is not a float! {value}") from error

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpeedInterface):
            return NotImplemented
        return self.speed == other.speed

    def __str__(self) -> str:
        return f"Speed of the Interface is: {self.speed} MBytes/second"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(speed={self.speed})"
