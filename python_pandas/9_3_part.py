# practice with csv

import pandas as pd


# создать список с перечнем "missing values" и указать их при инициализации экземпляра класса
na_vals = ['NA', 'Missing']
df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent', na_values=na_vals)
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df['YearsCode'].head(10)

# df['YearsCode'].mean()
# can only concatenate str (not "int") to str

# df['YearsCode'] = df['YearsCode'].astype(float)
# ValueError: could not convert string to float: 'Less than 1 year'

# заменить 'Less than 1 year' на 0
df['YearsCode'].replace('Less than 1 year', 0, inplace=True)

df['YearsCode'].replace('More than 50 years', 51, inplace=True)

df['YearsCode'] = df['YearsCode'].astype(float)

df['YearsCode'].dtypes  # dtype('float64')

df['YearsCode'].mean()  # 11.660681389160544

df['YearsCode'].median()  # 9.0
