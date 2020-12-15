from datetime import datetime
import pytz


WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print('You spent {} units'.format(amount))
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()

    def show_balance(self):
        print('Balance: {}'.format(self.__balance))

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(
                '{color} {amount} {white} {transaction} on {date}'.format(
                    color = color,
                    amount = amount,
                    white = WHITE,
                    transaction = transaction,
                    date = date.astimezone()
                )
            )


a = Account('og', 0)

# a.deposit(152)
# a.deposit(213)
# a.withdraw(180)
# a.deposit(600)
#
# a.show_history()
