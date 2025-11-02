# homework03_main.py
from storage.csv_storage import CSVStorage
from managers.member_repository import MemberRepository
from ui.cli_ui import CLIUI

def main():
    #(Dependency Inversion Principle - DIP)
    storage = CSVStorage("association_data.txt", encoding='utf-8')
    repo = MemberRepository(storage)
    ui = CLIUI()

    ui.show_message("Loading members...")
    members = repo.load_members()

    ui.show_members(members)

    total = len(members)
    paid = sum(1 for m in members if m.is_paid())
    ui.show_message(f"Total members: {total}, Paid: {paid}")

if __name__ == "__main__":
    main()
