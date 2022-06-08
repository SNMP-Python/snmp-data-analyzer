from test.graph.mothers.routers_mother import RouterMother

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode
from test.graph.utils import make_adjacent


def test_graph_creator_empty_router_list_outputs_empty_set():
    graph_creator = GraphCreatorImp([])
    assert graph_creator.get_graph() == []


def test_graph_creator_one_router_outputs_expected_graph():
    router = RouterMother.get_one_router()
    graph_creator = GraphCreatorImp([router])
    router_node = RouterNode(router=router)

    expected_graph = [router_node]
    actual_graph = graph_creator.get_graph()
    assert actual_graph == expected_graph


def test_graph_creator_two_routers_cycled_output_expected_graph():
    first_router, second_router = RouterMother.get_two_routers_in_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)

    make_adjacent(first_router_node, [second_router_node])
    make_adjacent(second_router_node, [first_router_node])

    expected_graph = [first_router_node, second_router_node]
    actual_graph = graph_creator.get_graph()
    assert actual_graph == expected_graph


def test_graph_creator_three_routers_without_cycle_output_expected_graph():
    (
        first_router,
        second_router,
        third_router,
    ) = RouterMother.get_three_routers_without_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router])
    first_router_node = RouterNode(router=first_router)
    third_router_node = RouterNode(router=third_router)
    second_router_node = RouterNode(router=second_router)

    make_adjacent(first_router_node, [second_router_node])
    make_adjacent(second_router_node, [first_router_node, third_router_node])
    make_adjacent(third_router_node, [second_router_node])

    expected_graph = [first_router_node, second_router_node, third_router_node]
    actual_graph = graph_creator.get_graph()

    assert actual_graph == expected_graph


def test_graph_creator_three_routers_cycled_output_expected_graph():
    (
        first_router,
        second_router,
        third_router,
    ) = RouterMother.get_three_routers_in_cycle()
    graph_creator = GraphCreatorImp([first_router, second_router, third_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)
    third_router_node = RouterNode(router=third_router)

    make_adjacent(first_router_node, [second_router_node, third_router_node])
    make_adjacent(second_router_node, [first_router_node, third_router_node])
    make_adjacent(third_router_node, [first_router_node, second_router_node])

    expected_graph = [first_router_node, second_router_node, third_router_node]
    actual_graph = graph_creator.get_graph()
    assert actual_graph == expected_graph


def test_graph_creator_four_routers_cycled_output_expected_graph():
    (
        first_router,
        second_router,
        third_router,
        fourth_router,
    ) = RouterMother.get_four_routers_in_cycle()
    graph_creator = GraphCreatorImp(
        [first_router, second_router, third_router, fourth_router]
    )
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)
    third_router_node = RouterNode(router=third_router)
    fourth_router_node = RouterNode(router=fourth_router)

    make_adjacent(first_router_node, [second_router_node, third_router_node])
    make_adjacent(
        second_router_node,
        [first_router_node, third_router_node, fourth_router_node],
    )
    make_adjacent(
        third_router_node,
        [first_router_node, second_router_node, fourth_router_node],
    )
    make_adjacent(fourth_router_node, [second_router_node, third_router_node])

    expected_graph = [
        first_router_node,
        second_router_node,
        third_router_node,
        fourth_router_node,
    ]
    actual_graph = graph_creator.get_graph()
    assert actual_graph == expected_graph


def test_graph_creator_four_routers_three_networks_output_expected_graph():
    (
        first_router,
        second_router,
        third_router,
        fourth_router,
    ) = RouterMother.get_four_routers_in_three_networks()
    graph_creator = GraphCreatorImp(
        [first_router, second_router, third_router, fourth_router]
    )
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router)
    third_router_node = RouterNode(router=third_router)
    fourth_router_node = RouterNode(router=fourth_router)

    make_adjacent(
        first_router_node,
        [second_router_node, fourth_router_node, third_router_node],
    )
    make_adjacent(
        second_router_node,
        [first_router_node, fourth_router_node, third_router_node],
    )
    make_adjacent(third_router_node, [first_router_node, second_router_node])
    make_adjacent(fourth_router_node, [first_router_node, second_router_node])

    expected_graph = [
        first_router_node,
        second_router_node,
        third_router_node,
        fourth_router_node,
    ]
    actual_graph = graph_creator.get_graph()
    assert actual_graph == expected_graph
