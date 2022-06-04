from __future__ import absolute_import

from abc import ABC, abstractmethod
from easysnmp import Session


class Poll(ABC):
    def __init__(self, session: Session):
        self.session = session

    @abstractmethod
    def poll(self):
        pass
