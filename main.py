"""Entry point for billing program."""
from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import pandas


class DebtItem(BaseModel):
    """Model for API request body."""

    name: str
    governmentId: int
    email: str
    debtAmount: float
    debtDueDate: str
    debtId: int


app = FastAPI()


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
