# interfaces/ui.py
from abc import ABC, abstractmethod
from models.member import Member

class UI(ABC):
    @abstractmethod
    def show_message(self, msg: str):
        pass

    @abstractmethod
    def show_members(self, members: list):
        pass
