import pandas as pd


people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com'],
}

df = df.append({'first': 'Adam', 'last': 'Doe', 'email': 'A@email.com'}, ignore_index=True)

# сортировка по алфавитному порядку
df.sort_values(by='last')

# сортировка в обратном порядке
df.sort_values(by='last', ascending=False)

# сортировка в обратном порядке,сначала last, потом first
df.sort_values(by=['last', 'first'], ascending=False)

# сортировка last в обратном, first по алфавитному
df.sort_values(by=['last', 'first'], ascending=[False, True])

# сортировка с изменением экземпляра класса
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)

# вернуть назад, если указать inplace=True, то сохранит в экземпляр класса
df.sort_index()

# в алфавитном порядке, но индекс в обратном
df['last'].sort_values()
# 3        Doe
# 1        Doe
# 2        Doe
# 0    Schafer
# Name: last, dtype: object
