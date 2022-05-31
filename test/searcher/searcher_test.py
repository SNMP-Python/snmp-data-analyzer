from unittest.mock import Mock

from searcher.client import Client
from searcher.snmp_router_searcher import SNMPRouterSearcher
from test.shared.router_primitive_mother import RouterPrimitiveMother


def test_one_item_returns_correct_values():
    expected_router = RouterPrimitiveMother.get()
    client: Client = Mock()
    client.get_router_primitives.return_value = expected_router
    searcher = SNMPRouterSearcher(
        ip_addr=expected_router.interfaces[0].ip_addr, client=client
    )
    assert frozenset({expected_router}) == searcher.get_router_primitives()


def test_complete_two_nodes_graph():
    first_router = RouterPrimitiveMother.get_router_with(
        id_router=1, neighbors=["10.0.0.2"], ospf_id="10.0.0.1"
    )
    second_router = RouterPrimitiveMother.get_router_with(
        id_router=2, neighbors=["10.0.0.1"], ospf_id="10.0.0.2"
    )
    client: Client = Mock()
    client.get_router_primitives.side_effect = [first_router, second_router]
    searcher = SNMPRouterSearcher(ip_addr="10.0.0.1", client=client)
    assert frozenset({first_router, second_router}) == searcher.get_router_primitives()


def test_incomplete_three_nodes_graph():
    first_router = RouterPrimitiveMother.get_router_with(
        id_router=1, neighbors=["10.0.1.2"], ospf_id="10.0.0.1"
    )
    second_router = RouterPrimitiveMother.get_router_with(
        id_router=2, neighbors=["10.0.0.1", "10.0.1.3"], ospf_id="10.0.1.2"
    )
    third_router = RouterPrimitiveMother.get_router_with(
        id_router=3, neighbors=["10.0.1.2"], ospf_id="10.0.1.3"
    )
    client: Client = Mock()
    client.get_router_primitives.side_effect = [
        first_router,
        second_router,
        third_router,
    ]
    searcher = SNMPRouterSearcher(ip_addr="10.0.0.1", client=client)
    assert (
        frozenset({first_router, second_router, third_router})
        == searcher.get_router_primitives()
    )


def test_complete_three_nodes_graph():
    first_router = RouterPrimitiveMother.get_router_with(
        id_router=1, neighbors=["10.0.1.2", "10.0.2.3"], ospf_id="10.0.2.1"
    )
    second_router = RouterPrimitiveMother.get_router_with(
        id_router=2, neighbors=["10.0.2.1", "10.0.2.3"], ospf_id="10.0.1.2"
    )
    third_router = RouterPrimitiveMother.get_router_with(
        id_router=3, neighbors=["10.0.1.2", "10.0.2.1"], ospf_id="10.0.2.3"
    )
    client: Client = Mock()
    client.get_router_primitives.side_effect = [
        first_router,
        third_router,
        second_router,
    ]
    searcher = SNMPRouterSearcher(ip_addr="10.0.0.1", client=client)
    assert (
        frozenset({first_router, second_router, third_router})
        == searcher.get_router_primitives()
    )


def test_complete_four_nodes_graph():
    first_router = RouterPrimitiveMother.get_router_with(
        id_router=1, neighbors=["10.0.4.2", "10.0.5.3", "10.0.5.4"], ospf_id="10.0.2.1"
    )
    second_router = RouterPrimitiveMother.get_router_with(
        id_router=2, neighbors=["10.0.2.1", "10.0.5.3", "10.0.5.4"], ospf_id="10.0.4.2"
    )
    third_router = RouterPrimitiveMother.get_router_with(
        id_router=3, neighbors=["10.0.2.1", "10.0.4.2", "10.0.5.4"], ospf_id="10.0.5.3"
    )
    fourth_router = RouterPrimitiveMother.get_router_with(
        id_router=3, neighbors=["10.0.2.1", "10.0.4.2", "10.0.5.3"], ospf_id="10.0.5.4"
    )
    client: Client = Mock()
    client.get_router_primitives.side_effect = [
        first_router,
        fourth_router,
        third_router,
        second_router,
    ]
    searcher = SNMPRouterSearcher(ip_addr="10.0.0.1", client=client)
    assert (
        frozenset({first_router, second_router, third_router, fourth_router})
        == searcher.get_router_primitives()
    )
