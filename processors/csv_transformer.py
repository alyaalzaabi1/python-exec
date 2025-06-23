from typing import Any, List

class CSVTransformer:
    def process(self, data: List[dict]) -> List[dict]:
        for row in data:
            row["processed"] = "yes"
        return data
