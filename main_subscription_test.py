# main_subscription_test.py
from models.subscription import Donation, MonthlySubscription, AnnualSubscription

def main():
    print("=== Test des abonnements ===")

    d = Donation("KARIM SID AHMED", "2025-11-01", 5000, "Soutien au club")
    m = MonthlySubscription("LATRECHE ILHEM", "2025-01-10", 1200)
    a = AnnualSubscription("DJEDDA YOUSSRA", "2024-10-15", 8000)

    for sub in [d, m, a]:
        print(sub.get_info())

if __name__ == "__main__":
    main()
