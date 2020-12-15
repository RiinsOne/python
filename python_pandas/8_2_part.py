# среднее значение колонки по странам, т.к. групбай по странам
country_grp['ConvertedComp'].median()

# можно применять метод лок
country_grp['ConvertedComp'].median().loc['Germany']

# можно выводить и два метода, через метод .agg
country_grp['ConvertedComp'].agg(['median', 'mean'])
# 	       median	 mean
# Country
# Afghanistan	6222.0	101953.333333
# Albania	10818.0	21833.700000
# Algeria	7878.0	34924.047619
# Andorra	160931.0	160931.000000
# Angola	7764.0	7764.000000

# и с помощью лок по нужной строке
country_grp['ConvertedComp'].agg(['median', 'mean']).loc['Canada']
# median     68705.000000
# mean      134018.564909
# Name: Canada, dtype: float64

# вывести общее количестов знающих людей Пайтон в Индии, sum() возвращает сумму True
filt = df['Country'].str.lower() == 'india'
df.loc[filt]['LanguageWorkedWith'].str.contains('Python').sum()
# 3105

# country_grp['LanguageWorkedWith'].str.contains('Python').sum()  # AttributeError: 'SeriesGroupBy' object has no attribute 'str'

# можно применить apply, если str не работает
country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
# Country
# Afghanistan                              8
# Albania                                 23
# Algeria                                 40

#
country_respondents = df['Country'].value_counts()
country_respondents

#
country_uses_python = country_grp['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
country_uses_python

# соединить две групбай
python_df = pd.concat([country_respondents, country_uses_python], axis='columns', sort=False)
python_df
#               Country	LanguageWorkedWith
# United States	    20949	10083
# India	            9061	 3105
# Germany	       5866	   2451

# переименовать колонки
python_df.rename(columns={'Country': 'NumRespondents', 'LanguageWorkedWith': 'NumKnowsPython'}, inplace=True)
python_df
#                 NumRespondents	NumKnowsPython
# United States	20949	10083
# India	          9061	3105

# добавить ещё колонку, в нашем случае процент знающих
python_df['PctKnowsPython'] = (python_df['NumKnowsPython']/python_df['NumRespondents']) * 100
python_df
#                 NumRespondents	NumKnowsPython	PctKnowsPython
# United States	  20949	10083	48.131176
# India	          9061	3105	34.267741
# Germany	          5866	2451	41.783157

# сортировка
python_df.sort_values(by='PctKnowsPython', ascending=False, inplace=True)
python_df

#
python_df.loc['Japan']
# NumRespondents    391.000000
# NumKnowsPython    182.000000
# PctKnowsPython     46.547315
# Name: Japan, dtype: float64
