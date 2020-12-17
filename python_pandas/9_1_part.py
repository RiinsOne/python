# dropna()

import pandas as pd
import numpy as np


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'],
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}

df = pd.DataFrame(people)

# удалить пустые строки - np.nan or None
df.dropna()

# тоже самое, что и df.dropna(), параметры по умолчанию
# axis на индекс и how=any -> т.е. drop по индексу если хоть в одной из колонок отсутствует значение
df.dropna(axis='index', how='any')

# how=all - удалить строки, если во всех колонках отсутствуют значения
df.dropna(axis='index', how='all')

# тоже самое, но по столбцам
df.dropna(axis='columns', how='all')

df.dropna(axis='columns', how='any')
# все значения будут пустыми, т.к. во всех колонках присутствуют np.nan или None значения

# удалить строки, где нет значений в столбце email
# при how=all будет такой же результат, т.к. есть аргумент subset
df.dropna(axis='index', how='any', subset=['email'])

# drop тех строк, где и last и email имеют None
# inplace=True для сохранения в экземпляре класса
df.dropna(axis='index', how='all', subset=['last', 'email'])
