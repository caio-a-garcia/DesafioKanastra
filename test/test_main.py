import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from fastapi import UploadFile
from fastapi.testclient import TestClient
from app.main import app, billing
from app.state import db, reset_db, set_db_with_mock_data

client = TestClient(app)


def test_check_bills():
    response = client.get("/check-bills")
    assert response.status_code == 200


def test_payment_no_debt():
    response = client.post(
        "/payment",
        json={
            "debtId": "8291",
            "paidAt": "2022-06-09 10:00:00",
            "paidAmount": 100000.00,
            "paidBy": "John Doe"
        }
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Debt with given id not found."
    }
    reset_db()


# def test_billing_valid():
#     reset_db()
#     print(db)
#     with open("./src/test-input.csv", "rb") as file:
#         # print("test_input: " + str(test_input))
#         response = client.post(
#             "/billing",
#             files={"file": UploadFile(file)}
#         )
#         assert response.status_code == 202


def test_payment_with_debt():
    set_db_with_mock_data()

    response = client.post(
        "/payment",
        json={
            "debtId": "1001",
            "paidAt": "2022-06-09 10:00:00",
            "paidAmount": 100000.00,
            "paidBy": "John Doe"
        }
    )

    assert response.status_code == 201
    assert response.json() == {
        "debtId": "1001",
        "paidAt": "2022-06-09 10:00:00",
        "paidAmount": 100000,
        "paidBy": "John Doe",
        "processed": True
    }
