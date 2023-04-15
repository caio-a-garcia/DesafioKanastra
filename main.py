"""Entry point for billing program."""
from fastapi import FastAPI, UploadFile, Response, HTTPException
import pandas
from model import DebtItem


app = FastAPI()

db = {"debt_items": [],
      "payment_items": []}


@app.post("/billing", status_code=202)
def read_csv(item: UploadFile, response: Response):
    """
    Get file as request body.

    Takes a file in the request body and returns its type.
    Expects a CSV, but no checks just yet.
    """
    expected_keys = ('name', 'governmentId', 'email',
                     'debtAmount', 'debtDueDate', 'debtId')

    if item.content_type != "text/csv":
        raise HTTPException(status_code=415,
                            detail="Wrong file type. CSV expected.")

    values = pandas.read_csv(item.file).T.to_dict()

    if not all(key in values[0] for key in expected_keys):
        # print(key for key in expected_keys)
        raise HTTPException(
            status_code=422,
            detail="Request does not have all expected fields.")

    item = DebtItem(name=values[0]['name'],
                    governmentId=values[0]['governmentId'],
                    email=values[0]['email'],
                    debtAmount=values[0]['debtAmount'],
                    debtDueDate=values[0]['debtDueDate'],
                    debtId=values[0]['debtId'])

    # Reject items with repeated ids.
    if item in db["debt_items"]:
        raise HTTPException(
            status_code=409,
            detail="Id already exists in db.")

    db['debt_items'].append(item)

    return item


@app.get("/check-bills")
def check_bills():
    """Return all bills."""
    debt_items = db["debt_items"]

    print(debt_items)

    return debt_items


@app.post("/json")
def read_json(item: DebtItem):
    """
    Test pydantic's BaseModel.

    Expect to use BaseModel to process CSV request body later.
    """
    return item
