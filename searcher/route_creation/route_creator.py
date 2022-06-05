from __future__ import absolute_import

from abc import ABC, abstractmethod


class RouteCreator(ABC):
    @abstractmethod
    def create_route_to(self, network: str, mask: str) -> None:
        pass
