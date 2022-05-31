from abc import ABC, abstractmethod
from parser.value_objects.router import Router
from typing import Dict, List

from distance.points import Points


class DistanceCalculator(ABC):
    @abstractmethod
    def get_distances(self) -> Dict[Points, List[Router]]:
        pass
