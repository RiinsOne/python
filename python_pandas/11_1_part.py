import pandas as pd


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

filt1 = (df['Country'] == 'India')
india_df = df.loc[filt1]
india_df.head()

india_df.to_csv('data/modified.csv')

# tsv - tab separate value
india_df.head(3).to_csv('data/modified.tsv', sep='\t')

# Для excel необходим доустановить следующие пакеты
# pip install xlwt openpyxl xlrd
india_df.head(3).to_excel('data/modified.xlsx')

test = pd.read_excel('data/modified.xlsx', index_col='Respondent', engine='openpyxl')
test

india_df.head().to_json('data/modified.json')

# более привычный формат json, наподобие dict в python
india_df.head().to_json('data/modified_2.json', orient='records', lines=True)

# respodent колонка пропадет, т.к. мы выбрали respodent как индекс и не записали индекс
# нужно обновить сбросить индекс и перезаписать india_df.reset_index()
test2 = pd.read_json('data/modified_2.json', orient='records', lines=True)
