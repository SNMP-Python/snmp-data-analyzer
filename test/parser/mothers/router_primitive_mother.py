from test.parser.mothers.interface_primitive_mothers import \
    InterfacePrimitiveMother
from test.parser.mothers.route_primitive_mother import RoutePrimitiveMother
from typing import List

from searcher.interface_primitives import InterfacePrimitives
from searcher.route_primitive import RoutePrimitive
from searcher.router_primitives import RouterPrimitives


class RouterPrimitiveMother:
    @staticmethod
    def get(
        sys_name: str = "router_1",
        interfaces: List[
            InterfacePrimitives
        ] = InterfacePrimitiveMother.get_list_of_one_element(),
        routing_table: List[
            RoutePrimitive
        ] = RoutePrimitiveMother.get_list_of_one_route(),
    ) -> RouterPrimitives:
        return RouterPrimitives(sys_name, interfaces, routing_table)

    @staticmethod
    def get_one_router(
        sys_name: str = "router_1",
        interfaces: List[
            InterfacePrimitives
        ] = InterfacePrimitiveMother.get_list_of_one_element(),
        routing_table: List[
            RoutePrimitive
        ] = RoutePrimitiveMother.get_list_of_one_route(),
    ) -> List[RouterPrimitives]:
        return [
            RouterPrimitiveMother.get(
                sys_name=sys_name, interfaces=interfaces, routing_table=routing_table
            )
        ]
