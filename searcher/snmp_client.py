from __future__ import absolute_import

from typing import List

from easysnmp import EasySNMPTimeoutError, Session

from searcher.client import Client
from searcher.exceptions.next_hop_not_found_exception import NextHopNotFoundException
from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.exceptions.ospf_id_not_available import OSPFIdNotAvailableException
from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives
from searcher.primitives.router_primitives import RouterPrimitives

SYS_NAME_OID = ".1.3.6.1.2.1.1.5.0"
INTERFACE_INDEX_OID = "RFC1213-MIB::ifIndex"
INTERFACE_STATUS_OID = "RFC1213-MIB::ifOperStatus"
INTERFACE_SPEED_OID = "RFC1213-MIB::ifSpeed"
INTERFACE_TYPE_OID = "RFC1213-MIB::ifType"
INTERFACE_ADDR_OID = "RFC1213-MIB::ipAdEntAddr"
INTERFACE_INDEX_TO_ADDR_OID = "RFC1213-MIB::ipAdEntIfIndex"
INTERFACE_MASK_OID = "RFC1213-MIB::ipAdEntNetMask"
INTERFACE_DESCR_OID = "RFC1213-MIB::ifDescr"
ROUTE_NETWORK_OID = "IP-FORWARD-MIB::ipCidrRouteDest"
ROUTE_MASK_OID = "RFC1213-MIB::ipRouteMask"
ROUTE_NEXT_HOP_OID = "IP-FORWARD-MIB::ipCidrRouteNextHop"
ROUTE_TYPE_OID = "IP-FORWARD-MIB::ipCidrRouteType"
OSPF_ID_OID = ".1.3.6.1.2.1.14.1.1"
OSPF_BEIGHBORS_OID = 'OSPF-MIB::ospfNbrIpAddr'
IP_ROUTE_TABLE_OID = "1.3.6.1.2.1.4.21"
RO_COMMUNITY = "rocom"
SNMP_VERSION = 2


class IndexAddresPair:
    def __init__(self, index: int, addr: str):
        self.index = index
        self.addr = addr


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
            interfaces=SNMPClient._get_interfaces(session),
            routing_table=SNMPClient._get_routing_table(session),
            ospf_id=SNMPClient._get_ospf_id(session),
            neighbors=SNMPClient._get_ospf_neighbors(session),
        )

    @staticmethod
    def _get_sys_name(session: Session) -> str:
        try:
            return session.get(SYS_NAME_OID).value
        except EasySNMPTimeoutError as error:
            raise NonReachableHostException(session.hostname) from error

    @staticmethod
    def _get_interfaces(session: Session) -> List[InterfacePrimitives]:
        return list(
            map(
                lambda pair: SNMPClient._get_interface_from_index(
                    session, pair.index, pair.addr
                ),
                SNMPClient._get_interfaces_indx_addr_pair(session),
            )
        )

    @staticmethod
    def _get_interfaces_indx_addr_pair(session: Session) -> List[IndexAddresPair]:
        return list(
            map(
                lambda entry: IndexAddresPair(entry.value, entry.oid_index),
                session.walk(INTERFACE_INDEX_TO_ADDR_OID),
            )
        )

    @staticmethod
    def _get_interface_from_index(
        session: Session, index: int, addr: str
    ) -> InterfacePrimitives:
        return InterfacePrimitives(
            interface=SNMPClient._get_interface_descr(session, index),
            ip_addr=addr,
            mask=SNMPClient._get_interface_mask(session, addr),
            status=SNMPClient._get_interface_status(session, index),
            speed=SNMPClient._get_interface_speed(session, index),
            int_type=SNMPClient._get_interface_type(session, index),
        )

    @staticmethod
    def _get_interface_descr(session: Session, index: int) -> str:
        return session.get(INTERFACE_DESCR_OID + "." + str(index)).value

    @staticmethod
    def _get_interface_mask(session: Session, addr: str) -> str:
        return session.get(INTERFACE_MASK_OID + "." + addr).value

    @staticmethod
    def _get_interface_status(session: Session, index: int) -> str:
        return str(session.get(INTERFACE_STATUS_OID + "." + str(index)).value)

    @staticmethod
    def _get_interface_speed(session: Session, index: int) -> str:
        return str(session.get(INTERFACE_SPEED_OID + "." + str(index)).value)

    @staticmethod
    def _get_interface_type(session: Session, index: int) -> str:
        return str(session.get(INTERFACE_TYPE_OID + "." + str(index)).value)

    @staticmethod
    def _get_routing_table(session: Session) -> List[RoutePrimitives]:
        return list(
            map(
                lambda network: SNMPClient._get_route_from_network(session, network),
                SNMPClient._get_networks(session),
            )
        )

    @staticmethod
    def _get_networks(session: Session) -> List[str]:
        return list(
            map(lambda entry: str(entry.value), session.walk(ROUTE_NETWORK_OID))
        )

    @staticmethod
    def _get_route_from_network(session: Session, network: str) -> RoutePrimitives:
        mask = SNMPClient._get_route_mask(session, network)
        return RoutePrimitives(
            network=network,
            mask=mask,
            next_hop=SNMPClient._get_route_next_hop(session, network, mask),
            route_type='3',
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
    def _get_route_type(session: Session, network: str) -> str:
        return str(session.get(ROUTE_TYPE_OID + "." + network).value)

    @staticmethod
    def _get_ospf_id(session: Session) -> str:
        result = session.walk(".1.3.6.1.2.1.14.1.1")
        if len(result) != 1:
            raise OSPFIdNotAvailableException()
        return result[0].value

    @staticmethod
    def _get_ospf_neighbors(session: Session) -> List[str]:
        queso = list(
            map(
                lambda neighbor: neighbor.value,
                session.walk(OSPF_BEIGHBORS_OID),
            )
        )
        return queso
