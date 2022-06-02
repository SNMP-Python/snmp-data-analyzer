from test.graph.mothers.routers_mother import RouterMother

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode


def test_empty_router_list_outputs_empty_set():
    graph_creator = GraphCreatorImp([])
    assert graph_creator.get_graph() == frozenset()


def test_one_router_outputs_expected_graph():
    router = RouterMother.get_one_router()
    graph_creator = GraphCreatorImp([router])

    expected_graph = frozenset({RouterNode(router=router)})
    actual_graph = graph_creator.get_graph()
    assert len(actual_graph) == len(expected_graph)
    assert expected_graph == actual_graph


def test_two_routers_output_expected_graph():
    first_router, second_router = RouterMother.get_two_routers()
    graph_creator = GraphCreatorImp([first_router, second_router])
    first_router_node = RouterNode(router=first_router)
    second_router_node = RouterNode(router=second_router, adjacents=[first_router_node])
    first_router_node.add_adjacent(second_router_node)
    expected_graph = frozenset(
        {
            RouterNode(router=first_router, adjacents=[second_router_node]),
            RouterNode(router=second_router, adjacents=[first_router_node]),
        }
    )
    actual_graph = graph_creator.get_graph()

    assert expected_graph == actual_graph
