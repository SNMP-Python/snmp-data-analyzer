from test.graph.mothers.routers_mother import RouterMother

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode


def test_graph_creator_empty_router_list_outputs_empty_set():
    graph_creator = GraphCreatorImp([])
    assert graph_creator.get_graph() == frozenset()


def test_graph_creator_one_router_outputs_expected_graph():
    router = RouterMother.get_one_router()
    graph_creator = GraphCreatorImp([router])
    router_node = RouterNode(router=router)

    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == 1
    assert router_node in actual_graph


def test_graph_creator_two_routers_cycled_output_expected_graph():
    first_router, second_router = RouterMother.get_two_routers_in_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    first_router_node.add_adjacent(second_router_node)

    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == 2
    assert first_router_node in actual_graph
    assert second_router_node in actual_graph


def test_graph_creator_three_routers_without_cycle_output_expected_graph():
    first_router, second_router, third_router = RouterMother.get_three_routers_without_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router])
    first_router_node = RouterNode(router=first_router)
    third_router_node = RouterNode(router=third_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node, third_router_node])
    first_router_node.add_adjacent(second_router_node)
    third_router_node.add_adjacent(second_router_node)

    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == 3
    assert first_router_node in actual_graph
    assert second_router_node in actual_graph
    assert third_router_node in actual_graph


def test_graph_creator_three_routers_cycled_output_expected_graph():
    first_router, second_router, third_router = RouterMother.get_three_routers_in_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    third_router_node = RouterNode(router=third_router, adjacents=[first_router_node, second_router_node])
    first_router_node.add_adjacent(second_router_node)
    first_router_node.add_adjacent(third_router_node)
    second_router_node.add_adjacent(third_router_node)

    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == 3
    assert first_router_node in actual_graph
    assert second_router_node in actual_graph
    assert third_router_node in actual_graph


def test_graph_creator_four_routers_cycled_output_expected_graph():
    first_router, second_router, third_router, fourth_router = RouterMother.get_four_routers_in_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router, fourth_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)
    third_router_node = RouterNode(router=third_router)
    fourth_router_node = RouterNode(router=fourth_router)

    first_router_node.add_adjacent(second_router_node)
    first_router_node.add_adjacent(third_router_node)

    second_router_node.add_adjacent(first_router_node)
    second_router_node.add_adjacent(third_router_node)
    second_router_node.add_adjacent(fourth_router_node)

    third_router_node.add_adjacent(first_router_node)
    third_router_node.add_adjacent(second_router_node)
    third_router_node.add_adjacent(fourth_router_node)

    fourth_router_node.add_adjacent(second_router_node)
    fourth_router_node.add_adjacent(third_router_node)

    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == 4
    assert first_router_node in actual_graph
    assert second_router_node in actual_graph
    assert third_router_node in actual_graph
    assert fourth_router_node in actual_graph


def test_graph_creator_four_routers_three_networks_output_expected_graph():
    first_router, second_router, third_router, fourth_router = RouterMother.get_four_routers_in_three_networks()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router, fourth_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)
    third_router_node = RouterNode(router=third_router)
    fourth_router_node = RouterNode(router=fourth_router)

    first_router_node.add_adjacent(second_router_node)
    first_router_node.add_adjacent(fourth_router_node)
    first_router_node.add_adjacent(third_router_node)

    second_router_node.add_adjacent(first_router_node)
    second_router_node.add_adjacent(third_router_node)
    second_router_node.add_adjacent(fourth_router_node)

    third_router_node.add_adjacent(first_router_node)
    third_router_node.add_adjacent(second_router_node)

    fourth_router_node.add_adjacent(first_router_node)
    fourth_router_node.add_adjacent(second_router_node)

    actual_graph = graph_creator.get_graph()

    assert first_router_node in actual_graph
    assert second_router_node in actual_graph
    assert third_router_node in actual_graph
    assert fourth_router_node in actual_graph
