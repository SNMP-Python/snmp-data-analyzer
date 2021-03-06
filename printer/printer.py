from abc import abstractmethod, ABC
from typing import Dict, FrozenSet

from distance.path import Path
from distance.point import Point
from parser.value_objects.router import Router
from searcher.primitives.router_primitives import RouterPrimitives


class Printer(ABC):
    @abstractmethod
    def print_primitives(
        self, router_primitives: FrozenSet[RouterPrimitives]
    ) -> None:
        pass

    @abstractmethod
    def print_routers(self, routers: FrozenSet[Router]) -> None:
        pass

    @abstractmethod
    def print_distances(self, distances: Dict[Point, Path]) -> None:
        pass
