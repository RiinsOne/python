import datetime
from ogframework import newline
import ym

x = datetime.datetime(2019, 4, 29)
print(x.strftime('%d%b%elem'))

month1 = 'APR'
print(x.strftime(f'%d{month1}%elem'))

newline()
yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterdaysMonth = yesterday.strftime('%b')
print(yesterdaysMonth)
# print(type(yesterday.strftime('%d%b%elem')))
# print(yesterday.strftime('%d%b%elem'))
# print(yesterday.strftime('%b'))

newline()
currentMonth = datetime.datetime.now().month
print(currentMonth)
print(type(currentMonth))


def month():
    if currentMonth == 1:
        return 'JAN'
    if currentMonth == 2:
        return 'FEB'
    if currentMonth == 3:
        return 'MAR'
    if currentMonth == 4:
        return 'APR'


newline()
print(month())
print(yesterday.strftime(f'%d{month()}%elem'))

newline()
print(ym.xmlFileName)


#
