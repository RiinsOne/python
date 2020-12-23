import pandas as pd


d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('data/ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)

df.set_index('Date', inplace=True)

# отобразит максимальные значения за каждый день, т.к. указали аргументом .resample('D'), т.е. Day
df['High'].resample('D').max()
# Date
# 2017-07-01    279.99
#                ...
# 2020-03-13    148.00
# Freq: D, Name: High, Length: 987, dtype: float64

highs = df['High'].resample('D').max()
highs['2020-01-01']  # 132.68

# импортировать модуль matplotlib
%matplotlib inline

# отобразить граффик highs
highs.plot()  # <AxesSubplot:xlabel='Date'>

# среднее значение по неделям
df.resample('W').mean()
# 	Open	High	Low	Close	Volume
# Date
# 2017-07-02	268.066486	271.124595	264.819730	268.202162	2.185035e+06
# ...	...	...	...	...	...
# 2020-03-15	176.937521	179.979487	172.936239	176.332821	4.259828e+06

# для столбца Close - среднее, для High - максимальное и т.д.
df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
# 	Close	High	Low	Volume
# Date
# 2017-07-02	268.202162	293.73	253.23	8.084631e+07
# ...	...	...	...	...
# 2020-03-15	176.332821	208.65	90.00	4.983998e+08
