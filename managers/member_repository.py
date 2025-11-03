# managers/member_repository.py

class MemberRepository:
    """Gestion des membres (chargement depuis une source de données)"""

    def __init__(self, storage):
        # Injection de dépendance : storage = CSVStorage, JSONStorage, etc.
        self.storage = storage

    def load_members(self):
        """Charge tous les membres depuis la source de données"""
        return self.storage.load_members()
