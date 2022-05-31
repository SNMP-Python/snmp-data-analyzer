from __future__ import absolute_import

from easysnmp import EasySNMPTimeoutError, Session

from searcher.client import Client
from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.primitives.router_primitives import RouterPrimitives

SYS_NAME_OID = '.1.3.6.1.2.1.1.5.0'
INTERFACE_TABLE_OID = '.1.3.6.1.2.1.2.2'
IP_ADDR_TABLE_OID = '.1.3.6.1.2.1.4.20'
IP_ROUTE_TABLE_OID = '1.3.6.1.2.1.4.21'
RO_COMMUNITY = 'rocom'
SNMP_VERSION = 2


class SNMPClient(Client):
    def get_router_primitives(self, ip_addr: str) -> RouterPrimitives:
        return SNMPClient._get_primitives_from_addr(ip_addr)

    @staticmethod
    def _get_primitives_from_addr(ip_addr: str) -> RouterPrimitives:
        session = SNMPClient._get_session_from(ip_addr)
        return SNMPClient._get_primitives_from_session(session)

    @staticmethod
    def _get_session_from(ip_addr: str) -> Session:
        return Session(hostname=ip_addr, community=RO_COMMUNITY, version=SNMP_VERSION)

    @staticmethod
    def _get_primitives_from_session(session: Session) -> RouterPrimitives:
        return RouterPrimitives(
            sys_name=SNMPClient._get_sys_name(session),
            interfaces=[],
            routing_table=[],
        )

    @staticmethod
    def _get_sys_name(session: Session) -> str:
        try:
            return session.get('1.2.3223123.11231').value
        except EasySNMPTimeoutError:
            raise NonReachableHostException(session.hostname)
