from typing import Protocol, Any


class FileReader(Protocol):
    def read(self, filepath: str) -> Any:
        ...


class FileProcessor(Protocol):
    def process(self, data: Any) -> Any:
        ...


class FileWriter(Protocol):
    def write(self, data: Any, filepath: str) -> None:
        ...
