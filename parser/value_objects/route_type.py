from enum import Enum


class RouteType(Enum):
    OTHER = 1
    INVALID = 2
    DIRECT = 3
    INDIRECT = 4

    @staticmethod
    def from_string(value: str) -> "RouteType":
        try:
            value_int = int(value)
            for route in RouteType:
                if route.value == value_int:
                    return route
            raise ValueError(f"Not found a Route Type with value: {value_int}")
        except Exception as error:
            raise ValueError("Value has to be an integer") from error
