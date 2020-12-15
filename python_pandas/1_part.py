import pandas as pd


# создаем экземпляр класса df с методом read_csv
df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

# вывести кортеж из количества строк и столбцов (88883, 85)
df.shape

# (85, 2)
schema_df

# изменить настройки экземпляра класса pd на отображение, 85 колонок и 85 строк
pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# сбросить настройки по умолчанию
pd.reset_option('display.max_columns')

# полная информация о экземпляре класса (т.е. открытом файле), наименования всех столбцов, данных по умолчанию и тип данных
df.info

# tail - отобразить последние 5 строк, по умолчанию.
# tail(10) - последение 10 строк
# head - первые строки
df.tail()
df.tail(10)
df.head()
df.head(15)
