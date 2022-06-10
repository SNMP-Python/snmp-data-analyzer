from __future__ import absolute_import

from typing import List, Tuple

from easysnmp import Session

from searcher.pollers.poller import Poll
from searcher.primitives.route_primitives import RoutePrimitives

ROUTE_NETWORK_OID = "IP-FORWARD-MIB::ipCidrRouteDest"
ROUTE_MASK_OID = "IP-FORWARD-MIB::ipCidrRouteMask"
ROUTE_NEXT_HOP_OID = "IP-FORWARD-MIB::ipCidrRouteNextHop"
ROUTE_TYPE_OID = "IP-FORWARD-MIB::ipCidrRouteType"


class RoutingTablePoller(Poll):
    def poll(self) -> List[RoutePrimitives]:
        primitives = RoutingTablePoller.poll_everything(self.session)
        return RoutingTablePoller.get_list_route_primitives(primitives)

    @staticmethod
    def poll_everything(session: Session) -> Tuple[List[str], List[str], List[str], List[str]]:
        networks = list(map(lambda x: x.value, session.walk(ROUTE_NETWORK_OID)))
        masks = list(map(lambda x: x.value, session.walk(ROUTE_MASK_OID)))
        next_hop = list(map(lambda x: x.value, session.walk(ROUTE_NEXT_HOP_OID)))
        type_link = list(map(lambda x: x.value, session.walk(ROUTE_TYPE_OID)))
        return networks, masks, next_hop, type_link

    @staticmethod
    def get_list_route_primitives(primitives: Tuple[List[str], List[str], List[str], List[str]]) -> List[
        RoutePrimitives]:
        result = []
        for _, (network, mask, next_hop, type_link) in enumerate(
                zip(primitives[0], primitives[1], primitives[2], primitives[3])):
            result.append(RoutePrimitives(network, mask, next_hop, type_link))
        return result
