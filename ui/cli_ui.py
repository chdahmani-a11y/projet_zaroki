# ui/cli_ui.py
from interfaces.ui import UI
from models.member import Member

class CLIUI(UI):
    def show_message(self, msg: str):
        print(msg)

    def show_members(self, members: list):
        print("Members:")
        for m in members:
            paid = "PAID" if m.is_paid() else "PENDING"
            print(f"{m.student_id} - {m.full_name()} - {m.email} - {paid}")
