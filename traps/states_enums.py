from enum import Enum

ROUTER_ID_MIB = ' SNMPv2-SMI::mib-2.14.1.1 '
INTERFACE_ID_MIB = ' SNMPv2-SMI::mib-2.14.7.1.1 '

class OSPFStatesMIB(Enum):
    DOWN = ' SNMPv2-SMI::mib-2.14.10.1.6 = 1\n'
    ATTEMPT = ' SNMPv2-SMI::mib-2.14.10.1.6 = 2\n'
    INIT = ' SNMPv2-SMI::mib-2.14.10.1.6 = 3\n'
    TWO_WAY = ' SNMPv2-SMI::mib-2.14.10.1.6 = 4\n'
    EXCHANGE_START= ' SNMPv2-SMI::mib-2.14.10.1.6 = 5\n'
    EXCHANGE = ' SNMPv2-SMI::mib-2.14.10.1.6 = 6\n'
    LOADING = ' SNMPv2-SMI::mib-2.14.10.1.6 = 7\n'
    FULL = ' SNMPv2-SMI::mib-2.14.10.1.6 = 8\n'

class InterfaceStateMIB(Enum):
    DOWN = ' SNMPv2-SMI::mib-2.14.7.1.12 = 1\n'
    LOOPBACK = ' SNMPv2-SMI::mib-2.14.7.1.12 = 2\n'
    WAITING = ' SNMPv2-SMI::mib-2.14.7.1.12 = 3\n'
    POINT_TO_POINT = ' SNMPv2-SMI::mib-2.14.7.1.12 = 4\n'
    DESIGNATED_ROUTER = ' SNMPv2-SMI::mib-2.14.7.1.12 = 5\n'
    BACKUP_DESIGNATED_ROUTER = ' SNMPv2-SMI::mib-2.14.7.1.12 = 6\n'
    OTHER_DESIGNATED_ROUTER = ' SNMPv2-SMI::mib-2.14.7.1.12 = 7\n'

class InterfacesMIB(Enum):
    ROUTER_ID = ' SNMPv2-SMI::mib-2.14.1.1 '
    INTERFACE_IP = ' SNMPv2-SMI::mib-2.14.7.1.1 '

class MIBType(Enum):
    NBR_STATE_CHANGE = ' SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::mib-2.14.16.2.2'
    IF_STATE_CHANGE = ' SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::mib-2.14.16.2.16'