from netaddr import IPAddress

from distance.points import Points


class GraphPointMother:
    @staticmethod
    def get_point_for_graph(
            source_str: str,
            destination_str, ) -> Points:
        return Points(
            source=IPAddress(source_str),
            destination=IPAddress(destination_str),
        )
