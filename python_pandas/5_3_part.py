import pandas as pd


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

df.head()

# переименовать столбец ConvertedComp в SalaryUSD
df.rename(columns={'ConvertedComp': 'SalaryUSD'}, inplace=True)
df['SalaryUSD']
# Respondent
# 1            NaN
# 2            NaN
# 3         8820.0
# 4        61000.0
# 5            NaN
#           ...
# 88377        NaN
# 88601        NaN
# 88802        NaN
# 88816        NaN
# 88863        NaN
# Name: SalaryUSD, Length: 88883, dtype: float64

# заменить с помощью map столбец Hobbyist на True и False
df['Hobbyist'] = df['Hobbyist'].map({'Yes': True, 'No': False})
df['Hobbyist']
# Respondent
# 1         True
# 2        False
# 3         True
# 4        False
# 5         True
#          ...
# 88377     True
# 88601    False
# 88802    False
# 88816    False
# 88863     True
# Name: Hobbyist, Length: 88883, dtype: bool
