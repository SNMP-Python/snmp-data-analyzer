from __future__ import absolute_import

from typing import FrozenSet, List

from arg_parser.arg_parser import ArgParser
from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from painter.graphviz_painter import GraphVizPainter
from parser.interface_remover import InterfaceRemover
from parser.router_parser import RouterParser
from parser.router_parser_facade import RouterParserFacade
from parser.value_objects.router import Router
from printer.printer import Printer
from printer.printer_imp import PrinterImp
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher
from searcher.router_searcher_facade import RouterSearcherFacade


def main(argv=None):
    ip_addr, logger, creator = ArgParser.get_objects_from_args(argv)
    printer: Printer = PrinterImp(backend=logger)
    searcher: RouterSearcher = RouterSearcherFacade(ip_addr=ip_addr, creator=creator, printer=printer, logger=logger)
    primitives: FrozenSet[RouterPrimitives] = searcher.get_router_primitives()
    parser: RouterParser = RouterParserFacade(printer=printer, logger=logger, routers_primitives=primitives)
    list_routers: List[Router] = parser.get_routers()
    InterfaceRemover.remove_down_and_loopback(list_routers, logger=logger)
    graph: FrozenSet[RouterNode] = GraphCreatorImp(list_routers).get_graph()
    painter = GraphVizPainter(graph)
    painter.paint()


if __name__ == "__main__":
    main()
