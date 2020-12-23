import pandas as pd


df = pd.read_csv('data/ETH_1h.csv')

df.head()
# Date	Symbol	Open	High	Low	Close	Volume
# 0	2020-03-13 08-PM	ETHUSD	129.94	131.82	126.87	128.71	1940673.93
# 1	2020-03-13 07-PM	ETHUSD	119.51	132.02	117.10	129.94	7579741.09
# 2	2020-03-13 06-PM	ETHUSD	124.47	124.85	115.50	119.51	4898735.81
# 3	2020-03-13 05-PM	ETHUSD	124.08	127.42	121.63	124.47	2753450.92
# 4	2020-03-13 04-PM	ETHUSD	124.85	129.51	120.17	124.08	4461424.71

df.shape  # (23674, 7)

df.loc[0, 'Date']  # '2020-03-13 08-PM'

# преобразить в нужный формат datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %I-%p')
# 0   2020-03-13 20:00:00
# 1   2020-03-13 19:00:00
# Name: Date, dtype: datetime64[ns]

# до преобразования в более читабельный формат функция day_name() не сработает, т.к. тип колонки 'Date' - 'object/string'
df.loc[0, 'Date'].day_name()  # 'Friday'

# нужный формат datetime при инициализации экземпляра класса
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
