from abc import ABC, abstractmethod
from typing import Any


class MemoryStorage(ABC):
    @abstractmethod
    def save(self, memory: Any) -> None:
        pass

    @abstractmethod
    def load_all(self) -> list[Any]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
