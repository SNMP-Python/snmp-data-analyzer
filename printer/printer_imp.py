# pylint: disable=C0209, W0108
from __future__ import absolute_import

from typing import Dict, List, FrozenSet

from distance.path import Path
from distance.point import Point
from parser.value_objects.interface.interface import Interface
from parser.value_objects.router import Router
from parser.value_objects.routing_table_entry import RoutingTableEntry
from printer.logger import Logger
from printer.printer import Printer
from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives
from searcher.primitives.router_primitives import RouterPrimitives

SEPARATOR_ROUTER_DISTANCE = " -> "


class PrinterImp(Printer):
    def __init__(self, backend: Logger):
        self.logger = backend

    def print_primitives(
        self, router_primitives: FrozenSet[RouterPrimitives]
    ) -> None:
        self.logger.info("Showing information about router primitives:")
        for router in router_primitives:
            self.logger.normal(f"Router sys name: {router.sys_name}")
            self.logger.normal(f"\tRouter OSPF id: {router.ospf_id}")
            self._print_primitive_interfaces(router.interfaces)
            self._print_primitive_routing_table(router.routing_table)

    def print_routers(self, routers: FrozenSet[Router]) -> None:
        self.logger.info("Showing information about routers:")
        for router in routers:
            self.logger.normal(f"Router sys name: {router.sys_name}")
            self._print_interfaces(router.interfaces)
            self._print_routing_table(router.routing_table)

    def print_distances(self, distances: Dict[Point, Path]) -> None:
        self.logger.info("Showing information about distances")
        max_length = PrinterImp._get_max_length_of_path(distances)
        self._write_beginning_of_distances_table(max_length=max_length)
        self._print_table_elements(distances, max_length)

    # methods for printing the router primitive values:

    def _print_primitive_interfaces(
        self, interfaces: List[InterfacePrimitives]
    ):
        self.logger.normal("\tInterfaces:")
        for interface in interfaces:
            self.logger.normal(f"\t\tName: {interface.interface}")
            self.logger.normal(f"\t\t\tIp: {interface.ip_addr}")
            self.logger.normal(f"\t\t\tMask: {interface.mask}")
            self.logger.normal(f"\t\t\tStatus: {interface.status}")
            self.logger.normal(f"\t\t\tType: {interface.int_type}")
            self.logger.normal(f"\t\t\tSpeed: {interface.speed}")

    def _print_primitive_routing_table(
        self, routing_table: List[RoutePrimitives]
    ):
        self._print_init_table()
        for routing_table_entry in routing_table:
            self._print_table_row(
                routing_table_entry.network,
                routing_table_entry.mask,
                routing_table_entry.next_hop,
                routing_table_entry.route_type,
            )
            self._print_separator_table()

    # methods for printing the router domain values:

    def _print_interfaces(self, interfaces: List[Interface]):
        self.logger.normal("\tInterfaces:")
        for interface in interfaces:
            self.logger.normal(f"\t\t{interface.name}:")
            self.logger.normal(f"\t\t\tStatus: {interface.status.name}:")
            self.logger.normal(f"\t\t\tIp: {interface.network.ip}:")
            self.logger.normal(f"\t\t\tMask: {interface.network.netmask}:")
            self.logger.normal(f"\t\t\tType: {interface.type_interface}:")
            self.logger.normal(f"\t\t\tSpeed: {interface.speed}:")

    def _print_routing_table(self, routing_table: List[RoutingTableEntry]):
        self._print_init_table(type_length=20)
        for table_entry in routing_table:
            self._print_table_row(
                str(table_entry.network.ip),
                str(table_entry.network.netmask),
                str(table_entry.next_hop),
                str(table_entry.route_type),
                type_length=20,
            )
            self._print_separator_table(type_length=20)

    # helper methods for printing the router table

    def _print_init_table(self, type_length=5):
        self.logger.normal("\tRouting Table:")
        self._print_separator_table(type_length=type_length)
        # pylint: disable=C0301
        self.logger.normal(
            f"\t\t|{'{:<15}'.format('Network:')}|{'{:<15}'.format('Mask:')}|{'{:<15}'.format('Next hop:')}|{('{:<' + str(type_length) + '}').format('Type:')}| "
        )
        self._print_separator_table(type_length=type_length)

    # pylint: disable=R0913
    def _print_table_row(
        self,
        network: str,
        mask: str,
        hop: str,
        type_network: str,
        type_length=5,
    ):
        # pylint: disable=C0301
        self.logger.normal(
            f"\t\t|{'{:<15}'.format(network)}|{'{:<15}'.format(mask)}|{'{:<15}'.format(hop)}|{('{:<' + str(type_length) + '}').format(type_network)}|"
        )

    def _print_separator_table(self, type_length=5):
        self.logger.normal(
            f"\t\t|{'-' * 15}|{'-' * 15}|{'-' * 15}|{'-' * type_length}|"
        )

    # helper methods for printing the distances' router table

    def _print_table_elements(
        self, distances: Dict[Point, Path], max_length: int
    ):
        for points, path in distances.items():
            path_sys_name: List[str] = [
                router.sys_name.name for router in path.get_path()
            ]
            self._print_distances_table(
                str(points.source),
                SEPARATOR_ROUTER_DISTANCE.join(path_sys_name),
                str(points.destination),
                max_length,
            )

    @staticmethod
    def _get_max_length_of_path(distances: Dict[Point, Path]) -> int:
        paths = [
            SEPARATOR_ROUTER_DISTANCE.join(
                [router.sys_name.name for router in path.get_path()]
            )
            for path in distances.values()
        ]
        return max(map(lambda x: len(x), paths))

    def _write_beginning_of_distances_table(self, max_length: int):
        self.logger.normal(f"|{'-' * 15}|{'-' * max_length}|{'-' * 15}|")
        self.logger.normal(
            f"|{'{:<15}'.format('IP Source')}|"
            + f"{('{:<' + str(max_length) + '}').format('Path')}"
            + f"|{'{:<15}'.format('IP Dest')}|"
        )
        self.logger.normal(f"|{'-' * 15}|{'-' * max_length}|{'-' * 15}|")

    def _print_distances_table(
        self, source: str, path: str, destination: str, max_length: int
    ):
        self.logger.normal(
            f"|{'{:<15}'.format(source)}|"
            + f"{('{:<' + str(max_length) + '}').format(path)}|"
            + f"{'{:<15}'.format(destination)}|"
        )
        self.logger.normal(f"|{'-' * 15}|{'-' * max_length}|{'-' * 15}|")
