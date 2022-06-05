from __future__ import absolute_import

from typing import Optional

from printer.logger import Logger
from searcher.route_creation.route_creator import RouteCreator

TAP0_ROUTE_TEMPLATE = 'sudo ip route add {network} dev {interface}'


class EmptyRouterCreator(RouteCreator):
    def __init__(self, logger: Optional[Logger] = None):
        self.logger = logger

    def create_route_to(self, network: str, mask: str) -> None:
        if self.logger:
            self.logger.debug(
                f'Detected network {network} with mask {mask}. Skipping route creation. '
                + 'If you want to add the new routes to the routing table add the -a flag'
            )
