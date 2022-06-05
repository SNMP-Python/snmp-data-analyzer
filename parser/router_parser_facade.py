import sys
from typing import FrozenSet, List

from parser.exceptions.empty_interface_name import EmptyInterfaceNameException
from parser.exceptions.empty_speed_value import SpeedValueException
from parser.exceptions.empty_sys_name import EmptySysNameException
from parser.exceptions.interface_type import InterfaceTypeException
from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from parser.exceptions.route_type import RouteTypeException
from parser.exceptions.status_value_exception import StatusValueException
from parser.router_parser import RouterParser
from parser.router_parser_imp import RouterParserImp
from parser.value_objects.router import Router
from printer.logger import Logger
from printer.printer import Printer
from searcher.primitives.router_primitives import RouterPrimitives


class RouterParserFacade(RouterParser):
    """
    Class which adds log functionality and error handling for the class RouterParserImplementation
    """

    def __init__(self, printer: Printer, logger: Logger, routers_primitives: FrozenSet[RouterPrimitives]):
        self.printer = printer
        self.logger = logger
        self.parser = RouterParserImp(routers_primitives)

    def get_routers(self) -> List[Router]:
        try:
            routers: List[Router] = self.parser.get_routers()
            self.printer.print_routers(frozenset(routers))
            return routers
        except EmptyInterfaceNameException as error:
            self._show_error_and_exit(f"Parser found an interface which had an invalid name: {error}")
        except SpeedValueException as error:
            self._show_error_and_exit(f"Parser found an invalid speed: {error}")
        except EmptySysNameException as error:
            self._show_error_and_exit(f"Parser found an invalid sys name: {error}")
        except InvalidIpException as error:
            self._show_error_and_exit(f"Parser found an invalid ip: {error}")
        except InvalidMaskException as error:
            self._show_error_and_exit(f"Parser found an invalid mask: {error}")
        except StatusValueException as error:
            self._show_error_and_exit(f"Parser found an invalid interface status: {error}")
        except InterfaceTypeException as error:
            self._show_error_and_exit(f"Parser found an invalid interface type: {error}")
        except RouteTypeException as error:
            self._show_error_and_exit(f"Parser found an invalid route type: {error}")
        except Exception as error:  # pylint: disable=W0703
            self._show_error_and_exit(f"Parser implementation error: {error}")
        return []

    def _show_error_and_exit(self, message: str) -> None:
        """
        After this function is called, the python process will be killed.
        The return type is necessary for mypy (python type checking)
        """
        self.logger.error(message)
        sys.exit(-1)
