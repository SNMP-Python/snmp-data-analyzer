from typing import Dict, List

from deepdiff import DeepDiff
from netaddr import IPAddress, IPNetwork

from distance.distance_calculator_imp import DistanceCalculatorImp
from distance.path import Path
from distance.points import Points
from parser.value_objects.router import Router
from test.distance.mothers.one_router_graph_mother import OneRouterGraphMother
from test.distance.mothers.three_routers_graph_mother import ThreeRoutersGraphMother
from test.distance.mothers.two_routers_graph_mother import \
    TwoRoutersGraphMother


def test_bitwise_and():
    network = IPNetwork('12.0.0.2/24')
    expected = IPAddress('12.0.0.0')
    assert network.network & network.netmask == expected


def test_one_router_one_interface_outputs_empty_dict():
    graph = OneRouterGraphMother.get_one_router_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    assert distance_calculator.get_distances() == {}


def test_one_router_three_interfaces_outputs_expected_dict():
    graph = OneRouterGraphMother.get_one_router_three_interfaces_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    router = OneRouterGraphMother._get_one_router_three_interfaces()
    expected = {}
    expected_first_point = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('8.0.0.5'))
    expected[expected_first_point] = Path([router])

    expected_second_point = Points(source=IPAddress('8.0.0.5'), destination=IPAddress('10.0.0.6'))
    expected[expected_second_point] = Path([router])

    expected_third_point = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('10.0.0.6'))
    expected[expected_third_point] = Path([router])

    actual = distance_calculator.get_distances()
    assert actual == expected


def test_two_router_one_interface_each_outputs_expected_dict():
    graph = TwoRoutersGraphMother.get_two_routers_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    first_router = TwoRoutersGraphMother._get_first_router_second_test()
    second_router = TwoRoutersGraphMother._get_second_router_second_test()

    expected = {}
    expected_first_point = Points(source=IPAddress('6.0.0.1'), destination=IPAddress('6.0.0.2'))
    expected[expected_first_point] = Path([first_router, second_router])

    actual = distance_calculator.get_distances()
    assert actual == expected


def test_three_routers_one_interface_each_outputs_expected_dict():
    graph = ThreeRoutersGraphMother.get_three_routers_one_interface_graph()
    distance_calculator = DistanceCalculatorImp(graph)
    first_router = ThreeRoutersGraphMother._get_first_router_third_test()
    second_router = ThreeRoutersGraphMother._get_second_router_third_test()
    third_router = ThreeRoutersGraphMother._get_third_router_third_test()
    expected = {}

    point_62_64 = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('6.0.0.4'))
    point_62_84 = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('8.0.0.4'))
    point_62_86 = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('8.0.0.6'))
    point_62_108 = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('10.0.0.8'))
    point_62_1010 = Points(source=IPAddress('6.0.0.2'), destination=IPAddress('10.0.0.10'))

    point_64_84 = Points(source=IPAddress('6.0.0.4'), destination=IPAddress('8.0.0.4'))
    point_64_86 = Points(source=IPAddress('6.0.0.4'), destination=IPAddress('8.0.0.6'))
    point_64_108 = Points(source=IPAddress('6.0.0.4'), destination=IPAddress('10.0.0.8'))
    point_64_1010 = Points(source=IPAddress('6.0.0.4'), destination=IPAddress('10.0.0.10'))

    point_84_86 = Points(source=IPAddress('8.0.0.4'), destination=IPAddress('8.0.0.6'))
    point_84_108 = Points(source=IPAddress('8.0.0.4'), destination=IPAddress('10.0.0.8'))
    point_84_1010 = Points(source=IPAddress('8.0.0.4'), destination=IPAddress('10.0.0.10'))

    point_86_108 = Points(source=IPAddress('8.0.0.6'), destination=IPAddress('10.0.0.8'))
    point_86_1010 = Points(source=IPAddress('8.0.0.6'), destination=IPAddress('10.0.0.10'))

    point_108_1010 = Points(source=IPAddress('10.0.0.8'), destination=IPAddress('10.0.0.10'))

    expected[point_62_64] = Path([first_router, second_router])
    expected[point_62_84] = Path([first_router])
    expected[point_62_86] = Path([first_router, third_router])
    expected[point_62_108] = Path([first_router, second_router])
    # expected[point_62_1010] = [first_router, third_router]
    expected[point_62_1010] = Path([first_router, second_router, third_router])

    # expected[point_64_84] = [second_router, first_router]
    expected[point_64_84] = Path([second_router, third_router, first_router])
    # expected[point_64_86] = [second_router, third_router]
    expected[point_64_86] = Path([second_router, first_router, third_router])
    expected[point_64_108] = Path([second_router])
    expected[point_64_1010] = Path([second_router, third_router])

    expected[point_84_86] = Path([first_router, third_router])
    expected[point_84_108] = Path([first_router, second_router])
    expected[point_84_1010] = Path([first_router, third_router])

    expected[point_86_108] = Path([third_router, second_router])
    expected[point_86_1010] = Path([third_router])

    expected[point_108_1010] = Path([second_router, third_router])

    actual = distance_calculator.get_distances()
    assert actual == expected
