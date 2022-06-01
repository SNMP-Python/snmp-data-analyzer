from parser.router_parser_imp import RouterParserImp
from test.parser.mothers.router_primitive_mother import RouterPrimitiveMother

from graph.graph_creator_imp import GraphCreatorImp
from graph.router_node import RouterNode


def test_empty_router_list_outputs_empty_set():
    graph_creator = GraphCreatorImp([])
    assert graph_creator.get_graph() == frozenset()


def test_one_router_outputs_expected_graph():
    router_parser = RouterParserImp(RouterPrimitiveMother.get_one_router())
    routers = router_parser.get_routers()
    graph_creator = GraphCreatorImp(routers)

    expected_graph = frozenset({RouterNode(router=routers[0])})
    actual_graph = graph_creator.get_graph()

    assert len(actual_graph) == len(expected_graph)
    assert all(x in expected_graph for x in actual_graph)
