from enum import Enum

class StatesMIB(Enum):
    DOWN = ' SNMPv2-SMI::mib-2.14.10.1.6 = 1\n'
    ATTEMPT = ' SNMPv2-SMI::mib-2.14.10.1.6 = 2\n'
    INIT = ' SNMPv2-SMI::mib-2.14.10.1.6 = 3\n'
    TWO_WAY = ' SNMPv2-SMI::mib-2.14.10.1.6 = 4\n'
    EXCHANGE_START= ' SNMPv2-SMI::mib-2.14.10.1.6 = 5\n'
    EXCHANGE = ' SNMPv2-SMI::mib-2.14.10.1.6 = 6\n'
    LOADING = ' SNMPv2-SMI::mib-2.14.10.1.6 = 7\n'
    FULL = ' SNMPv2-SMI::mib-2.14.10.1.6 = 8\n'

class InterfacesMIB(Enum):
    ROUTER_ID = ' SNMPv2-SMI::mib-2.14.1.1 '
    INTERFACE_IP = ' SNMPv2-SMI::mib-2.14.7.1.1 '

class MIBType(Enum):
    NBR_STATE_CHANGE = ' SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::mib-2.14.16.2.2'
    IF_STATE_CHANGE = ' SNMPv2-MIB::snmpTrapOID.0 = SNMPv2-SMI::mib-2.14.16.2.16'