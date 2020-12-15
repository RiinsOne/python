accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and return the event_more_view balance."""
    accounts[name] += amount
    return accounts[name]


add_balance(500.00, 'savings')
print(accounts['savings'])  # 4195.5

add_balance(500.00)
print(accounts['checking'])  # 2458.0
