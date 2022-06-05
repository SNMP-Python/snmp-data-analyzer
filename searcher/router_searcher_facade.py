from __future__ import absolute_import

import sys
from typing import FrozenSet

from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from printer.logger import Logger
from printer.printer import Printer
from searcher.exceptions.route_creation import RouteCreationException
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.route_creation.route_creator import RouteCreator
from searcher.router_searcher import RouterSearcher
from searcher.snmp_router_searcher import SNMPRouterSearcher


class RouterSearcherFacade(RouterSearcher):
    """
    Class which adds log functionality and error handling for the class SNMPRouterSearcher
    """

    def __init__(self, ip_addr: str, creator: RouteCreator, printer: Printer, logger: Logger):
        self.searcher: RouterSearcher = SNMPRouterSearcher(ip_addr=ip_addr, router_creator=creator)
        self.printer: Printer = printer
        self.logger: Logger = logger

    def get_router_primitives(self) -> FrozenSet[RouterPrimitives]:
        try:
            primitives: FrozenSet[RouterPrimitives] = self.searcher.get_router_primitives()
            self.printer.print_primitives(primitives)
            return primitives
        # The return type is necessary for mypy (python type checking)
        except InvalidIpException as error:
            self._show_error_and_exit(f"Searcher found an invalid ip: {error}")
            return frozenset()
        except InvalidMaskException as error:
            self._show_error_and_exit(f"Searcher found an invalid mask: {error}")
            return frozenset()
        except RouteCreationException as error:
            self._show_error_and_exit(f"Searcher got an error when executing add route: {error}")
            return frozenset()
        except Exception as error:  # pylint: disable=W0703
            self._show_error_and_exit(f"Searcher implementation error: {error}")
            return frozenset()

    def _show_error_and_exit(self, message: str) -> None:
        self.logger.error(message)
        sys.exit(-1)
