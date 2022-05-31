from __future__ import absolute_import

from typing import FrozenSet

from searcher.client import Client
from searcher.primitives.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher
from searcher.snmp_client import SNMPClient


class SNMPRouterSearcher(RouterSearcher):
    def __init__(self, ip_addr: str, client: Client = SNMPClient()):
        self.ip_addr = ip_addr
        self.client = client

    def get_router_primitives(self) -> FrozenSet[RouterPrimitives]:
        visited_ids = set()
        stack = [self.ip_addr]
        result = []
        while stack:
            current_ip = stack.pop()
            primitives_router = self.client.get_router_primitives(current_ip)
            visited_ids.add(primitives_router.ospf_id)
            result.append(primitives_router)
            for id_neighbor in primitives_router.neighbors:
                if id_neighbor not in visited_ids and id_neighbor not in stack:
                    stack.append(id_neighbor)
        return frozenset(result)
