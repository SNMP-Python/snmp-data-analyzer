from __future__ import absolute_import

from typing import List

from easysnmp import Session

from searcher.pollers.poller import Poll
from searcher.primitives.interface_primitives import InterfacePrimitives

INTERFACE_INDEX_OID = "RFC1213-MIB::ifIndex"
INTERFACE_STATUS_OID = "RFC1213-MIB::ifOperStatus"
INTERFACE_SPEED_OID = "RFC1213-MIB::ifSpeed"
INTERFACE_TYPE_OID = "RFC1213-MIB::ifType"
INTERFACE_ADDR_OID = "RFC1213-MIB::ipAdEntAddr"
INTERFACE_INDEX_TO_ADDR_OID = "RFC1213-MIB::ipAdEntIfIndex"
INTERFACE_MASK_OID = "RFC1213-MIB::ipAdEntNetMask"
INTERFACE_DESCR_OID = "RFC1213-MIB::ifDescr"


class InterfaceIndexAddresPair:
    def __init__(self, index: int, addr: str):
        self.index = index
        self.addr = addr


class InterfacesPoller(Poll):
    def poll(self) -> List[InterfacePrimitives]:
        return list(
            map(
                lambda pair: InterfacesPoller._get_interface_from_index(self.session, pair.index, pair.addr),
                InterfacesPoller._get_interfaces_indx_addr_pair(self.session),
            )
        )

    @staticmethod
    def _get_interfaces_indx_addr_pair(session: Session) -> List[InterfaceIndexAddresPair]:
        return list(
            map(
                lambda entry: InterfaceIndexAddresPair(entry.value, entry.oid_index),
                session.walk(INTERFACE_INDEX_TO_ADDR_OID),
            )
        )

    @staticmethod
    def _get_interface_from_index(session: Session, index: int, addr: str) -> InterfacePrimitives:
        return InterfacePrimitives(
            interface=InterfacesPoller._get_interface_descr(session, index),
            ip_addr=addr,
            mask=InterfacesPoller._get_interface_mask(session, addr),
            status=InterfacesPoller._get_interface_status(session, index),
            speed=InterfacesPoller._get_interface_speed(session, index),
            int_type=InterfacesPoller._get_interface_type(session, index),
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
