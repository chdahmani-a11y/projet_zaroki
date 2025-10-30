# club.py

from data_loader import load_members_from_file

class ScientificClub:
    def __init__(self, name, data_file):
        self.name = name
        self.data_file = data_file
        self.members = load_members_from_file(data_file)

    def count_paid_members(self):
        """Retourne le nombre de membres ayant payé."""
        return sum(1 for m in self.members if m.is_paid())

    def total_members(self):
        """Retourne le nombre total de membres."""
        return len(self.members)

    def paid_percentage(self):
        """Calcule le pourcentage de membres ayant payé."""
        total = self.total_members()
        return round((self.count_paid_members() / total) * 100, 2) if total > 0 else 0

    def generate_html_report(self, output_file="club_report.html"):
        """Génère une page HTML avec statistiques et liste des membres."""
        html = ["<html><head><meta charset='utf-8'><title>Rapport du Club</title></head><body>"]
        html.append(f"<h2>Club Scientifique : {self.name}</h2>")
        html.append(f"<p>Total des membres : {self.total_members()}</p>")
        html.append(f"<p>Membres ayant payé : {self.count_paid_members()} ({self.paid_percentage()}%)</p>")
        html.append("<table border='1'><tr><th>ID</th><th>Nom</th><th>Prénom</th><th>Email</th><th>Téléphone</th><th>Statut</th></tr>")
        for m in self.members:
            html.append(m.to_html_row())
        html.append("</table></body></html>")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(html))

        print(f"✅ Rapport HTML généré : {output_file}")
