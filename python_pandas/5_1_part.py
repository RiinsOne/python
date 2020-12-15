import pandas as pd


people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['og1', 'og2', 'og3'],
    "email": ['og1@ru', 'og2@ru', 'og3@ru'],
}

df = pd.DataFrame(people)

# отобразить столбцы
df.columns
# Index(['first', 'last', 'email'], dtype='object')

# изменить названия столбцов можно через список, но тогда требуется перечисление всех столбцов
df.columns = ['first_name', 'last_name', 'email']
df.columns
# Index(['first_name', 'last_name', 'email'], dtype='object')

# можно менять через list comprehension
df.columns = [x.upper() for x in df.columns]

# можно использовать строковые методы
df.columns = df.columns.str.replace(' ', '_')

# снова list comprehension
df.columns = [x.lower() for x in df.columns]

# изменение название колонок через словарь columns, можно указать только нужные столбцы, изменения в экземпляр класса не сохранятся
df.rename(columns={'first_name': 'first', 'last_name': 'last'})

# тоже самое, но с сохранием в экземпляр класса
df.rename(columns={'first_name': 'first', 'last_name': 'last'}, inplace=True)

# изменить данные строки с индексом 2
df.loc[2] = ['John', 'Smith', 'JohnSmith@email.com']

# изменить только перечисленные столбцы
df.loc[2, ['last', 'email']] = ['Doe', 'JohnDoe@email.com']

# изменить один столбец, тут список не нужен
df.loc[2, 'last'] = 'Smith'

# про at прочитать внимательнее
df.at[2, 'last'] = 'Joe'

# фильтер используем для поиска нужной строки
filt = (df['email'] == 'JohnDoe@email.com')
df[filt]['last'] = 'Smith'  # ошибка - SettingWithCopyWarning
# изменить значение строки по фильтру так нельзя, ошибка вверху

# изменяем колонку last строки, которую ищем с помощью фильтра filt
df.loc[filt, 'last'] = 'Smith'

# вывести колонку email с строковым методом lower
df['email'].str.lower()

# тоже самое, только с сохранием в экземпляр класса
df['email'] = df['email'].str.lower()
