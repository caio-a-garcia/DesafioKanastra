"""
Define model for the application.

Classes used for the application are defined here.
"""
from pydantic import BaseModel


class DebtItem(BaseModel):
    """Model for API request body."""

    name: str
    governmentId: int
    email: str
    debtAmount: float
    debtDueDate: str
    debtId: int
    amountPaid: float = 0.0
    amountDue: float
    paid: bool = False

    def __init__(self, name, governmentId, email,
                 debtAmount, debtDueDate, debtId, amountDue=0.0):
        """Initialize unpaid debt item."""
        super().__init__(name=name,
                         governmentId=governmentId,
                         email=email,
                         debtAmount=debtAmount,
                         debtDueDate=debtDueDate,
                         debtId=debtId,
                         amountDue=amountDue)

        self.name = name
        self.governmentId = governmentId
        self.email = email
        self.debtAmount = debtAmount
        self.debtDueDate = debtDueDate
        self.debtId = debtId
        self.amountDue = debtAmount

    def __str__(self):
        """Use debtId as string representation.

        debtId is used because it is suposed a unique identifier.
        """
        return self.debtId

    def __eq__(self, other):
        """Compare DebtItems by debtId."""
        return self.debtId == other.debtId


class PaymentItem(BaseModel):
    """Model for payments made."""

    debtId: int
    paidAt: str
    paidAmount: float
    paidBy: str

    def __init__(self, debtId, paidAt, paidAmount, paidBy):
        """Register a payment to be processed."""
        super().__init__(debtId=debtId,
                         paidAt=paidAt,
                         paidAmount=paidAmount,
                         paidBy=paidBy)

        self.debtId = debtId
        self.paidAt = paidAt
        self.paidAmount = paidAmount
        self.paidBy = paidBy
