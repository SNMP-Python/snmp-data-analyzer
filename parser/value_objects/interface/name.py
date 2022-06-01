from parser.exceptions.empty_interface_name import EmptyInterfaceNameException


class InterfaceName:
    def __init__(self, name: str):
        if len(name) == 0:
            raise EmptyInterfaceNameException("Interface name cannot be empty!")
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, InterfaceName):
            return NotImplemented
        return self.name == other.name

    def __str__(self) -> str:
        return f"Interface Name: {self.name}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name})"
