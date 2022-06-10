from __future__ import absolute_import

from typing import FrozenSet, List, Dict

from arg_parser.arg_parser import ArgParser
from distance.distance_calculator_imp import DistanceCalculatorImp
from distance.path import Path
from distance.point import Point
from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from painter.graphviz_painter import GraphVizPainter
from parser.interface_remover import InterfaceRemover
from parser.router_parser import RouterParser
from parser.router_parser_facade import RouterParserFacade
from parser.value_objects.router import Router
from printer.printer import Printer
from searcher.primitives.router_primitives import RouterPrimitives


def main(argv=None):
    # setup dependencies
    searcher, logger, printer = ArgParser.get_objects_from_args(argv)

    # get information from snmp and parse it to the domain objects
    primitives: FrozenSet[RouterPrimitives] = searcher.get_router_primitives()
    parser: RouterParser = RouterParserFacade(
        printer=printer, logger=logger, routers_primitives=primitives
    )
    list_routers: List[Router] = parser.get_routers()
    InterfaceRemover.remove_down_and_loopback(list_routers, logger=logger)

    # print values
    print_network_from_routers(list_routers=list_routers, printer=printer)


def print_network_from_routers(list_routers: List[Router], printer: Printer):
    graph: List[RouterNode] = GraphCreatorImp(list_routers).get_graph()
    distances: Dict[Point, Path] = DistanceCalculatorImp(graph).get_distances()
    printer.print_distances(distances)
    painter = GraphVizPainter(graph)
    painter.paint()


if __name__ == "__main__":
    main()
