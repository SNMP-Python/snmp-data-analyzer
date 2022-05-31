from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException

from netaddr import AddrFormatError, IPAddress, IPNetwork


class IPParser:
    @staticmethod
    def get_network_from(ip_addr: str, mask: str) -> IPNetwork:
        try:
            network = IPNetwork(ip_addr)
        except AddrFormatError as error:
            raise InvalidIpException("Not a valid ip") from error
        try:
            network.netmask = mask
        except AddrFormatError as error:
            raise InvalidMaskException("Mask is not valid") from error
        return network

    @staticmethod
    def get_ip_address_from(ip_addr: str) -> IPAddress:
        try:
            return IPAddress(ip_addr)
        except AddrFormatError as error:
            raise InvalidIpException("Not a valid ip") from error
