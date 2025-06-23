from datastore_interface import DataStore
from typing import Optional, List

class MemoryStore(DataStore):
    def __init__(self):
        self.storage = {}

    def store(self, key: str, value: str) -> bool:
        self.storage[key] = value
        return True

    def retrieve(self, key: str) -> Optional[str]:
        return self.storage.get(key)

    def delete(self, key: str) -> bool:
        return self.storage.pop(key, None) is not None

    def list_keys(self) -> List[str]:
        return list(self.storage.keys())

    def is_healthy(self) -> bool:
        return True
