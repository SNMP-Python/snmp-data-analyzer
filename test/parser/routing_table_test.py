from parser.exceptions.invalid_ip import InvalidIpException
from parser.exceptions.invalid_mask import InvalidMaskException
from parser.router_parser_imp import RouterParserImp
from parser.value_objects.routing_table_entry import RoutingTableEntry
from test.parser.mothers.route_primitive_mother import RoutePrimitiveMother
from test.parser.mothers.router_primitive_mother import RouterPrimitiveMother

import pytest
from netaddr import IPAddress, IPNetwork


def test_empty_network_throws_invalid_ip_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(network="")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_invalid_network_throws_invalid_ip_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(network="2.2.2.2.2")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_empty_mask_throws_invalid_mask_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(mask="")
    with pytest.raises(InvalidMaskException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_invalid_mask_throws_invalid_mask_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(
        mask="255.255.255.255.255255.255.255.255.255"
    )
    with pytest.raises(InvalidMaskException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_empty_ip_next_hop_throws_invalid_ip_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(next_hop="")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_invalid_ip_next_hop_throws_invalid_ip_exception():
    router_table = RoutePrimitiveMother.get_list_of_one_route(next_hop="1.a.2.b")
    with pytest.raises(InvalidIpException):
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        ).get_routers()


def test_valid_parameters_returns_correct_route_table_value():
    router_table = RoutePrimitiveMother.get_list_of_one_route(
        network="10.1.0.0", mask="255.255.0.0", next_hop="10.2.0.1"
    )
    table_param = (
        RouterParserImp(
            RouterPrimitiveMother.get_one_router(routing_table=router_table)
        )
        .get_routers()[0]
        .routing_table[0]
    )
    assert table_param == RoutingTableEntry(
        network=IPNetwork("10.1.0.0/16"), next_hop=IPAddress("10.2.0.1")
    )
