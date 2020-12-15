import pandas as pd


people = {
    "first": ['Corey', 'Jane', 'John'],
    "last": ['og1', 'og2', 'og3'],
    "email": ['og1@ru', 'og2@ru', 'og3@ru'],
}

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')
df = pd.DataFrame(people)

# отобразит все строки с булевыми значениями
df['last'] == 'Corey'
# 0    False
# 1    False
# 2    False
# Name: last, dtype: bool

# сохраним в переменную наш поиск (фильтер) и вызовем через аргумент в экземпляре класса df
filt = (df['last'] == 'Corey')
df[filt]
# email	first	last
# у нас пустые строки, т.е. нет совпадений

filt2 = (df['first'] == 'Corey')
df[filt2]  # или df[df['first'] == 'Corey']
#   email	first	last
# 0	og1@ru	Corey	og1

# можно использовать и через loc, чтобы удобнее было осуществлять вывод по нужным столбцам
df.loc[filt2, 'email']
# 0    og1@ru
# Name: email, dtype: object

# групповой поиск & (и) и | (или)
filt3 = (df['last'] == 'og1') & (df['email'] == 'og1@ru')
df.loc[filt3]
#     email	first	last
# 0	og1@ru	Corey	og1

filt3 = (df['last'] == 'og1') | (df['email'] == 'og2@ru')
df.loc[filt3, 'email']
# 0    og1@ru
# 1    og2@ru
# Name: email, dtype: object

# тильда (~) - значит не (not), т.е. отобразит все значения с приставкой не в начале фильтра
df.loc[~filt3, 'email']
# 2    og3@ru
# Name: email, dtype: object

# выборка по тем, у кого ежегодный доход выше 70000
high_salary = (df['ConvertedComp'] > 70000)
df.loc[high_salary]

# вывод не по всем колонкам, а по выбранным
df.loc[high_salary, ['Country', 'LanguageWorkedWith', 'ConvertedComp']]

# фильтр по определенным странам
countries = ['United States', 'India', 'United Kingdom', 'Germany', 'Canada']
filt = df['Country'].isin(countries)
df.loc[filt, 'Country']
# Respondent
# 1        United Kingdom
# 6                Canada
# 8                 India
# 10                India
# 12               Canada
#               ...
# 84539    United Kingdom
# 85182            Canada
# 85961    United Kingdom
# 86012             India
# 88377            Canada
# Name: Country, Length: 24059, dtype: object

df.loc[filt, 'Country'].value_counts()
# United States     20949
# India              9061
# Germany            5866
# United Kingdom     5737
# Canada             3395
# Name: Country, dtype: int64

# будет не совсем корректным такой способ, т.к. вывод будет только по строке, где совпадание Python единственное
p1 = ['Python']
filt2 = (df['LanguageWorkedWith'].isin(p1)) & (df['ConvertedComp'] > 50000)
df.loc[filt2, ['Country', 'LanguageWorkedWith']].value_counts()

# правильная выборка такая, через str.contains
# проверить что значит na=False
filt3 = df['LanguageWorkedWith'].str.contains('Python', na=False)
# df.loc[filt3, 'LanguageWorkedWith']
# Respondent
# 1                          HTML/CSS;Java;JavaScript;Python
# 2                                      C++;HTML/CSS;Python
# 4                                      C;C++;C#;Python;SQL
# 5              C++;HTML/CSS;Java;JavaScript;Python;SQL;VBA
# 8        Bash/Shell/PowerShell;C;C++;HTML/CSS;Java;Java...
#                                ...
# 84539    Bash/Shell/PowerShell;C;C++;HTML/CSS;Java;Java...
# 85738      Bash/Shell/PowerShell;C++;Python;Ruby;Other(s):
# 86566      Bash/Shell/PowerShell;HTML/CSS;Python;Other(s):
# 87739             C;C++;HTML/CSS;JavaScript;PHP;Python;SQL
# 88212                           HTML/CSS;JavaScript;Python
# Name: LanguageWorkedWith, Length: 36443, dtype: object
