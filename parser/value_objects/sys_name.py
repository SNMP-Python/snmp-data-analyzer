from parser.exceptions.empty_sys_name import EmptySysNameException


class SysName:
    def __init__(self, name: str):
        if len(name) == 0:
            raise EmptySysNameException("System Name cannot be empty!")
        self.name = name

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SysName):
            return NotImplemented
        return self.name == other.name

    def __str__(self) -> str:
        return f"System Name: {self.name}"
