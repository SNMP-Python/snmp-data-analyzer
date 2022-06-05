import states_enums
from dictionaries import mib_type_switch, event_switch

def print_div():
    print('----------------------------------------------------')

def print_event_type(events):
    print(mib_type_switch.get(events[0]))

def print_if_or_router_state(event):
    print(event_switch.get(event, ""), end="")

def get_header(events):
    header = events[0]
    events = events[1:]
    return header, events

def get_and_print_ids(event):
    if event.split('=')[0] == states_enums.ROUTER_ID_MIB:
        print('ROUTER ID: ' + event.split('=')[1] )
    if event.split('=')[0] == states_enums.INTERFACE_ID_MIB:
        print('INTERFACE ID: ' + event.split('=')[1] )

def parse_line(line):
    events = line.split(',')
    header, events = get_header(events)
    if events:
        print_div()
        print_event_type(events)
        for event in events:
            get_and_print_ids(event)
            print_if_or_router_state(event)

        print()

if __name__ == "__main__":
    file = open('logs.txt')
    for line in file:
        parse_line(line)

    print_div()



