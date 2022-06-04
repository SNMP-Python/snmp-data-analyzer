from __future__ import absolute_import

from easysnmp import EasySNMPTimeoutError, Session

from searcher.client import Client
from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.pollers.interfaces_poller import InterfacesPoller
from searcher.pollers.ospf_id_poller import OSPFIdPoller
from searcher.pollers.ospf_neighbors_poller import OSPFNeighborsPoller
from searcher.pollers.routing_table_poller import RoutingTablePoller
from searcher.pollers.sys_name_poller import SysNamePoller
from searcher.primitives.router_primitives import RouterPrimitives

RO_COMMUNITY = "rocom"
SNMP_VERSION = 2


class SNMPClient(Client):
    def get_router_primitives(self, ip_addr: str) -> RouterPrimitives:
        try:
            return SNMPClient._get_primitives_from_addr(ip_addr)
        except EasySNMPTimeoutError as error:
            raise NonReachableHostException(ip_addr) from error

    @staticmethod
    def _get_primitives_from_addr(ip_addr: str) -> RouterPrimitives:
        session = SNMPClient._get_session_from_ip(ip_addr)
        return SNMPClient._get_primitives_from_session(session)

    @staticmethod
    def _get_session_from_ip(ip_addr: str) -> Session:
        return Session(hostname=ip_addr, community=RO_COMMUNITY, version=SNMP_VERSION)

    @staticmethod
    def _get_primitives_from_session(session: Session) -> RouterPrimitives:
        return RouterPrimitives(
            sys_name=SysNamePoller(session).poll(),
            interfaces=InterfacesPoller(session).poll(),
            routing_table=RoutingTablePoller(session).poll(),
            ospf_id=OSPFIdPoller(session).poll(),
            neighbors=OSPFNeighborsPoller(session).poll(),
        )
