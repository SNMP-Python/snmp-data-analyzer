from __future__ import absolute_import

from typing import FrozenSet, Set, List

from searcher.client import Client
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher
from searcher.snmp_client import SNMPClient


class SNMPRouterSearcher(RouterSearcher):

    def __init__(self, ip_addr: str, client: Client = SNMPClient()):
        self.ip_addr = ip_addr
        self.client = client
        self.visited_ips: Set[str] = set()
        self.ips_to_visit: List[str] = [self.ip_addr]
        self.routers: Set[RouterPrimitives] = set()

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
        self.ips_to_visit.extend(self._get_ips_to_visit_from_router(router))

    def _get_ips_to_visit_from_router(self, router: RouterPrimitives) -> List[str]:
        result = []
        for id_neighbor in router.neighbors:
            if id_neighbor not in self.visited_ips and id_neighbor not in self.ips_to_visit:
                self.ips_to_visit.append(id_neighbor)
        return result
