from test.shared.interface_primitive_mothers import InterfacePrimitiveMother
from test.shared.route_primitive_mother import RoutePrimitiveMother
from typing import List

from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives
from searcher.primitives.router_primitives import RouterPrimitives


class RouterPrimitiveMother:
    @staticmethod
    def get(
        sys_name: str = "router_1",
        interfaces: List[
            InterfacePrimitives
        ] = InterfacePrimitiveMother.get_list_of_one_element(),
        routing_table: List[
            RoutePrimitives
        ] = RoutePrimitiveMother.get_list_of_one_route(),
        ospf_id: str = "",
    ) -> RouterPrimitives:
        return RouterPrimitives(sys_name, ospf_id, interfaces, routing_table)

    @staticmethod
    def get_one_router(
        sys_name: str = "router_1",
        interfaces: List[
            InterfacePrimitives
        ] = InterfacePrimitiveMother.get_list_of_one_element(),
        routing_table: List[
            RoutePrimitives
        ] = RoutePrimitiveMother.get_list_of_one_route(),
        ospf_id: str = "",
    ) -> List[RouterPrimitives]:
        return [
            RouterPrimitiveMother.get(
                sys_name=sys_name,
                interfaces=interfaces,
                routing_table=routing_table,
                ospf_id=ospf_id,
            )
        ]

    @staticmethod
    def get_router_with(id_router: int, neighbors: List[str], ospf_id: str):
        return RouterPrimitives(
            sys_name=f"Router-{id_router}",
            interfaces=[],
            routing_table=[],
            neighbors=neighbors,
            ospf_id=ospf_id,
        )
