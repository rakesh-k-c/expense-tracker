
from datetime import datetime
from dataclasses import asdict
from expense_tracker.models.transaction import Transaction

def main():
    print("Expense Tracker")

    transaction = Transaction(
        id=1,
        type="expense",
        amount=4440.0,
        category="foot",
        description="lunch",
        created_at=datetime.now(),
    )

    





if __name__ == "__main__":
    main()








































































