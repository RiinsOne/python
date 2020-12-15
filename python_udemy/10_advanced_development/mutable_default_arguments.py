def create_account(name: str, holder: str, account_holders: list = []):
    print(id(account_holders))
    account_holders.append(holder)

    return {
        'name': name,
        'main_account_holder': holder,
        'account_holders': account_holders
    }


# 8996304
# 8996304

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

print(a2)
# {'name': 'savings', 'main_account_holder': 'Jen', 'account_holders': ['Rolf', 'Jen']}


def create_account(name: str, holder: str, account_holders=None):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)
