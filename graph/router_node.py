import bisect
from parser.value_objects.router import Router
from typing import Any, List, Optional


class RouterNode:
    def __init__(self, router: Router, adjacents: Optional[List['RouterNode']] = None) -> None:
        self.router = router
        self.adjacents = adjacents or []
        self.adjacents.sort()

    def add_adjacent(self, router_node: 'RouterNode') -> None:
        if not router_node._is_contained(self.adjacents):  # pylint: disable=W0212
            bisect.insort(self.adjacents, router_node)

    def __eq__(self, other) -> bool:
        return self._equals(other, [])

    def _equals(self, other: Any, visited: List['RouterNode']) -> bool:
        if not isinstance(other, RouterNode):
            return False

        if self._is_contained(visited) or other._is_contained(visited):  # pylint: disable=W0212
            return True

        visited.append(self)
        visited.append(other)

        return self.router == other.router and all(
            x._equals(y, visited) for x, y in zip(self.adjacents, other.adjacents)  # pylint: disable=W0212
        )

    def _is_contained(self, visited: List['RouterNode']) -> bool:
        for other in visited:
            if self.router == other.router:
                return True
        return False

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(router={self.router.sys_name}, "
            f"adjacents={[r.router.sys_name.name for r in self.adjacents]})"
        )

    def __hash__(self) -> int:
        return 3 * hash(self.router)

    def __lt__(self, other) -> bool:
        if not isinstance(other, RouterNode):
            raise TypeError(f"can't compare between '{type(self).__name__}' and '{type(other).__name__}'")

        return self.router.sys_name.name < other.router.sys_name.name
