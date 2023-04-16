# Desafio Kanastra
## Billing System

This project implements a simple billing API. Commands are expected to be run from project root directory.

### Setup
Create virtual environment:
`python -m venv .env`

Activate environment (Windows):
`.env\Scripts\activate`

Install dependencies:
`pip install -r requirements.txt`

### Running Project
Commands in this section should be run with environment activated.

The server exposes endpoints for billing and payment.
To start the server run (Windows):
`start-server`

The scheduler checks for standing debts, and simulates the generation of invoices and sending of email. It is configured to run this task every 6 hours.
To start the scheduler run (Windows):
`scheduler`

For running tests:
`pytest`

### API
For SwaggerUI documentation of the API, start the server and point your browser to the "/docs" endpoint. When running on the default port, go to the url:
`http://localhost:8000/docs`

The "/billing" endpoint expects to receive a CSV file from the user with the fields:
  - name: string
  - governmentId: int
  - email: string
  - debtAmount: int
  - debtDueDate: str (a date with format "YYYY-MM-DD")
  - debtId: int
  
The "/payment" endpoint is to be used as a webhook and expects a JSON with fields:
  - debtId: str (string representation of an int)
  - paidAt: str (a date with format "YYYY-MM-DD HH:mm:ss")
  - paidAmount: int
  - paidBy: str
