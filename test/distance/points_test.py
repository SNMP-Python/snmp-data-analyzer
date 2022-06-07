from netaddr import IPAddress

from distance.point import Point


def test_points_equals_same_point():
    source = IPAddress('11.0.0.6')
    destination = IPAddress('11.0.0.2')
    first_point = second_point = Point(source, destination)
    assert first_point == second_point


def test_points_equals_inverse_point():
    source = IPAddress('11.0.0.6')
    destination = IPAddress('11.0.0.2')
    first_point = Point(source, destination)
    second_point = Point(destination, source)
    assert first_point == second_point
