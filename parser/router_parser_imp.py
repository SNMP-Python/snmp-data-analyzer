from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from parser.router_parser import RouterParser
from parser.value_objects.interface.name import InterfaceName
from parser.value_objects.interface.speed import SpeedInterface
from parser.value_objects.interface.status import InterfaceStatus
from parser.value_objects.sys_name import SysName
from typing import List

from netaddr import AddrFormatError, IPNetwork

from common.interface import Interface
from common.router import Router
from searcher.interface_primitives import InterfacePrimitives
from searcher.router_primitives import RouterPrimitives


class RouterParserImp(RouterParser):
    def __init__(self, primitives: List[RouterPrimitives]):
        self.primitives = primitives

    def get_routers(self) -> List[Router]:
        return self._parse_from_primitives()

    def _parse_from_primitives(self) -> List[Router]:
        result = []
        for router_primitive in self.primitives:
            sys_name = SysName(router_primitive.sys_name)
            interfaces = RouterParserImp._get_interfaces_from(
                router_primitive.interfaces
            )
            result.append(Router(sys_name=sys_name, interfaces=interfaces))
        return result

    @staticmethod
    def _get_interfaces_from(interfaces_primitives: List[InterfacePrimitives]):
        interfaces: List[Interface] = []
        for interface in interfaces_primitives:
            try:
                network = IPNetwork(interface.ip_addr)
            except AddrFormatError as error:
                raise InvalidIpException("Not a valid ip") from error
            try:
                network.netmask = interface.mask
            except AddrFormatError as error:
                raise InvalidMaskException("Mask is not valid") from error
            interfaces.append(
                Interface(
                    network=network,
                    name=InterfaceName(interface.name),
                    speed=SpeedInterface(interface.speed),
                    status=InterfaceStatus.from_str(interface.status),
                )
            )
        return interfaces
