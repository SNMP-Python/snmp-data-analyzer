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
        snmp_client.get_router_primitives('12.34.56.78')


def test_reachable_host_returns_name():
    router_primitives = snmp_client.get_router_primitives('10.0.0.2')
    assert 'R1' == router_primitives.sys_name


def test_reachable_host_returns_interfaces():
    router_primtives = snmp_client.get_router_primitives('10.0.0.2')
    assert _get_expected_interface_primitives() == set(router_primtives.interfaces)


def test_reachable_host_returns_routing_table():
    router_primitives = snmp_client.get_router_primitives('10.0.0.2')
    assert _get_expected_routing_table() == set(router_primitives.routing_table)


def _get_expected_routing_table() -> Set[RoutePrimitives]:
    return {_get_r1_route_primitives(), _get_r2_route_primitives()}


def _get_expected_interface_primitives() -> Set[InterfacePrimitives]:
    return {_get_fa1_interface_primitives(), _get_fa2_interface_primitives(), _get_loopback_interface_primitives()}


def _get_fa1_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface='FastEthernet0/0',
        ip_addr='11.0.0.1',
        mask='255.255.255.0',
        status='1',
        speed='100000000',
        int_type='6',
    )


def _get_fa2_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface='FastEthernet0/1',
        ip_addr='10.0.0.2',
        mask='255.255.255.0',
        status='1',
        speed='100000000',
        int_type='6',
    )


def _get_loopback_interface_primitives() -> InterfacePrimitives:
    return InterfacePrimitives(
        interface='Loopback0', ip_addr='13.0.0.1', mask='255.255.255.0', status='up1', speed='4294967295', int_type='24'
    )


def _get_r1_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network='', mask='', next_hop='', route_type='')


def _get_r2_route_primitives() -> RoutePrimitives:
    return RoutePrimitives(network='', mask='', next_hop='', route_type='')
