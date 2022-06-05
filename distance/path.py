from typing import List, Optional

from parser.value_objects.router import Router


class Path:
    def __init__(self, path: Optional[List[Router]] = None):
        if path is None:
            path = []
        self.path = path

    def add_router(self, router: Router) -> None:
        self.path.append(router)

    def get_path(self) -> List[Router]:
        return self.path

    def __eq__(self, other) -> bool:
        if not isinstance(other, Path):
            return NotImplemented
        other_reverse = list(reversed(other.path.copy()))
        return self.path == other.path or self.path == other_reverse

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str([router.sys_name.name for router in self.path])

    def __lt__(self, other):
        if not isinstance(other, Path):
            return NotImplemented
        return len(self.path) < len(other.path)
