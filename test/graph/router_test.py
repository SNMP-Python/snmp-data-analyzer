from netaddr import IPAddress

from test.graph.mothers.routers_mother import RouterMother


def test_router_is_connected_to_two_networks():
    router = RouterMother.get_one_router()
    assert router.is_connected(IPAddress("10.0.0.0"))
    assert router.is_connected(IPAddress("12.0.0.0"))


def test_router_is_not_connected_to_network():
    router = RouterMother.get_one_router()
    assert router.is_connected(IPAddress("11.0.0.0")) is False
