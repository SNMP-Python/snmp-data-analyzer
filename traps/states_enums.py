from enum import Enum

ROUTER_ID_MIB = 'SNMPv2-SMI::mib-2.14.1.1'
INTERFACE_ID_MIB = 'SNMPv2-SMI::mib-2.14.7.1.1'


class OSPFStatesMIB(Enum):
    DOWN = 'SNMPv2-SMI::mib-2.14.10.1.6 1'
    ATTEMPT = 'SNMPv2-SMI::mib-2.14.10.1.6 2'
    INIT = 'SNMPv2-SMI::mib-2.14.10.1.6 3'
    TWO_WAY = 'SNMPv2-SMI::mib-2.14.10.1.6 4'
    EXCHANGE_START = 'SNMPv2-SMI::mib-2.14.10.1.6 5'
    EXCHANGE = 'SNMPv2-SMI::mib-2.14.10.1.6 6'
    LOADING = 'SNMPv2-SMI::mib-2.14.10.1.6 7'
    FULL = 'SNMPv2-SMI::mib-2.14.10.1.6 8'


class InterfaceStateMIB(Enum):
    DOWN = 'SNMPv2-SMI::mib-2.14.7.1.12 1'
    LOOPBACK = 'SNMPv2-SMI::mib-2.14.7.1.12 2'
    WAITING = 'SNMPv2-SMI::mib-2.14.7.1.12 3'
    POINT_TO_POINT = 'SNMPv2-SMI::mib-2.14.7.1.12 4'
    DESIGNATED_ROUTER = 'SNMPv2-SMI::mib-2.14.7.1.12 5'
    BACKUP_DESIGNATED_ROUTER = 'SNMPv2-SMI::mib-2.14.7.1.12 6'
    OTHER_DESIGNATED_ROUTER = 'SNMPv2-SMI::mib-2.14.7.1.12 7'


class InterfacesMIB(Enum):
    ROUTER_ID = 'SNMPv2-SMI::mib-2.14.1.1'
    INTERFACE_IP = 'SNMPv2-SMI::mib-2.14.7.1.1'


class MIBType(Enum):
    NBR_STATE_CHANGE = 'SNMPv2-MIB::snmpTrapOID.0 SNMPv2-SMI::mib-2.14.16.2.2'
    IF_STATE_CHANGE = 'SNMPv2-MIB::snmpTrapOID.0 SNMPv2-SMI::mib-2.14.16.2.16'
