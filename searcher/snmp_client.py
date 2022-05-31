from __future__ import absolute_import

from searcher.primitives.router_primitives import RouterPrimitives

SYS_NAME_OID = '.1.3.6.1.2.1.1.5.0'
INTERFACE_TABLE_OID = '.1.3.6.1.2.1.2.2'
IP_ADDR_TABLE_OID = '.1.3.6.1.2.1.4.20'
IP_ROUTE_TABLE_OID = '1.3.6.1.2.1.4.21'


class SNMPClient:
    def get_router_primitives(self, ip_addr: str) -> RouterPrimitives:
        pass
