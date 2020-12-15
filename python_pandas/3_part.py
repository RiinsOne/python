import pandas as pd


people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['og1', 'og2', 'og3'],
    "email": ['og1@ru', 'og2@ru', 'og3@ru'],
}

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')
df = pd.DataFrame(people)

# сделать колонку email основной как индекс, удобно, т.к. почтовые адреса у всех уникальные
df.set_index('email')

# Index(['og1@ru', 'og2@ru', 'og3@ru'], dtype='object', name='email')
df.index

# loc теперь работает только по индексу email, loc[0] - выведет ошибку
df.loc['og1@ru']

# 'og1'
df.loc['og1@ru', 'last']

# iloc можно использовать по старому
df.iloc[0]
# first    Corey
# last       og1
# Name: og1@ru, dtype: object

# обнуление индекса по умолчанию
df.reset_index(inplace=True)
df
# email	first	last
# 0	og1@ru	Corey	og1
# 1	og2@ru	Jane	og2
# 2	og3@ru	John	og3

# теперь можно использовать loc
df.loc[0]

# можно задать индекс по умолчанию при определении экземпляра класса
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')

# индекс по умолчанию - Respondent
df.head()

# в схеме сделать индекс по умолчанию - Column
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

schema_df.loc['Hobbyist']
# QuestionText    Do you code as a hobby?
# Name: Hobbyist, dtype: object

schema_df.loc['MgrIdiot']
# QuestionText    How confident are you that your manager knows ...
# Name: MgrIdiot, dtype: object

schema_df.loc['MgrIdiot', 'QuestionText']
# 'How confident are you that your manager knows what they’re doing?'

# вывести сортированную таблицу, по умолчанию - A>Z, у нас Column основной индекс
schema_df.sort_index()
# Column      QuestionText
# Age	        What is your age (in years)? If you prefer not...
# Age1stCode	At what age did you write your first line of c...

# В обратном порядке
schema_df.sort_index(ascending=False)

# Отсортировать и изменить (сохранить) в экземпляре класса
schema_df.sort_index(inplace=True)
