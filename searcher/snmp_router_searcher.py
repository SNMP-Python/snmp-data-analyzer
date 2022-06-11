from __future__ import absolute_import

from typing import FrozenSet, Set, List, Optional

from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from parser.ip_objects_converter import IPParser
from searcher.client import Client
from searcher.exceptions.route_creation import RouteCreationException
from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.route_creation.route_creator import RouteCreator
from searcher.router_searcher import RouterSearcher
from searcher.snmp_client import SNMPClient


class SNMPRouterSearcher(RouterSearcher):
    def __init__(self, ip_addr: str, router_creator: RouteCreator, community: Optional[str] = None,
                 client: Optional[Client] = None):
        self.ip_addr = ip_addr
        self.client = client if client else SNMPClient(community)
        self.router_creator = router_creator
        self.visited_ips: Set[str] = set()
        self.ips_to_visit: List[str] = [self.ip_addr]
        self.routers: Set[RouterPrimitives] = set()
        self.first_hop = ip_addr

    def get_router_primitives(self) -> FrozenSet[RouterPrimitives]:
        while self.ips_to_visit:
            current_ip = self.ips_to_visit.pop()
            router = self.client.get_router_primitives(current_ip)
            self.routers.add(router)
            self._update_ips_to_visit_and_visited(router=router)
        return frozenset(self.routers)

    def _update_ips_to_visit_and_visited(self, router: RouterPrimitives) -> None:
        for interface in router.interfaces:
            self.visited_ips.add(interface.ip_addr)
        ips_to_visit = self._get_ips_to_visit_from_router(router)
        self._add_network_gateway_to_host(ips_to_visit, router.interfaces)
        self.ips_to_visit.extend(ips_to_visit)

    def _get_ips_to_visit_from_router(self, router: RouterPrimitives) -> List[str]:
        return list(
            filter(
                lambda ip_addr: ip_addr not in self.visited_ips and ip_addr not in self.ips_to_visit, router.neighbors
            )
        )

    def _add_network_gateway_to_host(self, ips_to_visit: List[str], interfaces: List[InterfacePrimitives]):
        try:
            for ip_to_visit in ips_to_visit:
                ip_addr = IPParser.get_ip_address_from(ip_to_visit)
                for interface in interfaces:
                    network = IPParser.get_network_from(interface.ip_addr, interface.mask)
                    if ip_addr in network:
                        self.router_creator.create_route_to(network=network.network, mask=network.netmask)
        except InvalidIpException as error:
            raise error
        except InvalidMaskException as error:
            raise error
        except Exception as error:
            raise RouteCreationException("Couldn't add route to device routing table because os limitations") from error

    def get_first_hop(self) -> str:
        return self.first_hop
