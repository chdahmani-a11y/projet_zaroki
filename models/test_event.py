
from models.event import Trip, Meeting, Competition, display_event_details

trip = Trip("Voyage scientifique", "Sortie à Alger", "2025-03-15", "Club Zaroki", "Alger")
meeting = Meeting("Réunion hebdomadaire", "Discussion de projets", "2025-02-20", "Président", "IA et Robotique")
competition = Competition("Hackathon", "Défi de programmation", "2025-04-05", "Département Info", "Certificat + 10000DA")

display_event_details(trip)
display_event_details(meeting)
display_event_details(competition)




#from models.event import Trip, Meeting, Competition

#trip = Trip("Voyage d'étude", "Sortie à Alger", "2025-11-10", "Club Chahira", "Université de Bab Ezzouar")
#meeting = Meeting("Réunion générale", "Planification des activités", "2025-11-05", "Président du club", "Activités du mois")
#competition = Competition("Hackathon IA", "Défi de programmation", "2025-12-01", "Club Chahira", "Certificat + Cadeau")

#for e in [trip, meeting, competition]:
   # print(e.get_summary())


