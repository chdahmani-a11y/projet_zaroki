import csv
from models.member import Member

def load_members_from_file(filename, encoding='utf-8'):
    """
    Lit un fichier CSV ou TSV et retourne une liste d'objets Member.
    """
    try:
        with open(filename, 'r', encoding=encoding, newline='') as f:
            reader = csv.DictReader(f, delimiter='\t')
            members = []
            for row in reader:
                m = Member(
                    student_id=row.get("student_id", ""),
                    family_name=row.get("family_name", ""),
                    first_name=row.get("first_name", ""),
                    email=row.get("email", ""),
                    phone=row.get("phone", ""),
                    address=row.get("address", ""),
                    join_date=row.get("join_date", ""),
                    subscription_status=row.get("subscription_status", "")
                )
                members.append(m)
            return members

    except UnicodeDecodeError:
        print("  Erreur d'encodage avec utf-8, nouvel essai...")
        return load_members_from_file(filename, encoding='utf-16')

    except FileNotFoundError:
        print("  Fichier introuvable !")
        return []
    except Exception as e:
        print(f" Erreur inattendue : {e}")
        return []
