# homework02.py
from club import ScientificClub

def main():
    
    club = ScientificClub("Club Scientifique chahira_cylia", "association_data.txt")

    
    club.load_data()


    club.display_members()

    
    club.generate_html_report()

if __name__ == "__main__":
    main()
