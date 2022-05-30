from parser.value_objects.sys_name import SysName
from typing import List

from common.interface import Interface


class Router:
    def __init__(self, sys_name: SysName, interfaces: List[Interface]):
        self.sys_name = sys_name
        self.interfaces = interfaces
