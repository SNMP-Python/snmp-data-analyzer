from parser.value_objects.router import Router
from typing import List


class RouterNode:
    def __init__(self, router: Router):
        self.router = router
        self.adjacent_routers: List[RouterNode] = []
