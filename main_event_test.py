# main_event_test.py
from models.event import Trip, Meeting, Competition

def main():
    print("=== Démonstration des événements du club scientifique ===\n")

    trip = Trip(
        name="Voyage d'étude",
        description="Sortie à Alger pour visiter le Centre de recherche",
        event_date="2025-11-10",
        organizer="Club Chahira_Cylia",
        destination="Université de Bab Ezzouar"
    )

    meeting = Meeting(
        name="Réunion générale",
        description="Planification des activités du mois",
        event_date="2025-11-05",
        organizer="Président du club",
        topic="Organisation du hackathon et des ateliers"
    )

    competition = Competition(
        name="Hackathon IA",
        description="Compétition d'intelligence artificielle",
        event_date="2025-12-01",
        organizer="Club Chahira_Cylia",
        reward="Certificat + Cadeau surprise"
    )

    # Test LSP: toutes les sous-classes peuvent être utilisées à la place de Event
    for event in [trip, meeting, competition]:
        print(event.describe())

if __name__ == "__main__":
    main()
