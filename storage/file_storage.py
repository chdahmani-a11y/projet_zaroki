# storage/file_storage.py

import csv

class FileStorage:
    """Responsable de la lecture et de l'écriture des fichiers (principe SRP)."""

    def __init__(self, filename, encoding="utf-8"):
        self.filename = filename
        self.encoding = encoding

    def read_tab_file(self):
        """Lit un fichier TSV (tab-separated values)"""
        try:
            with open(self.filename, "r", encoding=self.encoding) as f:
                reader = csv.DictReader(f, delimiter="\t")
                return list(reader)
        except UnicodeDecodeError:
            print(" Erreur d'encodage avec utf-8, nouvel essai avec utf-16...")
            with open(self.filename, "r", encoding="utf-16") as f:
                reader = csv.DictReader(f, delimiter="\t")
                return list(reader)
        except FileNotFoundError:
            print(" Erreur : fichier introuvable.")
            return []

    def write_to_file(self, content, mode="w"):
        """Écrit du texte dans un fichier"""
        with open(self.filename, mode, encoding=self.encoding) as f:
            f.write(content)
        print(f" Données enregistrées dans {self.filename}")
