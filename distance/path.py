from parser.value_objects.router import Router
from typing import List, Optional


class Path:
    def __init__(self, path: Optional[List[Router]] = None):
        if path is None:
            path = []
        self.route = path

    def add_router(self, router: Optional[Router]) -> None:
        if router is not None:
            self.route.append(router)

    def get_path(self) -> List[Router]:
        return self.route

    def __eq__(self, other) -> bool:
        if not isinstance(other, Path):
            return NotImplemented
        other_reverse = list(reversed(other.route.copy()))
        return self.route == other.route or self.route == other_reverse

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str([router.sys_name.name for router in self.route])

    def __lt__(self, other):
        if not isinstance(other, Path):
            return NotImplemented
        return len(self.route) < len(other.route)
