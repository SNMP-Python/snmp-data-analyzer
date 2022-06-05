from __future__ import absolute_import

from argparse import ArgumentParser

from typing import Dict

IP_FLAG = 'ip'
OUTPUT_FILE_FLAG = 'output'
ADD_ROUTES_FLAG = 'add_routes'


class ParsedArgs:
    def __init__(self, ip_address, output_file, add_routes):
        self.ip_address = ip_address
        self.output_file = output_file
        self.add_routes = add_routes


class ArgParser:
    @staticmethod
    def get_args() -> ParsedArgs:
        args = ArgParser._parse_args()
        return ParsedArgs(
            ip_address=args[IP_FLAG], output_file=args[OUTPUT_FILE_FLAG], add_routes=args[ADD_ROUTES_FLAG]
        )

    @staticmethod
    def _parse_args() -> Dict[str, str]:
        parser = ArgParser._get_parser()
        return parser.parse_args().__dict__

    @staticmethod
    def _get_parser() -> ArgumentParser:
        parser = ArgumentParser(
            description='A program that analyzes the network by asking routers using the ' 'snmp protocol.'
        )
        return ArgParser._add_flags(parser)

    @staticmethod
    def _add_flags(parser: ArgumentParser) -> ArgumentParser:
        parser.add_argument('-i', '--ip', type=str, help='The ip address of the router.')
        parser.add_argument('-o', '--output', type=str, help='The output file.')
        parser.add_argument('-a', '--add-routes', action='store_true', help='Adds needed routes to perform snmp polls.')
        return parser
