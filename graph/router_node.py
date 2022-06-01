from parser.value_objects.router import Router
from typing import Optional, Set


class RouterNode:
    def __init__(self, router: Router, adjacents: Optional[Set['RouterNode']] = None) -> None:
        self.router = router
        self.adjacents = adjacents or set()

    def add_adjacent(self, router_node: 'RouterNode') -> None:
        self.adjacents.add(router_node)

    def __eq__(self, other) -> bool:
        if not isinstance(other, RouterNode):
            return False
        return (
            self.router == other.router
            and len(self.adjacents) == len(other.adjacents)
            and self.adjacents == other.adjacents
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(router={self.router})"

    def __hash__(self) -> int:
        return hash(self.router) + sum(hash(adj.router) for adj in self.adjacents)
