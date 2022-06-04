from typing import List

from graph.router_node import RouterNode


def make_adjacent(router: RouterNode, adjacent_set: List[RouterNode]):
    for adjacent in adjacent_set:
        router.add_adjacent(adjacent)
