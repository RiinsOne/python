import datetime

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterdaysMonth = yesterday.strftime('%b')


def month():
    if yesterdaysMonth == 'Jan':
        return 'JAN'
    if yesterdaysMonth == 'Feb':
        return 'FEB'
    if yesterdaysMonth == 'Mar':
        return 'MAR'
    if yesterdaysMonth == 'Apr':
        return 'APR'
    if yesterdaysMonth == 'May':
        return 'MAY'
    if yesterdaysMonth == 'Jun':
        return 'JUN'
    if yesterdaysMonth == 'Jul':
        return 'JUL'
    if yesterdaysMonth == 'Aug':
        return 'AUG'
    if yesterdaysMonth == 'Sep':
        return 'SEP'
    if yesterdaysMonth == 'Oct':
        return 'OCT'
    if yesterdaysMonth == 'Nov':
        return 'NOV'
    if yesterdaysMonth == 'Dec':
        return 'DEC'


yesterdayDate = yesterday.strftime(f'%d{month()}%elem')
xmlFileName = f'152{yesterdayDate}CKP.XML.gz.enc'

"""
yesterdaysMonthUpperCase = yesterdaysMonth.upper()
print(yesterdaysMonthUpperCase)
yesterdayDateSecondVar = yesterday.strftime(f'%d{yesterdaysMonthUpperCase}%elem')
print(yesterdayDateSecondVar)
"""

#
