from abc import ABC, abstractmethod
from typing import Dict

from distance.path import Path
from distance.points import Points


class DistanceCalculator(ABC):
    @abstractmethod
    def get_distances(self) -> Dict[Points, Path]:
        pass
