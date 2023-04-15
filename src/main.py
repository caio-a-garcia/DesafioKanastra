"""Entry point for billing program."""
from fastapi import FastAPI, UploadFile, HTTPException
import pandas
from model import DebtItem, PaymentItem
from state import db


app = FastAPI()


@app.post("/billing", status_code=202)
def billing(item: UploadFile):
    """Register a new debt."""
    expected_keys = ("name", "governmentId", "email",
                     "debtAmount", "debtDueDate", "debtId")

    if item.content_type != "text/csv":
        raise HTTPException(status_code=415,
                            detail="Wrong file type. CSV expected.")

    values = pandas.read_csv(item.file).T.to_dict()

    if not all(key in values[0] for key in expected_keys):
        raise HTTPException(
            status_code=422,
            detail="Request does not have all expected fields.")

    item = DebtItem(name=values[0]["name"],
                    governmentId=values[0]["governmentId"],
                    email=values[0]["email"],
                    debtAmount=values[0]["debtAmount"],
                    debtDueDate=values[0]["debtDueDate"],
                    debtId=values[0]["debtId"])

    # Reject items with repeated ids.
    if item in db["debt_items"]:
        raise HTTPException(
            status_code=409,
            detail="Id already exists in db.")

    db["debt_items"].append(item)

    return item


@app.get("/check-bills")
def check_bills():
    """Return all bills."""
    debt_items = db["debt_items"]

    return debt_items


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


@app.post("/payment", status_code=201)
def payment(item: PaymentItem):
    """Take a payment and process it against registered debts.

    Processing happen in process_payment.
    """
    expected_keys = ("debtId", "paidAt", "paidAmount", "paidBy")

    if not all(key in item.json() for key in expected_keys):
        raise HTTPException(
            status_code=422,
            detail="Request does not have all expected fields.")

    db["payment_items"].append(item)

    payment_processed = process_payment(item)

    if not payment_processed:
        raise HTTPException(status_code=404,
                            detail="Debt with given id not found.")

    return item
