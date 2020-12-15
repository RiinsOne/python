import pandas as pd


people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['Schafer', 'Doe', 'Doe'],
    "email": ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com'],
}

df = pd.DataFrame(people)

# соединить два столбца
df['first'] + ' ' + df['last']

# соединить два столбца и сохранить
df['full_name'] = df['first'] + ' ' + df['last']

#
df
# 	first	last	email	full_name
# 0	Corey	Schafer	CoreyMSchafer@gmail.com	Corey Schafer
# 1	Jane	Doe	JaneDoe@email.com	Jane Doe
# 2	John	Doe	JohnDoe@email.com	John Doe

# удалить столбцы
df.drop(columns=['first', 'last'])
# 	email	full_name
# 0	CoreyMSchafer@gmail.com	Corey Schafer
# 1	JaneDoe@email.com	Jane Doe
# 2	JohnDoe@email.com	John Doe

# inplace=True для сохранения
df.drop(columns=['first', 'last'], inplace=True)

# метод сплит для строки
df['full_name'].str.split(' ')
# 0    [Corey, Schafer]
# 1         [Jane, Doe]
# 2         [John, Doe]
# Name: full_name, dtype: object

# expand=True приводит в более нужный вид
df['full_name'].str.split(' ', expand=True)
# 	0	1
# 0	Corey	Schafer
# 1	Jane	Doe
# 2	John	Doe

# создадим и сохраним в столбцы first и last значения
df[['first', 'last']] = df['full_name'].str.split(' ', expand=True)
#   email	full_name	first	last
# 0	CoreyMSchafer@gmail.com	Corey Schafer	Corey	Schafer
# 1	JaneDoe@email.com	Jane Doe	Jane	Doe
# 2	JohnDoe@email.com	John Doe	John	Doe

# добавить новую строку с first Tony, остальные значения будут NaN
df.append({'first': 'Tony'}, ignore_index=True)

people2 = {
    "first": ['Tony', 'Steve'],
    "last": ['Stark', 'Rogers'],
    "email": ['IronMan@avenge.com', 'Cap@avenge.com'],
}

df2 = pd.DataFrame(people2)

# отобразить соединение двух таблиц, те таблицы данных которых нет будут NaN
df.append(df2, ignore_index=True, sort=False)
#     email	full_name	first	last
# 0	CoreyMSchafer@gmail.com	Corey Schafer	Corey	Schafer
# 1	JaneDoe@email.com	Jane Doe	Jane	Doe
# 2	JohnDoe@email.com	John Doe	John	Doe
# 3	IronMan@avenge.com	NaN	Tony	Stark
# 4	Cap@avenge.com	NaN	Steve	Rogers

# сохранить в экземпляр класса
df = df.append(df2, ignore_index=True, sort=False)

# удалить строку с индексом 4
df.drop(index=4)

# пример фильтра по фамилии Doe и удаление строк с индексами где есть это совпадение
filt = df['last'] == 'Doe'
df.drop(index=df[filt].index)
