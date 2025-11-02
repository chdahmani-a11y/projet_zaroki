# storage/csv_storage.py
import csv
from typing import List, Dict
from interfaces.storage import Storage

class CSVStorage(Storage):
    def __init__(self, filename: str, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding

    def load(self) -> List[Dict]:
        rows = []
        try:
            with open(self.filename, newline='', encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter='\t')
                for r in reader:
                    rows.append(r)
        except UnicodeDecodeError:
            # fallback
            with open(self.filename, newline='', encoding='utf-16') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for r in reader:
                    rows.append(r)
        return rows

    def save(self, rows: List[Dict]):
        if not rows:
            return
        fieldnames = list(rows[0].keys())
        with open(self.filename, 'w', newline='', encoding=self.encoding) as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
