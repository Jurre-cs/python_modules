from abc import ABC, abstractmethod
from typing import Any


class HealCapability(ABC):

    @abstractmethod
    def heal(self, target: Any = None) -> str:
        pass


class TransformCapability(ABC):

    transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
