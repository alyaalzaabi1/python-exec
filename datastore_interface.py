from abc import ABC, abstractmethod
from typing import Optional, List

class DataStore(ABC):
    @abstractmethod
    def store(self, key: str, value: str) -> bool:
        pass

    @abstractmethod
    def retrieve(self, key: str) -> Optional[str]:
        pass

    @abstractmethod
    def delete(self, key: str) -> bool:
        pass

    @abstractmethod
    def list_keys(self) -> List[str]:
        pass

    @abstractmethod
    def is_healthy(self) -> bool:
        pass
