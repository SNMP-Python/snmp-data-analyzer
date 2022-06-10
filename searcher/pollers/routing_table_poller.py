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
        return self.get_list_route_primitives(primitives)

    @staticmethod
    def poll_everything(session: Session) -> Tuple[List[str], List[str], List[str], List[str]]:
        networks = list(map(lambda x: x.value, session.walk(ROUTE_NETWORK_OID)))
        masks = list(map(lambda x: x.value, session.walk(ROUTE_MASK_OID)))
        next_hop = list(map(lambda x: x.value, session.walk(ROUTE_NEXT_HOP_OID)))
        type_link = list(map(lambda x: x.value, session.walk(ROUTE_TYPE_OID)))
        return networks, masks, next_hop, type_link

    def get_list_route_primitives(self, primitives: Tuple[List[str], List[str], List[str], List[str]]) -> List[RoutePrimitives]:
        networks = primitives[0]
        masks = primitives[1]
        next_hops = primitives[2]
        type_link = primitives[3]
        result = []
        for i in range(0, len(networks)):
            result.append(RoutePrimitives(networks[i], masks[i], next_hops[i], type_link[i]))
        return result