from abc import ABC, abstractmethod

class Registrable(ABC):
    @abstractmethod
    def register_member(self, member_name):
        """Ajoute un membre à une liste ou base de données"""
        pass
