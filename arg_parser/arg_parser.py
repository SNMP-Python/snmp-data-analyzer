from __future__ import absolute_import

from argparse import ArgumentParser
from typing import Optional, Tuple, List

from printer.file_logger import FileLogger
from printer.logger import Logger
from printer.printer import Printer
from printer.printer_imp import PrinterImp
from printer.stdout_logger import StdoutLogger
from searcher.route_creation.empty_route_creator import EmptyRouterCreator
from searcher.route_creation.linux_route_creator import LinuxRouterCreator
from searcher.router_searcher import RouterSearcher
from searcher.router_searcher_facade import RouterSearcherFacade

IP_FLAG = 'ip'
OUTPUT_FILE_FLAG = 'output'
COMMUNITY_FLAG = 'community'
ADD_ROUTES_FLAG = 'add_routes'
DEBUG_FLAG = 'debug'

DEFAULT_COMMUNITY = 'rocom'


class ArgParser:

    @staticmethod
    def _parse_args(args: Optional[List[str]]) -> Tuple[Optional[str], Optional[str], Optional[str], bool, bool]:
        """
        Returns a tuple which includes:
        ip_address or None, output file or None, community or None, add routes boolean, debug boolean
        """
        parser = ArgParser._get_parser()
        arguments = parser.parse_args(args=args).__dict__
        return arguments[IP_FLAG], arguments[OUTPUT_FILE_FLAG], arguments[COMMUNITY_FLAG], arguments[ADD_ROUTES_FLAG], \
               arguments[DEBUG_FLAG]

    @staticmethod
    def _get_parser() -> ArgumentParser:
        parser = ArgumentParser(
            description='A program that analyzes the network by asking cisco routers using the snmp protocol.'
        )
        return ArgParser._add_flags(parser)

    @staticmethod
    def _add_flags(parser: ArgumentParser) -> ArgumentParser:
        parser.add_argument('-i', '--ip', type=str, help='The ip address of the router.')
        parser.add_argument('-o', '--output', type=str, help='The output file.')
        parser.add_argument('-a', '--add-routes', action='store_true', help='Adds needed routes to perform snmp polls.')
        parser.add_argument('-c', '--community', type=str, help='The community password for the agent')
        parser.add_argument('-d', '--debug', action='store_true',
                            help='Show messages that are created from developers to developers')
        return parser

    @staticmethod
    def get_objects_from_args(args_to_parse: Optional[List[str]] = None) -> Tuple[RouterSearcher, Logger, Printer]:
        ip_address, output_file, community, add_routes, debug = ArgParser._parse_args(args_to_parse)
        while ip_address is None or ip_address.isspace():
            ip_address = input("Please, insert ip address:")
        community = community if community else DEFAULT_COMMUNITY
        # dependencies
        logger = FileLogger(file_name=output_file, debug=debug) if output_file else StdoutLogger(debug)
        route_creator = EmptyRouterCreator(logger=logger) if not add_routes else LinuxRouterCreator()
        printer: Printer = PrinterImp(backend=logger)
        searcher: RouterSearcher = RouterSearcherFacade(
            ip_addr=ip_address, creator=route_creator, printer=printer, logger=logger, community=community
        )
        return searcher, logger, printer
