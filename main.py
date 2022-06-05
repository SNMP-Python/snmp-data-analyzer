from __future__ import absolute_import

from typing import List, FrozenSet

from graph.graph_creator_imp import GraphCreatorImp
from painter.graphviz_painter import GraphVizPainter
from parser.interface_remover import InterfaceRemover
from parser.router_parser import RouterParser
from parser.router_parser_imp import RouterParserImp
from printer.file_logger import FileLogger
from printer.logger import Logger
from printer.printer import Printer
from printer.printer_imp import PrinterImp
from printer.stdout_logger import StdoutLogger
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher
from searcher.snmp_router_searcher import SNMPRouterSearcher


def main():
    ip_addr = get_ip_addr_from_input()
    logger: Logger = FileLogger(file_name="test.txt")
    printer: Printer = PrinterImp(backend=logger)
    searcher: RouterSearcher = SNMPRouterSearcher(ip_addr=ip_addr)
    primitives: FrozenSet[RouterPrimitives] = searcher.get_router_primitives()
    printer.print_primitives(primitives)
    parser: RouterParser = RouterParserImp(primitives=primitives)
    list_routers = parser.get_routers()
    printer.print_routers(frozenset(list_routers))
    InterfaceRemover.remove_down_and_loopback(list_routers, logger=logger)
    graph = GraphCreatorImp(list_routers).get_graph()
    painter = GraphVizPainter(graph)
    painter.paint()


def get_ip_addr_from_input() -> str:
    # pylint: disable=W1632
    ip_addr = input("Please, insert ip address:")
    return ip_addr


if __name__ == "__main__":
    main()
