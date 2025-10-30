# models.py

class Member:
    """
    Représente un membre du club scientifique.
    """
    def __init__(self, student_id, family_name, first_name, email, phone, address, join_date, subscription_status, skills="", interests=""):
        self.student_id = student_id
        self.family_name = family_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
        self.address = address
        self.join_date = join_date
        self.subscription_status = subscription_status
        self.skills = skills
        self.interests = interests

    def is_paid(self):
        """Retourne True si le membre a payé son abonnement."""
        return self.subscription_status.strip().lower() == "paid"

    def to_html_row(self):
        """Retourne une ligne HTML pour ce membre."""
        return f"<tr><td>{self.student_id}</td><td>{self.family_name}</td><td>{self.first_name}</td><td>{self.email}</td><td>{self.phone}</td><td>{self.subscription_status}</td></tr>"


