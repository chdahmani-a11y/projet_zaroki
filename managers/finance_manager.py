# managers/finance_manager.py

class FinanceManager:
    """Classe responsable du suivi des paiements et abonnements"""

    def __init__(self, members):
        self.members = members

    def count_paid(self):
        """Compte le nombre de membres ayant payé"""
        return sum(1 for m in self.members if m.is_paid())

    def count_pending(self):
        """Compte le nombre de membres en attente de paiement"""
        return sum(1 for m in self.members if not m.is_paid())

    def summary(self):
        """Retourne un résumé financier"""
        total = len(self.members)
        paid = self.count_paid()
        pending = self.count_pending()
        ratio = (paid / total * 100) if total else 0
        return {
            "total_members": total,
            "paid": paid,
            "pending": pending,
            "ratio_paid": round(ratio, 2)
        }
