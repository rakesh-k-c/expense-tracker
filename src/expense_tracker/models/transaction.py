
from dataclasses import dataclass
from datetime import datetime

from .enums import TransactionType, IncomeCategoryType, ExpenseCategoryType


@dataclass
class Transaction:
    id: int
    type: TransactionType
    amount: float
    category: IncomeCategoryType | ExpenseCategoryType
    description: str
    created_at: datetime

