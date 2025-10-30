def load_members_from_file(filename):
    """Lit le fichier TSV et retourne une liste d'objets Member."""
    import csv
    from models import Member

    encodings = ["utf-8", "utf-16", "latin1"]
    for enc in encodings:
        try:
            with open(filename, "r", encoding=enc) as f:
                reader = csv.DictReader(f, delimiter="\t")
                members = []
                for row in reader:
                    m = Member(
                        row["student_id"],
                        row["family_name"],
                        row["first_name"],
                        row["email"],
                        row["phone"],
                        row["address"],
                        row["join_date"],
                        row["subscription_status"],
                        row.get("skills", ""),
                        row.get("interests", "")
                    )
                    members.append(m)
            print(f"✅ Fichier chargé avec succès en {enc}")
            return members
        except UnicodeDecodeError:
            print(f"⚠️ Erreur d'encodage avec {enc}, nouvel essai...")
            continue

    raise UnicodeDecodeError("Aucun encodage valide trouvé pour le fichier.")
