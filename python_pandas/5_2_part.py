import pandas as pd

# apply
# map
# applymap
# replace

people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['og1', 'og2', 'og3'],
    "email": ['og1@ru', 'og2@ru', 'og3@ru'],
}

df = pd.DataFrame(people)

# apply - принимает аргументов функцию
# отобразит в колонке email длину значений всех строк
df['email'].apply(len)
# 0     6
# 1     6
# 2    17
# Name: email, dtype: int64

def update_email(email):
    return email.upper()
df['email'].apply(update_email)
# как пример вернет все адреса в верхнем регистре

# сохранить в колонку email изменения
df['email'] = df['email'].apply(update_email)

# вернуть адреса в нижний регистр
df['email'] = df['email'].apply(lambda c: c.lower())

# отобразит столбцы и кол-во строк, т.е. длину всех значений
df.apply(len)

len(df['email'])  # 3

# по умолчанию axis (индекс) rows (строки), axis=columns - вывести по индексу столбцов
df.apply(len, axis='columns')

# проверить эти методы
df.apply(pd.Series.min)
df.apply(lambda x: x.min())

# applymap применяется ко всем объектам экземпляра класса (т.е. все значения во всех строках)
df.applymap(len)
# 	first	last	email
# 0	5	3	6
# 1	4	3	6
# 2	4	5	17

# все значения в нижний регистр
df.applymap(str.lower)

# пример map, т.е. map заменит указанные значения колонки чьи ключи будут совпадать, а остальные в NaN
df['first'].map({'Corey': 'Chris', 'Jane': 'Mary'})
# 0    Chris
# 1     Mary
# 2      NaN
# Name: first, dtype: object

# пример replace, т.е. replace заменит указанные значения колонки, а остальные без изменения
df['first'] = df['first'].replace({'Corey': 'Chris', 'Jane': 'Mary'})
# 	first	last	email
# 0	Chris	og1	og1@ru
# 1	Mary	og2	og2@ru
# 2	John	og3	og3@ru
