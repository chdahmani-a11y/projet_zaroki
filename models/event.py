# models/event.py
from abc import ABC, abstractmethod
from typing import List

class Event(ABC):
    def __init__(self, event_name: str, description: str, event_date: str, organizer: str, participants: List[str]=None):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.organizer = organizer
        self.participants = participants or []

    @abstractmethod
    def describe(self) -> str:
        pass

class Trip(Event):
    def describe(self) -> str:
        return f"Trip: {self.event_name} on {self.event_date} organized by {self.organizer}"

class Meeting(Event):
    def describe(self) -> str:
        return f"Meeting: {self.event_name} on {self.event_date} organized by {self.organizer}"

class Competition(Event):
    def describe(self) -> str:
        return f"Competition: {self.event_name} on {self.event_date} organized by {self.organizer}"
