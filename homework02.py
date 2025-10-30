# homework02.py

from club import ScientificClub

def main():
    club = ScientificClub("Club Scientifique Zaroki", "association_data.txt")
    club.generate_html_report()

if __name__ == "__main__":
    main()
