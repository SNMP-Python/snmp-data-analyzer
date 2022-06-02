from test.graph.mothers.routers_mother import RouterMother

import pytest

from graph.router_node import RouterNode


def test_router_node_compared_with_other_type_raises_type_error():
    router_node = RouterNode(RouterMother.get_one_router())
    with pytest.raises(TypeError):
        _ = router_node < 6


def test_router_node_equals_itself():
    router_node = RouterNode(router=RouterMother.get_one_router())
    assert router_node == router_node


def test_router_node_without_adjacents_equals_instance():
    first_router_node = RouterNode(router=RouterMother.get_one_router())
    second_router_node = RouterNode(router=RouterMother.get_one_router())

    assert first_router_node == second_router_node


def test_router_node_without_adjacents_not_equals_different_instance():
    first_router, second_router = RouterMother.get_two_routers_in_cycle()
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)

    assert first_router_node != second_router_node


def test_router_node_adjacents_not_equals_instance():
    first_router, second_router = RouterMother.get_two_routers_in_cycle()
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    second_router_node.add_adjacent(first_router_node)

    assert first_router_node != second_router_node


def test_router_node_with_cycle_adjacents_not_equals_instances():
    first_router, second_router, third_router = RouterMother.get_three_routers_in_cycle()
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    third_router_node = RouterNode(router=third_router, adjacents=[first_router_node, second_router_node])

    first_router_node.add_adjacent(second_router_node)
    first_router_node.add_adjacent(third_router_node)
    second_router_node.add_adjacent(third_router_node)

    assert first_router_node != second_router_node
    assert second_router_node != third_router_node
    assert first_router_node != third_router_node


def test_router_node_first_with_cycle_equals_instance():
    first_router, second_router, third_router = RouterMother.get_three_routers_in_cycle()
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    third_router_node = RouterNode(router=third_router, adjacents=[first_router_node, second_router_node])

    first_router_node.add_adjacent(second_router_node)
    first_router_node.add_adjacent(third_router_node)
    second_router_node.add_adjacent(third_router_node)

    equal_first_router_node = RouterNode(first_router, adjacents=[second_router_node, third_router_node])

    assert equal_first_router_node == first_router_node
