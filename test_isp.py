from interfaces.payable import Payable
from interfaces.registrable import Registrable
from interfaces.organizable import Organizable

# تطبيق بسيط لهذه الواجهات
class Member(Payable):
    def __init__(self, name):
        self.name = name
        self.paid = False

    def process_payment(self):
        self.paid = True
        print(f" Paiement traité pour {self.name}")

class Club(Registrable, Organizable):
    def __init__(self, name):
        self.name = name
        self.members = []
        self.events = []

    def register_member(self, member_name):
        self.members.append(member_name)
        print(f" Membre '{member_name}' ajouté au club {self.name}")

    def schedule(self, event_name, date):
        self.events.append((event_name, date))
        print(f" Événement '{event_name}' prévu le {date} dans {self.name}")

# -------- TEST ----------
if __name__ == "__main__":
    print("=== Test du principe ISP ===\n")

    # Créer un membre et tester le paiement
    m = Member("Karim Sid Ahmed")
    m.process_payment()

    # Créer un club et tester les méthodes
    c = Club("Club Scientifique Chahira_Cylia")
    c.register_member("Karim Sid Ahmed")
    c.schedule("Réunion du mois", "2025-11-10")

    print("\n--- Résumé ---")
    print(f"Membres inscrits : {c.members}")
    print(f"Événements planifiés : {c.events}")
