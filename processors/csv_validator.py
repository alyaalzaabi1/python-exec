from typing import Any, List

class CSVValidator:
    def process(self, data: List[dict]) -> List[dict]:
        return [row for row in data if all(row.values())]  # Keep only rows with no empty fields

