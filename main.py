from __future__ import absolute_import

from typing import FrozenSet, List

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from painter.graphviz_painter import GraphVizPainter
from parser.interface_remover import InterfaceRemover
from parser.router_parser import RouterParser
from parser.router_parser_facade import RouterParserFacade
from parser.value_objects.router import Router
from printer.file_logger import FileLogger
from printer.logger import Logger
from printer.printer import Printer
from printer.printer_imp import PrinterImp
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.route_creation.linux_route_creator import LinuxRouterCreator
from searcher.router_searcher import RouterSearcher
from searcher.router_searcher_facade import RouterSearcherFacade


def main():
    ip_addr = get_ip_addr_from_input()
    logger: Logger = FileLogger(file_name="test.txt")
    printer: Printer = PrinterImp(backend=logger)
    searcher: RouterSearcher = RouterSearcherFacade(
        ip_addr=ip_addr, creator=LinuxRouterCreator(), printer=printer, logger=logger
    )
    primitives: FrozenSet[RouterPrimitives] = searcher.get_router_primitives()
    parser: RouterParser = RouterParserFacade(printer=printer, logger=logger, routers_primitives=primitives)
    list_routers: List[Router] = parser.get_routers()
    InterfaceRemover.remove_down_and_loopback(list_routers, logger=logger)
    graph: FrozenSet[RouterNode] = GraphCreatorImp(list_routers).get_graph()
    painter = GraphVizPainter(graph)
    painter.paint()


def get_ip_addr_from_input() -> str:
    # pylint: disable=W1632
    ip_addr = input("Please, insert ip address:")
    return ip_addr


if __name__ == "__main__":
    main()
