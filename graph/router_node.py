import heapq
from parser.value_objects.router import Router
from typing import List, Optional


class RouterNode:
    def __init__(self, router: Router, adjacents: Optional[List['RouterNode']] = None) -> None:
        self.router = router
        self.adjacents = adjacents or []
        heapq.heapify(self.adjacents)

    def add_adjacent(self, router_node: 'RouterNode') -> None:
        if router_node not in self.adjacents:
            heapq.heappush(self.adjacents, router_node)

    def __eq__(self, other) -> bool:
        return self._equals(other, [])

    def _equals(self, other, visited) -> bool:
        if self in visited or other in visited:
            return True

        visited.append(self)
        visited.append(other)
        if not isinstance(other, RouterNode):
            return False

        return self.router == other.router and all(
            x._equals(y, visited) for x, y in zip(self.adjacents, other.adjacents)  # pylint: disable=W0212
        )

    def __repr__(self) -> str:
        return f"{type(self).__name__}(router={self.router}, n_adjacents={len(self.adjacents)})"

    def __hash__(self) -> int:
        return 3 * hash(self.router)

    def __lt__(self, other) -> bool:
        if not isinstance(other, RouterNode):
            raise TypeError(f"can't compare between '{type(self).__name__}' and '{type(other).__name__}'")

        return self.router.sys_name.name < other.router.sys_name.name
