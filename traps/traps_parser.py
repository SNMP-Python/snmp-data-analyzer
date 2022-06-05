from mibs_parser import OSPFStatesMIB, InterfacesMIB, MIBType, InterfaceStateMIB


def get_header(events):
    header = events[0]
    events = events[1:]
    return header, events

event_switch = {
    OSPFStatesMIB.DOWN.value: "STATE: FULL",
    OSPFStatesMIB.ATTEMPT.value: "STATE: ATTEMPT",
    OSPFStatesMIB.INIT.value: "STATE: INIT",
    OSPFStatesMIB.TWO_WAY.value: "STATE: TWO_WAY",
    OSPFStatesMIB.EXCHANGE_START.value: "STATE: EXCHANGE_START",
    OSPFStatesMIB.EXCHANGE.value: "STATE: EXCHANGE",
    OSPFStatesMIB.LOADING.value: "STATE: LOADING",
    OSPFStatesMIB.FULL.value: "STATE: FULL",
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
    InterfacesMIB.ROUTER_ID.value: ' SNMPv2-SMI::mib-2.14.1.1 ',
    InterfacesMIB.INTERFACE_IP.value: ' SNMPv2-SMI::mib-2.14.7.1.1 '
}

def get_and_print_ids(event):
    if event.split('=')[0] == ' SNMPv2-SMI::mib-2.14.1.1 ':
        print('ROUTER ID: ' + event.split('=')[1] )
    if event.split('=')[0] == ' SNMPv2-SMI::mib-2.14.7.1.1 ':
        print('INTERFACE ID: ' + event.split('=')[1] )

def parse_line(line):
    events = line.split(',')
    header, events = get_header(events)
    if events:
        print('----------------------------------------------------')
        print(mib_type_switch.get(events[0]))
        for event in events:
            get_and_print_ids(event)
            print(event_switch.get(event,""), end="")

        print()
        print('----------------------------------------------------')

if __name__ == "__main__":
    file = open('logs.txt')
    for line in file:
        parse_line(line)

