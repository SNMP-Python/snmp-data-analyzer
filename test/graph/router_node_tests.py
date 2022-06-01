from test.graph.mothers.routers_mother import RouterMother

from graph.router_node import RouterNode


def test_router_node_equals_itself():
    routers = RouterMother.get_one_router()
    router_node = RouterNode(router=routers[0])
    assert router_node == router_node


def test_router_node_equals_instance():
    first_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    second_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    assert first_router_node == second_router_node


def test_router_node_not_equals_different_instance():
    first_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    second_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    second_router_node.router.sys_name.name = "router-2"
    assert first_router_node != second_router_node


def test_router_node_with_adjacents_equals_instance():
    first_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    second_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    adjacent_router_node = RouterNode(router=RouterMother.get_one_router()[0])
    adjacent_router_node.router.sys_name.name = "router-2"
    first_router_node.add_adjacent(adjacent_router_node)
    second_router_node.add_adjacent(adjacent_router_node)
    assert first_router_node == second_router_node
