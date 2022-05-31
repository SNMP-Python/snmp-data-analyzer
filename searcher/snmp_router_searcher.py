from __future__ import absolute_import

from typing import List

from searcher.primitives.router_primitives import RouterPrimitives
from searcher.router_searcher import RouterSearcher


class SNMPRouterSearcher(RouterSearcher):
    def get_router_primitives(self) -> List[RouterPrimitives]:
        pass
