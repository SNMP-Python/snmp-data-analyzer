from test.distance.mothers.graphs_mother import GraphMother

from deepdiff import DeepDiff
from netaddr import IPAddress, IPNetwork

from distance.distance_calculator_imp import DistanceCalculatorImp
from distance.points import Points


def test_bitwise_and():
    network = IPNetwork('12.0.0.2/24')
    expected = IPAddress('12.0.0.0')
    assert network.network & network.netmask == expected


def test_one_router_one_interface_outputs_empty_dict():
    graph = GraphMother.get_one_router_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    assert distance_calculator.get_distances() == {}


def test_one_router_three_interfaces_outputs_expected_dict():
    graph = GraphMother.get_one_router_three_interfaces_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    router = GraphMother._get_one_router_three_interfaces()
    expected = {}
    expected_first_point = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('8.0.0.5'))
    expected[expected_first_point] = router

    expected_second_point = Points(source=IPAddress('8.0.0.5'), destination=IPAddress('10.0.0.6'))
    expected[expected_second_point] = router

    expected_third_point = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('10.0.0.6'))
    expected[expected_third_point] = router

    actual = distance_calculator.get_distances()
    diff = DeepDiff(actual, expected)
    for position in diff.keys():
        assert diff[position] == [None]


def test_two_router_one_interface_each_outputs_expected_dict():
    graph = GraphMother.get_two_routers_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    first_router = GraphMother._get_first_router_second_test()
    second_router = GraphMother._get_second_router_second_test()
    expected = {}
    expected_first_point = Points(source=IPAddress('6.0.0.1'), destination=IPAddress('8.0.0.2'))
    expected[expected_first_point] = [first_router, second_router]

    actual = distance_calculator.get_distances()
    diff = DeepDiff(actual, expected)
    for position in diff.keys():
        assert diff[position] == [None]
