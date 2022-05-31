from __future__ import absolute_import

from abc import ABC, abstractmethod

from searcher.primitives.router_primitives import RouterPrimitives


class Client(ABC):
    @abstractmethod
    def get_router_primitives(self, ip_addr: str) -> RouterPrimitives:
        pass
