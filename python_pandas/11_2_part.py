import pandas as pd

from sqlalchemy import create_engine
import psycopg2


df = pd.read_csv('data/survey_results_public.csv', index_col='Respondent')
schema_df = pd.read_csv('data/survey_results_schema.csv', index_col='Column')

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

filt1 = (df['Country'] == 'India')
india_df = df.loc[filt1]
india_df.head()

# pip install SQLAlchemy
# pip install psycopg2-binary

# юзер:пароль@адрес_хоста:порт/имя_базы
engine = create_engine('postgresql://dbuser:dbpass@localhost:5432/sample_db')

# sqlite3
db_engine = create_engine('sqlite:///data/database.sqlite3')

india_df.head().to_sql('sample_table', db_engine)
# если нет таблицы, то создаст
# Respodent также запишется

# 'append' - чтобы добавить к существующей таблице
# 'replace' - заменить
india_df.head().to_sql('sample_table', db_engine, if_exists='append')

sql_df = pd.read_sql('sample_table', db_engine, index_col='Respondent')
sql_df.head()

# запрос к таблице
sql_df = pd.read_sql_query('SELECT * FROM sample_table LIMIT 2', db_engine, index_col='Respondent')
sql_df

# пример чтения файла с веб-страницы
posts_df = pd.read_json('https://....../posts.json')
posts_df
