import csv
from typing import Any

class CSVWriter:
    def write(self, data: Any, filepath: str) -> None:
        if not data:
            return

        with open(filepath, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
