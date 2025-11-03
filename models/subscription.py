# models/subscription.py
from datetime import date


class Subscription:
    """Classe de base représentant un abonnement générique."""

    def __init__(self, member_name: str, start_date: str, amount: float):
        self.member_name = member_name
        self.start_date = start_date
        self.amount = amount

    def get_info(self):
        """Renvoie une description générique de l’abonnement."""
        return f"Abonnement de {self.member_name} depuis {self.start_date}, montant : {self.amount} DA"


# ----------------------------------------------------------
# Sous-classes pour différents types d’abonnements
# --------- OCP : extension sans modification ---------------
# ----------------------------------------------------------

class Donation(Subscription):
    """Représente un don unique fait par un membre."""
    def __init__(self, member_name: str, date_donation: str, amount: float, message: str = ""):
        super().__init__(member_name, date_donation, amount)
        self.message = message

    def get_info(self):
        msg = f" ({self.message})" if self.message else ""
        return f" Don de {self.member_name} le {self.start_date} : {self.amount} DA{msg}"


class MonthlySubscription(Subscription):
    """Abonnement mensuel avec paiement récurrent."""
    def __init__(self, member_name: str, start_date: str, amount: float):
        super().__init__(member_name, start_date, amount)

    def get_info(self):
        return f" Abonnement mensuel de {self.member_name} : {self.amount} DA/mois (depuis {self.start_date})"


class AnnualSubscription(Subscription):
    """Abonnement annuel."""
    def __init__(self, member_name: str, start_date: str, amount: float):
        super().__init__(member_name, start_date, amount)

    def get_info(self):
        return f" Abonnement annuel de {self.member_name} : {self.amount} DA/an (depuis {self.start_date})"
