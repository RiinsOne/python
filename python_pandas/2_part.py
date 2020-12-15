import pandas as pd

people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['og1', 'og2', 'og3'],
    "email": ['og1@ru', 'og2@ru', 'og3@ru'],
}

# экземпляр класса для словаря, но DataFrame может намного больше
df = pd.DataFrame(people)

# выведет в табличном стиле все строки из столбца email
df['email']
# 0    og1@ru
# 1    og2@ru
# 2    og3@ru
# Name: email, dtype: object

type(df['email'])
# pandas.core.series.Series

# можно и через точку, но так не желательно
df.email

# можно вывести все строки двух столбцов
df[['last', 'email']]
# 	last	email
# 0	og1	og1@ru
# 1	og2	og2@ru
# 2	og3	og3@ru

# список всех стобцов и тип объекта, object - строка
df.columns
Index(['first', 'last', 'email'], dtype='object')

# iloc отображает в табличном стиле указанную строку по индексу
df.iloc[0]
# first     Corey
# last        og1
# email    og1@ru
# Name: 0, dtype: object

# с двумя аргументами со списком внутри отобразит две строки по индексу
df.iloc[[0, 1]]
#     first	last	email
# 0	Corey	og1	og1@ru
# 1	Jane	og2	og2@ru

# в таком варианте отобразит две строки и 3ий столбец (2ой по индексу)
df.iloc[[0, 1], 2]
# 0    og1@ru
# 1    og2@ru
# Name: email, dtype: object

# loc аналогичен iloc, но позволяет выводить строки с указанием столбцов по имени
df.loc[0]
# 0    og1@ru
# 1    og2@ru
# Name: email, dtype: object

df.loc[[0, 1], ['email', 'last']]
# 	email	last
# 0	og1@ru	og1
# 1	og2@ru	og2


df = pd.read_csv('data/survey_results_public.csv')

# выведет название всех столбцов в формате списка объекта класса Index
df.columns

# выведет все строки столбца/колонки Hobbyist
df['Hobbyist']

# отобразит количество совпадающих значений в колонке Hobbyist
df['Hobbyist'].value_counts()
# Yes    71257
# No     17626
# Name: Hobbyist, dtype: int64

# для примера, столбец Hobbyist, строка 1, по индексу 0 - 'Yes'
df.loc[0, 'Hobbyist']

# первые три строки колонки Hobbyist
# не забываем, что перечисление строк внутри списка [[]]
df.loc[[0, 1, 2], 'Hobbyist']

# можно использовать срезы, тогда дополнительный список не нужен
df.loc[0:4, 'Hobbyist']
# 0    Yes
# 1     No
# 2    Yes
# 3     No
# 4    Yes
# Name: Hobbyist, dtype: object

# через срезы можно использовать и название столбцов
df.loc[0:2, 'Hobbyist':'OpenSource']
# Hobbyist	OpenSourcer	OpenSource
# 0	Yes	Never	The quality of OSS and closed source software ...
# 1	No	Less than once per year	The quality of OSS and closed source software ...
# 2	Yes	Never	The quality of OSS and closed source software ...
