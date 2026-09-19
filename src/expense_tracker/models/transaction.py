
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    id: int
    type: str
    amount: float
    category: str
    description: str
    created_at: datetime

