from typing import Protocol, Dict, Any
import asyncio

class TextAnalyzer(Protocol):
    name: str
    version: str
    description: str
    is_async: bool

    def analyze(self, text: str) -> Dict[str, Any]:
        ...

    async def analyze_async(self, text: str) -> Dict[str, Any]:
        ...
