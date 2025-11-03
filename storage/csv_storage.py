# storage/csv_storage.py
import csv
from models.member import Member

class CSVStorage:
    """Classe responsable du chargement des membres depuis un fichier CSV/TSV"""

    def __init__(self, file_path, encoding='utf-8'):
        self.file_path = file_path
        self.encoding = encoding

    def load_members(self):
        """Charge les membres depuis un fichier TSV (tab-separated values)."""
        members = []
        try:
            with open(self.file_path, 'r', encoding=self.encoding, newline='') as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    member = Member(
                        student_id=row.get("student_id", ""),
                        family_name=row.get("family_name", ""),
                        first_name=row.get("first_name", ""),
                        email=row.get("email", ""),
                        phone=row.get("phone", ""),
                        address=row.get("address", ""),
                        join_date=row.get("join_date", ""),
                        subscription_status=row.get("subscription_status", "")
                    )
                    members.append(member)
            print(f" Fichier chargé avec succès en {self.encoding}")
        except UnicodeDecodeError:
            if self.encoding == 'utf-8':
                print(" Erreur d'encodage avec utf-8, nouvel essai...")
                self.encoding = 'utf-16'
                return self.load_members()
            else:
                print(" Erreur d'encodage fatale.")
        return members
