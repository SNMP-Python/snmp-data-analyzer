from __future__ import absolute_import

import os
from parser.ip_objects_converter import IPParser
from searcher.route_creator.route_creator import RouteCreator


class LinuxRouterCreator(RouteCreator):
    ROUTE_TEMPLATE = 'sudo ip route add {network} dev {interface}'

    def __init__(self, interface_name: str = 'tap0'):
        self.interface_name = interface_name

    def create_route_to(self, network: str, mask: str) -> None:
        network = str(IPParser.get_network_from(network, mask))
        route_command = self.ROUTE_TEMPLATE.format(network=network, interface=self.interface_name)
        LinuxRouterCreator._execute_command(route_command)

    @staticmethod
    def _execute_command(command: str) -> None:
        os.system(command)
