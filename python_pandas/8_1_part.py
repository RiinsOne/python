import pandas as pd


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# среднее значение столбца, если значения NaN, то они пропускаются
df['ConvertedComp'].median()
# 57287.0

# среднее значение всех столбцов с плавующей точкой, т.е. float
df.median()
# CompTotal        62000.0
# ConvertedComp    57287.0
# WorkWeekHrs         40.0
# CodeRevHrs           4.0
# Age                 29.0
# dtype: float64

# полное описание всех столбцов float, например кол-во, минимальное, 25%, 50% и т.д.
df.describe()

# полное описание выбранной колонки
df['ConvertedComp'].describe()

# общее кол-во данных/строк, NaN не учитываются
df['ConvertedComp'].count()

# итоговый подсчет всех значений указанной колонки
df['Hobbyist'].value_counts()

# пример поиска по фильтру
filt1 = df['SocialMedia'].str.lower() == 'youtube'
df.loc[filt1, 'SocialMedia'].count()  # 13830

# normalize=True приведет результат в проценты
df['SocialMedia'].value_counts()
df['SocialMedia'].value_counts(normalize=True)

# группировать и создать новый экземпляр класс по выбранной колонки
country_grp = df.groupby(['Country'])

#
country_grp
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x09F5DE80>

# выведет все данные только по стране Индия
country_grp.get_group('India')

# тоже самое без группировки, а через фильтр
filt = df['Country'] == 'India'
df.loc[filt]
# df.loc[filt, 'SocialMedia'].value_counts()
df.loc[filt]['SocialMedia'].value_counts()

# т.к. экземпляр класса groupby, то выведет первый столбец страны и дальше значения выбранной колонки
# т.е. страны становятся строками и к данному экземпляру классу можно применять метод loc
country_grp['SocialMedia'].value_counts()
# Country      SocialMedia
# Afghanistan  Facebook                    15
#              YouTube                      9
#              I don't use social media     6
#              WhatsApp                     4
#              Instagram                    1

# пример через групбай по стране Индиа
country_grp['SocialMedia'].value_counts().loc['India']

# пример по RF с нормализацией, т.е. выведением данных в процентах
country_grp['SocialMedia'].value_counts(normalize=True).loc['Russian Federation']
