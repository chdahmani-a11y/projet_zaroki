# club.py
from data_loader import load_members_from_file
import html
import os

class ScientificClub:
    def __init__(self, name: str, data_file: str):
        self.name = name
        self.data_file = data_file
        self.members = []  
             
  
    def load_data(self):
        """
        يقرأ الملف association_data.txt ويحوّل كل سطر إلى كائن Member 
        باستخدام الدالة load_members_from_file الموجودة في data_loader.py
        """
        self.members = load_members_from_file(self.data_file)
        return self.members

    def display_members(self, limit=20):
        
        if not self.members:
            print("Aucun membre chargé.")
            return
        print(f"\n=== Liste des membres du club '{self.name}' ===")
        for m in self.members[:limit]:
            
            print(f"- {m}")
        print(f"... ({len(self.members)} membres au total)")

    def generate_html_report(self, output_file="association_data.html"):
        
        if not self.members:
            print("Aucun membre à exporter en HTML.")
            return

        
        headers = ["student_id", "family_name", "first_name", "email", "phone", "address", "join_date", "subscription_status"]

        html_parts = []
        html_parts.append("<!doctype html>")
        html_parts.append("<html lang='fr'>")
        html_parts.append("<head><meta charset='utf-8' /><title>Rapport des membres</title></head>")
        html_parts.append("<body>")
        html_parts.append(f"<h2>Liste des membres — {html.escape(self.name)}</h2>")
        html_parts.append("<table border='1' cellpadding='5' cellspacing='0'>")
        # header
        html_parts.append("<thead><tr>")
        for h in headers:
            html_parts.append(f"<th>{html.escape(h)}</th>")
        html_parts.append("</tr></thead>")
        # body
        html_parts.append("<tbody>")
        for m in self.members:
            
            try:
                rowd = m.to_dict()
            except Exception:
                
                rowd = {
                    "student_id": getattr(m, "student_id", ""),
                    "family_name": getattr(m, "family_name", ""),
                    "first_name": getattr(m, "first_name", ""),
                    "email": getattr(m, "email", ""),
                    "phone": getattr(m, "phone", ""),
                    "address": getattr(m, "address", ""),
                    "join_date": getattr(m, "join_date", ""),
                    "subscription_status": getattr(m, "subscription_status", "")
                }
            html_parts.append("<tr>")
            for h in headers:
                val = str(rowd.get(h, ""))
                html_parts.append(f"<td>{html.escape(val)}</td>")
            html_parts.append("</tr>")
        html_parts.append("</tbody></table>")
        html_parts.append("</body></html>")

        content = "\n".join(html_parts)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Rapport HTML généré : {os.path.abspath(output_file)}")
