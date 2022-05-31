from parser.router_parser import RouterParser
from parser.router_parser_imp import RouterParserImp
from searcher.router_searcher import RouterSearcher
from searcher.snmp_router_searcher import SNMPRouterSearcher


def main():
    ip_addr = get_ip_addr_from_input()
    searcher: RouterSearcher = SNMPRouterSearcher(ip_addr=ip_addr)
    parser: RouterParser = RouterParserImp(primitives=searcher.get_router_primitives())
    list_routers = parser.get_routers()
    for router in list_routers:
        print(f"Router sys name: {router.sys_name}")
        print("\tInterfaces:")
        for interface in router.interfaces:
            print(f"\t\t{interface.name}:")
            print(f"\t\t\tStatus: {interface.status.name}:")
            print(f"\t\t\tIp: {interface.network.ip}:")
            print(f"\t\t\tMask: {interface.network.netmask}:")
            print(f"\t\t\tType: {interface.type_interface}:")
            print(f"\t\t\tSpeed: {interface.speed}:")
        print("\tRouting table:")
        for table_entry in router.routing_table:
            print(f"\t\tNetwork: {table_entry.network.ip}:")
            print(f"\t\tMask: {table_entry.network.netmask}:")
            print(f"\t\tNext Hop: {table_entry.next_hop}:")


def get_ip_addr_from_input() -> str:
    ip_addr = input("Please, insert ip address:")
    return ip_addr


if __name__ == "__main__":
    main()
