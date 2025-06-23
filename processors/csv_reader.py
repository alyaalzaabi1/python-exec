import csv
from typing import Any, List

class CSVReader:
    def read(self, filepath: str) -> List[dict]:
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
