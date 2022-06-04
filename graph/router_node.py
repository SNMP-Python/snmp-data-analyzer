from typing import Optional, Set

from parser.value_objects.router import Router


class RouterNode:
    def __init__(self, router: Router, adjacents: Optional[Set['RouterNode']] = None) -> None:
        self.router = router
        self.adjacents = adjacents or set()

    def add_adjacent(self, router_node: 'RouterNode') -> None:
        self.adjacents.add(router_node)

    def __eq__(self, other) -> bool:
        if not isinstance(other, RouterNode):
            return False

        return self.router == other.router and set(id(x.router) for x in self.adjacents) == set(
            id(x.router) for x in other.adjacents
        )

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}(router={self.router.sys_name}, "
            f"adjacents={[r.router.sys_name.name for r in self.adjacents]})"
        )

    def __hash__(self) -> int:
        return 3 * hash(self.router)
