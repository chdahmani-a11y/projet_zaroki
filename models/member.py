# models/member.py
from dataclasses import dataclass

@dataclass
class Member:
    student_id: int
    family_name: str
    first_name: str
    email: str
    phone: str
    address: str
    join_date: str
    subscription_status: str

    def is_paid(self) -> bool:
        return self.subscription_status.strip().lower() == "paid"

    def full_name(self) -> str:
        return f"{self.first_name} {self.family_name}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "family_name": self.family_name,
            "first_name": self.first_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "join_date": self.join_date,
            "subscription_status": self.subscription_status,
        }
