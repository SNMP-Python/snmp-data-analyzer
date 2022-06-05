from __future__ import absolute_import

from printer.logger import Logger
from searcher.route_creation.route_creator import RouteCreator

TAP0_ROUTE_TEMPLATE = 'sudo ip route add {network} dev {interface}'


class EmptyRouterCreator(RouteCreator):
    def __init__(self, logger: Logger):
        self.logger = logger

    def create_route_to(self, network: str, mask: str) -> None:
        self.logger.debug(f'Detected network {network} with mask {mask}. Skipping route creation.')
