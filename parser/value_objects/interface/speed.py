from parser.exceptions.empty_speed_value import SpeedValueException


class SpeedInterface:
    """
    Encapsulates the speed of the interface in MBytes/second
    """
    FACTOR_DIVIDER = 1_000_000

    def __init__(self, value: str):
        if len(value) == 0:
            raise SpeedValueException("Speed Value is empty!")
        try:
            seconds = int(value)
            if seconds < 0:
                raise SpeedValueException("Value cannot be negative!")
            self.speed = seconds / SpeedInterface.FACTOR_DIVIDER
        except Exception as error:
            raise SpeedValueException(f"Value is not an integer! {value}") from error

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SpeedInterface):
            return NotImplemented
        return self.speed == other.speed

    def __str__(self) -> str:
        return f"Speed of the Interface is: {self.speed} MBytes/second"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(speed={self.speed})"

    def __hash__(self) -> int:
        return 13 * hash(self.speed)
