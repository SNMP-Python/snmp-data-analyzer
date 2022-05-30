from __future__ import absolute_import

from typing import List

from searcher.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher


class OSPFRouterSearcher(RouterSearcher):
    def get_router_primitives(self) -> List[RouterPrimitives]:
        pass
