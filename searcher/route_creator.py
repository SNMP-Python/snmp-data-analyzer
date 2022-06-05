from __future__ import absolute_import

import os

TAP0_ROUTE_TEMPLATE = 'sudo ip route add {network} dev tap0'


class RouteCreator:
    @staticmethod
    def create_tap0_route_to(network: str) -> None:
        route_command = TAP0_ROUTE_TEMPLATE.format(network=network)
        RouteCreator._execute_command(route_command)

    @staticmethod
    def _execute_command(command: str) -> None:
        os.system(command)
