from states_enums import OSPFStatesMIB, InterfaceStateMIB, MIBType, InterfacesMIB

event_switch = {
    OSPFStatesMIB.DOWN.value: "OSPF ROUTER STATE: FULL",
    OSPFStatesMIB.ATTEMPT.value: "OSPF ROUTER STATE: ATTEMPT",
    OSPFStatesMIB.INIT.value: "OSPF ROUTER STATE: INIT",
    OSPFStatesMIB.TWO_WAY.value: "OSPF ROUTER STATE: TWO_WAY",
    OSPFStatesMIB.EXCHANGE_START.value: "OSPF ROUTER STATE: EXCHANGE_START",
    OSPFStatesMIB.EXCHANGE.value: "OSPF ROUTER STATE: EXCHANGE",
    OSPFStatesMIB.LOADING.value: "OSPF ROUTER STATE: LOADING",
    OSPFStatesMIB.FULL.value: "OSPF ROUTER STATE: FULL",
    InterfaceStateMIB.DOWN.value: "INTERFACE STATE: DOWN",
    InterfaceStateMIB.LOOPBACK.value: "INTERFACE STATE: LOOPBACK",
    InterfaceStateMIB.WAITING.value: "INTERFACE STATE: WAITING",
    InterfaceStateMIB.POINT_TO_POINT.value: "INTERFACE STATE: POINT_TO_POINT",
    InterfaceStateMIB.DESIGNATED_ROUTER.value: "INTERFACE STATE: DESIGNATED_ROUTER",
    InterfaceStateMIB.BACKUP_DESIGNATED_ROUTER.value: "INTERFACE STATE: BACKUP_DESIGNATED_ROUTER",
    InterfaceStateMIB.OTHER_DESIGNATED_ROUTER   .value: "INTERFACE STATE: OTHER_DESIGNATED_ROUTER",
}

mib_type_switch = {
    MIBType.IF_STATE_CHANGE.value: "IF STATE CHANGE",
    MIBType.NBR_STATE_CHANGE.value: "NEIGHBOR STATE CHANGE"
}

interfaces_mib_switch = {
    InterfacesMIB.ROUTER_ID.value: 'SNMPv2-SMI::mib-2.14.1.1',
    InterfacesMIB.INTERFACE_IP.value: 'SNMPv2-SMI::mib-2.14.7.1.1'
}
