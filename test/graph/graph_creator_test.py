from test.graph.mothers.routers_mother import RouterMother

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode


def test_empty_router_list_outputs_empty_set():
    graph_creator = GraphCreatorImp([])
    assert graph_creator.get_graph() == frozenset()


def test_one_router_outputs_expected_graph():
    routers = RouterMother.get_one_router()
    graph_creator = GraphCreatorImp(routers)

    expected_graph = frozenset({RouterNode(router=routers[0])})
    actual_graph = graph_creator.get_graph()
    assert len(actual_graph) == len(expected_graph)
    assert expected_graph == actual_graph


# def test_two_routers_output_expected_graph():
#     routers = RouterMother.get_two_routers()
#     graph_creator = GraphCreatorImp(routers)
#     first_router_node = RouterNode(router=routers[0])
#     second_router_node = RouterNode(router=routers[1], adjacents={first_router_node})
#     first_router_node.add_adjacent(second_router_node)
#     expected_graph = frozenset(
#         {
#             RouterNode(router=routers[0], adjacents={second_router_node}),
#             RouterNode(router=routers[1], adjacents={first_router_node}),
#         }
#     )
#     actual_graph = graph_creator.get_graph()
#
#     assert len(actual_graph) == len(expected_graph)
#     assert expected_graph == actual_graph
