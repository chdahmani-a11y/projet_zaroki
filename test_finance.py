# test_finance.py
from managers.finance_manager import FinanceManager
from models.member import Member

def main():
    members = [
        Member("1", "Karim", "Ali", "a@mail.com", "123", "Alger", "2025-01-01", "paid"),
        Member("2", "Sara", "Ben", "b@mail.com", "456", "Oran", "2025-01-01", "pending")
    ]

    fm = FinanceManager(members)
    print(fm.summary())

if __name__ == "__main__":
    main()
