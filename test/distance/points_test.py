from netaddr import IPAddress

from distance.points import Points


def test_points_equals_same_point():
    source = IPAddress('11.0.0.6')
    destination = IPAddress('11.0.0.2')
    first_point = second_point = Points(source, destination)
    assert first_point == second_point


def test_points_equals_inverse_point():
    source = IPAddress('11.0.0.6')
    destination = IPAddress('11.0.0.2')
    first_point = Points(source, destination)
    second_point = Points(destination, source)
    assert first_point == second_point
