from __future__ import absolute_import

from typing import List

from easysnmp import Session

from searcher.exceptions.next_hop_not_found_exception import NextHopNotFoundException
from searcher.pollers.poller import Poll
from searcher.primitives.route_primitives import RoutePrimitives

ROUTE_NETWORK_OID = "IP-FORWARD-MIB::ipCidrRouteDest"
ROUTE_MASK_OID = "RFC1213-MIB::ipRouteMask"
ROUTE_NEXT_HOP_OID = "IP-FORWARD-MIB::ipCidrRouteNextHop"
ROUTE_TYPE_OID = "IP-FORWARD-MIB::ipCidrRouteType"


class RoutingTablePoller(Poll):
    def poll(self) -> List[RoutePrimitives]:
        return list(
            map(
                lambda network: RoutingTablePoller._get_route_from_network(self.session, network),
                RoutingTablePoller._get_networks(self.session),
            )
        )

    @staticmethod
    def _get_networks(session: Session) -> List[str]:
        return list(map(lambda entry: str(entry.value), session.walk(ROUTE_NETWORK_OID)))

    @staticmethod
    def _get_route_from_network(session: Session, network: str) -> RoutePrimitives:
        mask = RoutingTablePoller._get_route_mask(session, network)
        return RoutePrimitives(
            network=network,
            mask=mask,
            next_hop=RoutingTablePoller._get_route_next_hop(session, network, mask),
            route_type=RoutingTablePoller._get_route_type(session, network, mask),
        )

    @staticmethod
    def _get_route_mask(session: Session, network: str) -> str:
        return str(session.get(ROUTE_MASK_OID + "." + network).value)

    @staticmethod
    def _get_route_next_hop(session: Session, network: str, mask: str) -> str:
        result = session.walk(ROUTE_NEXT_HOP_OID + "." + network + "." + mask)
        if len(result) != 1:
            raise NextHopNotFoundException()
        return str(result[0].value)

    @staticmethod
    def _get_route_type(session: Session, network: str, mask: str) -> str:
        return str(session.walk(ROUTE_TYPE_OID + "." + network + "." + mask)[0].value)
