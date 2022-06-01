from __future__ import absolute_import

from typing import List, Set

import pytest

from searcher.exceptions.non_reachable_host import NonReachableHostException
from searcher.primitives.interface_primitives import InterfacePrimitives
from searcher.primitives.route_primitives import RoutePrimitives
from searcher.snmp_client import SNMPClient

snmp_client = SNMPClient()


def test_non_reachable_host_throws_non_reachable_host_exception():
    with pytest.raises(NonReachableHostException):
        snmp_client.get_router_primitives("12.34.56.78")


def test_reachable_host_returns_name():
    router_primitives = snmp_client.get_router_primitives("10.0.0.2")
    assert router_primitives.sys_name == "R1"


def test_reachable_host_returns_interfaces():
    router_primtives = snmp_client.get_router_primitives("10.0.0.2")
    assert set(router_primtives.interfaces) == _get_expected_interface_primitives()


def test_reachable_host_returns_routing_table():
    router_primitives = snmp_client.get_router_primitives("10.0.0.2")
    assert set(router_primitives.routing_table) == _get_expected_routing_table()


def test_reachable_host_returns_ospf_id():
    router_primitives = snmp_client.get_router_primitives("10.0.0.2")
    assert router_primitives.ospf_id == "13.0.0.1"


def test_reachable_host_returns_ospf_neighbors():
    router_primitives = snmp_client.get_router_primitives('11.0.0.2')
    assert set(router_primitives.neighbors) == {'11.0.0.2'}


def _get_expected_routing_table() -> Set[RoutePrimitives]:
    return {
        _get_r1_route_primitives(),
        _get_r2_route_primitives(),
        _get_r3_route_primitives(),
        _get_r4_route_primitives(),
    }


def _get_expected_interface_primitives() -> Set[InterfacePrimitives]:
    return {
        _get_fa1_interface_primitives(),
        _get_fa2_interface_primitives(),
        _get_loopback_interface_primitives(),
    }


def _get_fa1_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface="FastEthernet0/0",
        ip_addr="11.0.0.1",
        mask="255.255.255.0",
        status="1",
        speed="100000000",
        int_type="6",
    )


def _get_fa2_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface="FastEthernet0/1",
        ip_addr="10.0.0.2",
        mask="255.255.255.0",
        status="1",
        speed="100000000",
        int_type="6",
    )


def _get_loopback_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface="Loopback0",
        ip_addr="13.0.0.1",
        mask="255.255.255.0",
        status="up1",
        speed="4294967295",
        int_type="24",
    )


def _get_r1_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network="10.0.0.0", mask="255.255.255.0", next_hop="0.0.0.0", route_type="3")


def _get_r2_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network="11.0.0.0", mask="255.255.255.0", next_hop="0.0.0.0", route_type="3")


def _get_r3_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network="12.0.0.0", mask="255.255.255.0", next_hop="11.0.0.2", route_type="4")


def _get_r4_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network="13.0.0.0", mask="255.255.255.0", next_hop="0.0.0.0", route_type="3")
