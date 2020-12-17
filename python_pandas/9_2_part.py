# replace(), isna(), fillna(), astype(), dtypes, mean()

import pandas as pd
import numpy as np


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)

# заменить значения NA и Missing на np.nan и сохранить в экземпляре класса df
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)

# вернет таблицу со значениями True или False
df.isna()

# заменить все значения NaN, None на 'Missing'
df.fillna('MISSING')
df.fillna(0)

# все колонки являются объектами, в пандас это тип - строка
df.dtypes
# first    object
# last     object
# email    object
# age      object
# dtype: object

# df['age'].mean()
# TypeError: can only concatenate str (not "int") to str

# df['age'] = df['age'].astype(int)
# int() argument must be a string, a bytes-like object or a number, not 'NoneType'

type(np.nan)  # float

# изменить тип столбца age на float
df['age'] = df['age'].astype(float)

df.dtypes
# age теперь float64

# метод mean() считает "среднее значение" тех объектов, которые имеют значения
# т.е. в колонке age 7 значений (строк), но т.к. в трех из них np.na или None, то mean() считывает среднее значений по 4 строкам
df['age'].mean()

# метод astype() приводит объекты в нужный тип
# df.astype()
