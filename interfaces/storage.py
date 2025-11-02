# interfaces/storage.py
from abc import ABC, abstractmethod
from typing import List, Dict

class Storage(ABC):
    @abstractmethod
    def load(self) -> List[Dict]:
        """Return list of dict rows"""
        pass

    @abstractmethod
    def save(self, rows: List[Dict]):
        pass
