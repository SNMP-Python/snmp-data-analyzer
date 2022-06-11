from __future__ import absolute_import

import sys
from typing import FrozenSet

from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from printer.logger import Logger
from printer.printer import Printer
from searcher.exceptions.mask_not_found import MaskNotFoundException
from searcher.exceptions.next_hop_not_found_exception import NextHopNotFoundException
from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.exceptions.ospf_id_not_available import OSPFIdNotAvailableException
from searcher.exceptions.route_creation import RouteCreationException
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.route_creation.route_creator import RouteCreator
from searcher.router_searcher import RouterSearcher
from searcher.snmp_router_searcher import SNMPRouterSearcher


class RouterSearcherFacade(RouterSearcher):
    """
    Class which adds log functionality and error handling for the class SNMPRouterSearcher
    """

    # pylint: disable=R0913
    def __init__(self, ip_addr: str, creator: RouteCreator, printer: Printer, logger: Logger, community: str):
        self.searcher: RouterSearcher = SNMPRouterSearcher(ip_addr=ip_addr, router_creator=creator, community=community)
        self.printer: Printer = printer
        self.logger: Logger = logger
        self.first_hop = ip_addr

    def get_router_primitives(self) -> FrozenSet[RouterPrimitives]:
        try:
            primitives: FrozenSet[RouterPrimitives] = self.searcher.get_router_primitives()
            self.printer.print_primitives(primitives)
            return primitives
        # The return type is necessary for mypy (python type checking)
        except InvalidIpException as error:
            self._show_error_and_exit(f"Searcher found an invalid ip: {error}")
        except InvalidMaskException as error:
            self._show_error_and_exit(f"Searcher found an invalid mask: {error}")
        except RouteCreationException as error:
            self._show_error_and_exit(f"Searcher got an error when executing add route: {error}")
        except MaskNotFoundException as error:
            self._show_error_and_exit(f"Searcher got an error when looking for mask: {error}")
        except NextHopNotFoundException as error:
            self._show_error_and_exit(f"Searcher got an error when looking for next hop: {error}")
        except NonReachableHostException as error:
            self._show_error_and_exit(f"Searcher couldn't find host: {error}")
        except OSPFIdNotAvailableException as error:
            self._show_error_and_exit(f"Searcher got an error when looking for OSPF ID: {error}")
        except Exception as error:  # pylint: disable=W0703
            self._show_error_and_exit(f"Searcher implementation error: {error}")
        return frozenset()

    def _show_error_and_exit(self, message: str) -> None:
        self.logger.error(message)
        sys.exit(-1)

    def get_first_hop(self) -> str:
        return self.first_hop
