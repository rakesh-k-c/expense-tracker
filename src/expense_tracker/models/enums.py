

from enum import Enum

class TransactionType(Enum):
    INCOME="income"
    EXPENSE="expense"

class IncomeCategoryType(Enum):
    SALARY="salary"
    RENT="rent"
    INVESTMENT_RETURN="investment_return"
    OTHER="other"

class ExpenseCategoryType(Enum):
    FOOD="food"
    FASHION="fashion"
    HOUSEHOLD_ACCESSORIES="household_accessories"
    OTHER="other"