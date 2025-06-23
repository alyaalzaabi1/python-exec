from datastore_interface import DataStore
from typing import Optional, List
import json, os

class FileStore(DataStore):
    def __init__(self, filename="filestore.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def _read_file(self) -> dict:
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def _write_file(self, data: dict):
        with open(self.filename, "w") as f:
            json.dump(data, f)

    def store(self, key: str, value: str) -> bool:
        data = self._read_file()
        data[key] = value
        self._write_file(data)
        return True

    def retrieve(self, key: str) -> Optional[str]:
        data = self._read_file()
        return data.get(key)

    def delete(self, key: str) -> bool:
        data = self._read_file()
        if key in data:
            del data[key]
            self._write_file(data)
            return True
        return False

    def list_keys(self) -> List[str]:
        data = self._read_file()
        return list(data.keys())

    def is_healthy(self) -> bool:
        try:
            open(self.filename, "r").close()
            return True
        except Exception:
            return False
