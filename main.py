"""Entry point for billing program."""
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Root of API. Used for testing purposes."""
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    """
    Test endpoint with argument.

    Return simple response, taking argument into account.
    Used for testing purposes.
    """
    return {"item_id": item_id, "q": q}
