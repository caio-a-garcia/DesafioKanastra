"""Entry point for billing program."""
from fastapi import FastAPI, UploadFile, Response, HTTPException
import pandas
from model import DebtItem


app = FastAPI()

db = {"debt_items": [],
      "payment_items": []}

@app.post("/csv")
def read_csv(item: UploadFile):
    """
    Get file as request body.

    Takes a file in the request body and returns its type.
    Expects a CSV, but no checks just yet.
    """
    if item.content_type == "text/csv":
        return pandas.read_csv("test-input.csv").T.to_dict()


@app.post("/json")
def read_json(item: DebtItem):
    """
    Test pydantic's BaseModel.

    Expect to use BaseModel to process CSV request body later.
    """
    return item
