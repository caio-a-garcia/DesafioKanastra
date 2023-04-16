"""Initialize application state."""
from app.model import DebtItem

db = {"debt_items": [DebtItem(name="John Doe",
                              governmentId=11111111,
                              email="johndoe@kanastra.com.br",
                              debtAmount=50000.00,
                              debtDueDate="2023-04-20",
                              debtId=1001)
                     ],
      "payment_items": []}


def process_payment(item):
    """Deduces payment amount from appropriate debt."""
    for debt in db["debt_items"]:
        if debt.debtId == int(item.debtId):
            debt.amountDue = debt.amountDue - item.paidAmount
            item.processed = True
            if debt.amountDue <= 0.0:
                debt.paid = True
            return True

    return False


def reset_db():
    """Reset db to empty state."""
    db = {"debt_items": [],
          "payment_items": []}

    return db


def set_db_with_mock_data():
    """Add mock data to db for testing."""
    debt_item1 = DebtItem(name="John Doe",
                          governmentId=11111111,
                          email="johndoe@kanastra.com.br",
                          debtAmount=50000.00,
                          debtDueDate="2023-04-20",
                          debtId=1001)

    debt_item2 = DebtItem(name="Jane Doe",
                          governmentId=11111112,
                          email="jannied@kanastra.com.br",
                          debtAmount=10.00,
                          debtDueDate="2023-04-20",
                          debtId=1002)

    db["debt_items"].extend((debt_item1, debt_item2))
