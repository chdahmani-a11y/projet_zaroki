# models/member.py

from interfaces.payable import Payable

class Member(Payable):
    """Représente un membre de l'association scientifique"""

    def __init__(self, student_id, family_name, first_name, email, phone, address, join_date, subscription_status):
        self.student_id = student_id
        self.family_name = family_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.subscription_status = subscription_status

    def is_paid(self):
        return self.subscription_status.strip().lower() == "paid"

    def __str__(self):
        return f"{self.family_name} {self.first_name} ({self.subscription_status})"
