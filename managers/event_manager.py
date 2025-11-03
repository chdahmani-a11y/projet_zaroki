# managers/event_manager.py
from models.event import Event

def display_event_details(event: Event):

    print(event.describe())
