"""Entry point for billing program."""
from typing import Union

from fastapi import FastAPI

import pandas

app = FastAPI()


@app.get("/")
def read_root():
    """Root of API. Used for testing purposes."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    """
    Test endpoint with argument.

    Return simple response, taking argument into account.
    Used for testing purposes.
    """
    return {"item_id": item_id, "q": q}


@app.get("/csv")
def read_csv():
    """
    Get csv from directory.

    First implementation of consuming a CSV file.
    This will read a specific CSV file from the project directory,
    which is in the expected format to be received by the API.
    """
    df = pandas.read_csv("test-input.csv").T.to_dict()
    return df
