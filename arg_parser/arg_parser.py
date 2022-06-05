from __future__ import absolute_import

from argparse import ArgumentParser
from typing import Optional, Tuple, List

from printer.file_logger import FileLogger
from printer.logger import Logger
from printer.stdout_logger import StdoutLogger
from searcher.route_creation.empty_route_creator import EmptyRouterCreator
from searcher.route_creation.linux_route_creator import LinuxRouterCreator
from searcher.route_creation.route_creator import RouteCreator

IP_FLAG = 'ip'
OUTPUT_FILE_FLAG = 'output'
ADD_ROUTES_FLAG = 'add_routes'


class ArgParser:
    @staticmethod
    def get_objects_from_args(args_to_parse: Optional[List[str]] = None) -> Tuple[str, Logger, RouteCreator]:
        ip_address, output_file, add_routes = ArgParser._parse_args(args_to_parse)
        while ip_address is None or ip_address.isspace():
            ip_address = input("Please, insert ip address:")
        logger = FileLogger(file_name=output_file) if output_file else StdoutLogger()
        route_creator = EmptyRouterCreator(logger=logger) if not add_routes else LinuxRouterCreator()
        return ip_address, logger, route_creator

    @staticmethod
    def _parse_args(args: Optional[List[str]]) -> Tuple[Optional[str], Optional[str], bool]:
        parser = ArgParser._get_parser()
        arguments = parser.parse_args(args=args).__dict__
        return arguments[IP_FLAG], arguments[OUTPUT_FILE_FLAG], arguments[ADD_ROUTES_FLAG]

    @staticmethod
    def _get_parser() -> ArgumentParser:
        parser = ArgumentParser(
            description='A program that analyzes the network by asking routers using the snmp protocol.'
        )
        return ArgParser._add_flags(parser)

    @staticmethod
    def _add_flags(parser: ArgumentParser) -> ArgumentParser:
        parser.add_argument('-i', '--ip', type=str, help='The ip address of the router.')
        parser.add_argument('-o', '--output', type=str, help='The output file.')
        parser.add_argument('-a', '--add-routes', action='store_true', help='Adds needed routes to perform snmp polls.')
        return parser
