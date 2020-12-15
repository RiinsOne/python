import pandas as pd


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# сортировка Country по алфавитному и ConvertedComp по убыванию, т.е. с максимальным значением
df.sort_values(by=['Country', 'ConvertedComp'], ascending=[True, False], inplace=True)

# отобразить 50 строк указанных столбцов
df[['Country', 'ConvertedComp']].head(50)

# отобразить 50 самых больших значений указанной колонки
df['ConvertedComp'].nlargest(10)

# отобразить 10 строк всех столбцов по значению ConvertedComp, где этот столбец имеет самые большие значения
df.nlargest(10, 'ConvertedComp')

# самые маленькие значения ConvertedComp, отобразит 10 строк всех столбцов
df.nsmallest(10, 'ConvertedComp')
