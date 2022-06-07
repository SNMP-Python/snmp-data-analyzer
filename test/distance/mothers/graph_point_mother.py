from netaddr import IPAddress

from distance.point import Point


class GraphPointMother:
    @staticmethod
    def get_point_for_graph(
        source_str: str,
        destination_str,
    ) -> Point:
        return Point(
            source=IPAddress(source_str),
            destination=IPAddress(destination_str),
        )
