from netaddr import IPAddress, IPNetwork

from distance.distance_calculator_imp import (
    DistanceCalculatorImp,
    _discard_point,
)
from distance.path import Path
from test.distance.mothers.graph_mothers.one_router_graph_mother import (
    OneRouterGraphMother,
)
from test.distance.mothers.graph_mothers.three_routers_graph_mother import (
    ThreeRoutersGraphMother,
)
from test.distance.mothers.graph_mothers.two_routers_graph_mother import (
    TwoRoutersGraphMother,
)
from test.distance.mothers.graph_point_mother import GraphPointMother


def test_bitwise_and():
    network = IPNetwork('12.0.0.2/24')
    expected = IPAddress('12.0.0.0')
    assert network.network & network.netmask == expected


def test_should_discard_points():
    same_source_destination = GraphPointMother.get_point_for_graph(
        '6.0.0.6', '6.0.0.6'
    )
    assert _discard_point(same_source_destination)


def test_should_not_discard_points():
    not_same_source_destination = GraphPointMother.get_point_for_graph(
        '6.0.0.6', '4.0.0.28'
    )
    assert not _discard_point(not_same_source_destination)


def test_one_router_three_interfaces_outputs_expected_dict():
    graph = OneRouterGraphMother.get_one_router_three_interfaces_graph()
    distance_calculator = DistanceCalculatorImp(graph, '6.0.0.2')
    router = OneRouterGraphMother._get_one_router_three_interfaces()
    expected = {}

    expected_first_point = GraphPointMother.get_point_for_graph(
        '6.0.0.2', '8.0.0.5'
    )
    expected[expected_first_point] = Path([router])

    expected_second_point = GraphPointMother.get_point_for_graph(
        '8.0.0.5', '10.0.0.6'
    )
    expected[expected_second_point] = Path([router])

    expected_third_point = GraphPointMother.get_point_for_graph(
        '6.0.0.2', '10.0.0.6'
    )
    expected[expected_third_point] = Path([router])

    actual = distance_calculator.get_distances()
    assert actual == expected


def test_two_router_one_interface_each_outputs_expected_dict():
    graph = TwoRoutersGraphMother.get_two_routers_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph, '6.0.0.1')
    first_router = TwoRoutersGraphMother._get_first_router_second_test()
    second_router = TwoRoutersGraphMother._get_second_router_second_test()

    expected = {}
    expected_first_point = GraphPointMother.get_point_for_graph(
        '6.0.0.1', '6.0.0.2'
    )
    expected[expected_first_point] = Path([first_router, second_router])

    actual = distance_calculator.get_distances()
    assert actual == expected


def test_three_routers_one_interface_ascending_each_outputs_expected_dict():
    graph = (
        ThreeRoutersGraphMother.get_three_routers_one_interface_graph_ascending()
    )
    distance_calculator = DistanceCalculatorImp(graph, '6.0.0.2')
    first_router = ThreeRoutersGraphMother._get_first_router_third_test()
    second_router = ThreeRoutersGraphMother._get_second_router_third_test()
    third_router = ThreeRoutersGraphMother._get_third_router_third_test()
    expected = {}

    point_62_64 = GraphPointMother.get_point_for_graph('6.0.0.2', '6.0.0.4')
    point_62_84 = GraphPointMother.get_point_for_graph('6.0.0.2', '8.0.0.4')
    point_62_86 = GraphPointMother.get_point_for_graph('6.0.0.2', '8.0.0.6')
    point_62_108 = GraphPointMother.get_point_for_graph('6.0.0.2', '10.0.0.8')
    point_62_1010 = GraphPointMother.get_point_for_graph('6.0.0.2', '10.0.0.10')

    point_64_84 = GraphPointMother.get_point_for_graph('6.0.0.4', '8.0.0.4')
    point_64_86 = GraphPointMother.get_point_for_graph('6.0.0.4', '8.0.0.6')
    point_64_108 = GraphPointMother.get_point_for_graph('6.0.0.4', '10.0.0.8')
    point_64_1010 = GraphPointMother.get_point_for_graph('6.0.0.4', '10.0.0.10')

    point_84_86 = GraphPointMother.get_point_for_graph('8.0.0.4', '8.0.0.6')
    point_84_108 = GraphPointMother.get_point_for_graph('8.0.0.4', '10.0.0.8')
    point_84_1010 = GraphPointMother.get_point_for_graph('8.0.0.4', '10.0.0.10')

    point_86_108 = GraphPointMother.get_point_for_graph('8.0.0.6', '10.0.0.8')
    point_86_1010 = GraphPointMother.get_point_for_graph('8.0.0.6', '10.0.0.10')

    point_108_1010 = GraphPointMother.get_point_for_graph(
        '10.0.0.8', '10.0.0.10'
    )

    expected[point_62_64] = Path([first_router, second_router])
    expected[point_62_84] = Path([first_router])
    expected[point_62_86] = Path([first_router, third_router])
    expected[point_62_108] = Path([first_router, second_router])
    expected[point_62_1010] = Path([first_router, second_router, third_router])

    expected[point_64_84] = Path([second_router, first_router])
    expected[point_64_86] = Path([second_router, third_router])
    expected[point_64_108] = Path([second_router])
    expected[point_64_1010] = Path([second_router, third_router])

    expected[point_84_86] = Path([first_router, third_router])
    expected[point_84_108] = Path([first_router, second_router])
    expected[point_84_1010] = Path([first_router, second_router, third_router])

    expected[point_86_108] = Path([third_router, second_router])
    expected[point_86_1010] = Path([third_router])

    expected[point_108_1010] = Path([second_router, third_router])

    actual = distance_calculator.get_distances()
    assert actual == expected


def test_three_routers_one_interface_descending_each_outputs_expected_dict():
    graph = (
        ThreeRoutersGraphMother.get_three_routers_one_interface_graph_descending()
    )
    distance_calculator = DistanceCalculatorImp(graph, '10.0.0.10')
    first_router = ThreeRoutersGraphMother._get_first_router_third_test()
    second_router = ThreeRoutersGraphMother._get_second_router_third_test()
    third_router = ThreeRoutersGraphMother._get_third_router_third_test()
    expected = {}

    point_62_64 = GraphPointMother.get_point_for_graph('6.0.0.2', '6.0.0.4')
    point_62_84 = GraphPointMother.get_point_for_graph('6.0.0.2', '8.0.0.4')
    point_62_86 = GraphPointMother.get_point_for_graph('6.0.0.2', '8.0.0.6')
    point_62_108 = GraphPointMother.get_point_for_graph('6.0.0.2', '10.0.0.8')
    point_62_1010 = GraphPointMother.get_point_for_graph('6.0.0.2', '10.0.0.10')

    point_64_84 = GraphPointMother.get_point_for_graph('6.0.0.4', '8.0.0.4')
    point_64_86 = GraphPointMother.get_point_for_graph('6.0.0.4', '8.0.0.6')
    point_64_108 = GraphPointMother.get_point_for_graph('6.0.0.4', '10.0.0.8')
    point_64_1010 = GraphPointMother.get_point_for_graph('6.0.0.4', '10.0.0.10')

    point_84_86 = GraphPointMother.get_point_for_graph('8.0.0.4', '8.0.0.6')
    point_84_108 = GraphPointMother.get_point_for_graph('8.0.0.4', '10.0.0.8')
    point_84_1010 = GraphPointMother.get_point_for_graph('8.0.0.4', '10.0.0.10')

    point_86_108 = GraphPointMother.get_point_for_graph('8.0.0.6', '10.0.0.8')
    point_86_1010 = GraphPointMother.get_point_for_graph('8.0.0.6', '10.0.0.10')

    point_108_1010 = GraphPointMother.get_point_for_graph(
        '10.0.0.8', '10.0.0.10'
    )

    expected[point_62_64] = Path([first_router, second_router])
    expected[point_62_84] = Path([first_router])
    expected[point_62_86] = Path([first_router, third_router])
    expected[point_62_108] = Path([first_router, second_router])
    expected[point_62_1010] = Path(
        [first_router, third_router]
    )  # This one changes

    expected[point_64_84] = Path(
        [second_router, third_router, first_router]
    )  # This one changes
    expected[point_64_86] = Path(
        [second_router, first_router, third_router]
    )  # This one changes
    expected[point_64_108] = Path([second_router])
    expected[point_64_1010] = Path(
        [second_router, first_router, third_router]
    )  # This one changes

    expected[point_84_86] = Path([first_router, third_router])
    expected[point_84_108] = Path(
        [first_router, third_router, second_router]
    )  # This one changes
    expected[point_84_1010] = Path(
        [first_router, third_router]
    )  # This one changes

    expected[point_86_108] = Path([third_router, second_router])
    expected[point_86_1010] = Path([third_router])

    expected[point_108_1010] = Path([second_router, third_router])

    actual = distance_calculator.get_distances()
    assert actual == expected
