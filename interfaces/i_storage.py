# interfaces/i_storage.py
from abc import ABC, abstractmethod

class IStorage(ABC):
    """Interface pour toutes les classes de stockage (CSV, JSON, DB, etc.)"""

    @abstractmethod
    def load_data(self):
        """Charge les données depuis une source (fichier, base, etc.)"""
        pass

    @abstractmethod
    def save_data(self, data):
        """Enregistre les données dans la source"""
        pass
