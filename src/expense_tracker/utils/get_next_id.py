


def get_next_id(transactions):
    if len(transactions) == 0:
        return 1

    return max(transaction.id for transaction in transactions) + 1