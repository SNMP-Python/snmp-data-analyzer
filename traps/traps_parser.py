from mibs_parser import StatesMIB, InterfacesMIB, MIBType


def get_header(events):
    header = events[0]
    events = events[1:]
    return header, events

event_switch = {
    StatesMIB.DOWN.value: "STATE: FULL",
    StatesMIB.ATTEMPT.value: "STATE: ATTEMPT",
    StatesMIB.INIT.value: "STATE: INIT",
    StatesMIB.TWO_WAY.value: "STATE: TWO_WAY",
    StatesMIB.EXCHANGE_START.value: "STATE: EXCHANGE_START",
    StatesMIB.EXCHANGE.value: "STATE: EXCHANGE",
    StatesMIB.LOADING.value: "STATE: LOADING",
    StatesMIB.FULL.value: "STATE: FULL",
}

mib_type_switch = {
    MIBType.IF_STATE_CHANGE.value: "IF STATE CHANGE",
    MIBType.NBR_STATE_CHANGE.value: "NEIGHBOR STATE CHANGE"
}

def parse_line(line):
    events = line.split(',')
    header, events = get_header(events)
    if events:
        print('----------------------------------------------------')
        print(mib_type_switch.get(events[0]))
        for event in events:
            print(event_switch.get(event,""), end="")

        print()
        print('----------------------------------------------------')

if __name__ == "__main__":
    file = open('logs.txt')
    for line in file:
        parse_line(line)

