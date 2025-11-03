# models/event.py
from datetime import date

class Event:
    """Classe de base représentant un événement général dans le club."""

    def __init__(self, name: str, description: str, event_date: str, organizer: str):
        self.name = name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer

    def get_summary(self):
        """Retourne un résumé générique de l'événement"""
        return f"{self.name} organisé par {self.organizer} le {self.event_date}"

    def describe(self):
        """Méthode générique — à redéfinir par les sous-classes"""
        return f"[Événement] {self.name}: {self.description}"

    def __str__(self):
        return f"[Événement] {self.name} ({self.event_date})"


# ------------------------------------------------------
# Classes dérivées : OCP + LSP
# ------------------------------------------------------

class Trip(Event):
    """Événement de type voyage scientifique ou culturel"""
    def __init__(self, name, description, event_date, organizer, destination):
        super().__init__(name, description, event_date, organizer)
        self.destination = destination

    def get_summary(self):
        return f"Voyage à {self.destination} organisé par {self.organizer} le {self.event_date}"

    def describe(self):
        return f"Voyage scientifique '{self.name}' vers {self.destination} — Description: {self.description}"


class Meeting(Event):
    """Événement de type réunion"""
    def __init__(self, name, description, event_date, organizer, topic):
        super().__init__(name, description, event_date, organizer)
        self.topic = topic

    def get_summary(self):
        return f"Réunion sur '{self.topic}' animée par {self.organizer} le {self.event_date}"

    def describe(self):
        return f"Réunion '{self.name}' — Sujet: {self.topic}, Détails: {self.description}"


class Competition(Event):
    """Événement de type compétition"""
    def __init__(self, name, description, event_date, organizer, reward):
        super().__init__(name, description, event_date, organizer)
        self.reward = reward

    def get_summary(self):
        return f"Compétition '{self.name}' organisée par {self.organizer} le {self.event_date} (Prix: {self.reward})"

    def describe(self):
        return f"Compétition '{self.name}' — Prix: {self.reward}, Détails: {self.description}"
