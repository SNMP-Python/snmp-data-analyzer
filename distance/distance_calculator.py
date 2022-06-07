from abc import ABC, abstractmethod
from typing import Dict

from distance.path import Path
from distance.point import Point


class DistanceCalculator(ABC):
    @abstractmethod
    def get_distances(self) -> Dict[Point, Path]:
        pass
