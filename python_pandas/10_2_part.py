import pandas as pd


d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)

# через класс dt и метод day_name() преобразит в дни недели
df['Date'].dt.day_name()
# 0          Friday
#            ...
# 23673    Saturday
# Name: Date, Length: 23674, dtype: object

# создать столбец DayOfWeek со днями недели
df['DayOfWeek'] = df['Date'].dt.day_name()

df.head(3)
# Date	Symbol	Open	High	Low	Close	Volume	DayOfWeek
# 0	2020-03-13 20:00:00	ETHUSD	129.94	131.82	126.87	128.71	1940673.93	Friday
# 1	2020-03-13 19:00:00	ETHUSD	119.51	132.02	117.10	129.94	7579741.09	Friday
# 2	2020-03-13 18:00:00	ETHUSD	124.47	124.85	115.50	119.51	4898735.81	Friday

df['Date'].min()  # Timestamp('2017-07-01 11:00:00')
df['Date'].max()  # Timestamp('2020-03-13 20:00:00')
df['Date'].max() - df['Date'].min()  # Timedelta('986 days 09:00:00')

filt = (df['Date'] >= '2020')
# последняя строка поиска по фильтру будет 2020-01-01 00:00:00
df.loc[filt]
# 1748	2020-01-01 00:00:00	ETHUSD	128.54	128.54	128.12	128.34	245119.91	Wednesday

filt1 = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt1]
# last row - 2019-01-01 00:00:00

filt2 = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt2]
# как и предыдущий результат

df.set_index('Date', inplace=True)

# более быстрый доступ к датам, если настроить даты как индекс
df['2019']
# 	Symbol	Open	High	Low	Close	Volume	DayOfWeek
# Date
# 2019-12-31 23:00:00	ETHUSD	128.33	128.69	128.14	128.54	440678.91	Tuesday
# ...	...	...	...	...	...	...	...
# 2019-01-01 00:00:00	ETHUSD	130.53	131.91	130.48	131.62	1067136.21	Tuesday

df['2020-01':'2020-02']
# от 2020-01-01 00:00 до 2020-02-29 23:00

df['2020-01':'2020-02']['Close'].mean()  # 195.1655902777778

df['2020-01-01']['High'].max()  # 132.68
